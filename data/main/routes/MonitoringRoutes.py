from flask_restx import Namespace, Resource
from flask import current_app
import time
import requests

from main.common.utils.DateTimeUtils import DateTimeUtils
from main.infrastructure.http.HttpContext import HttpContext

ns = Namespace("health", description="Application Health Check")

@ns.route("")
class HealthCheckResource(Resource):
    
    def __init__(self, api):
        self._http_context = HttpContext()
        super().__init__(api)
    
    def get(self):
        
        api_name = current_app.config.get("API_NAME")
        app_started_at_utc = current_app.config.get("APPLICATION_STARTED_AT_UTC")
        geocode_api_url = current_app.config.get("GEOCODE_API_URL")
        weather_forecast_api_url = current_app.config.get("OPEN_METEO_API_URL")

        info = {
            "status": "ok",
            "service": api_name,
            "started_at_utc": app_started_at_utc,
            "requested_at_utc": DateTimeUtils.utc_now_iso(),
            "uptime_s": round(time.time() - DateTimeUtils.utc_to_timestamp(app_started_at_utc), 1),
        }
            
        deps = {}
        
        deps["open_meteo"] = self._test_external_service(weather_forecast_api_url + "/v1/forecast", "get", params={
            "latitude": 0, "longitude": 0,
            "hourly": "temperature_2m",
            "forecast_days": 1, "timezone": "UTC"
        })
        
        deps["geocode"] = self._test_external_service(geocode_api_url + "/search", "get", params={
            "q": "United States", 
            "format": "json", 
            "limit": 1
        })

        info["deps"] = deps
        
        for dep in deps.values():
            if dep["status"] == "fail":
                info["status"] = "fail"
                break

        result_status_code = 200 if info["status"] == "ok" else 503
        return info, result_status_code
    
    def _test_external_service(self, url, method_name, params, headers={}):
        method = getattr(self._http_context, method_name)
        try:
            t0 = time.perf_counter()
            method(url=url, params=params, headers=headers)
            return {
                "status": "ok",
                "latency_ms": round((time.perf_counter() - t0) * 1000, 1)
            }
        except Exception as e:
            return {
                "status": "fail", 
                "error": type(e).__name__
            }
    
    def _test_external_service(self, url, method_name, params, headers={}):
        method = getattr(self._http_context, method_name)
        try:
            t0 = time.perf_counter()
            method(url=url, params=params, headers=headers)
            return {
                "status": "ok",
                "latency_ms": round((time.perf_counter() - t0) * 1000, 1)
            }
        except Exception as e:
            return {
                "status": "fail", 
                "error": type(e).__name__
            }