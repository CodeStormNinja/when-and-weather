from flask_restx import Namespace, Resource
from flask import current_app
import time
import requests

from main.common.utils.DateTimeUtils import DateTimeUtils

ns = Namespace("health", description="Application Health Check")

@ns.route("")
class HealthCheckResource(Resource):
    
    def get(self):
        
        api_name = current_app.config.get("API_NAME")
        app_started_at_utc = current_app.config.get("APPLICATION_STARTED_AT_UTC")
        open_meteo_url = current_app.config.get("OPEN_METEO_API_URL")
        open_meteo_timeout = current_app.config.get("OPEN_METEO_TIMEOUT_SECS")

        info = {
            "status": "ok",
            "service": api_name,
            "started_at_utc": app_started_at_utc,
            "requested_at_utc": DateTimeUtils.utc_now_iso(),
            "uptime_s": round(time.time() - DateTimeUtils.utc_to_timestamp(app_started_at_utc), 1),
        }
            
        deps = {}
        try:
            t0 = time.perf_counter()
            r = requests.get(
                open_meteo_url,
                params={
                    "latitude": 0, "longitude": 0,
                    "hourly": "temperature_2m",
                    "forecast_days": 1, "timezone": "UTC"
                },
                timeout=float(open_meteo_timeout)
            )
            r.raise_for_status()
            deps["open_meteo"] = {
                "status": "ok",
                "latency_ms": round((time.perf_counter() - t0) * 1000, 1)
            }
        except Exception as e:
            deps["open_meteo"] = {
                "status": "fail", 
                "error": type(e).__name__
            }

        info["deps"] = deps
        
        for dep in deps.values():
            if dep["status"] == "fail":
                info["status"] = "fail"
                break

        result_status_code = 200 if info["status"] == "ok" else 503
        return info, result_status_code