from flask import current_app

from main.infrastructure.http.HttpContext import HttpContext

class WeatherForecastHttpContext:

    def __init__(self):
        self._http_context = HttpContext()
        self._open_meteo_url = current_app.config.get("OPEN_METEO_API_URL") + "/v1"
        self._nasa_power_url = current_app.config.get("NASA_POWER_API_URL")
        
    def forecast_by_coordinates_and_period(self, latitude, longitude, start_date, end_date):
        return self._http_context.get(self._open_meteo_url + "/forecast", params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ",".join([
                "temperature_2m",
                "rain",
                "precipitation_probability",
                "wind_gusts_10m",
                "snowfall"
            ]),
            "start_date": start_date,
            "end_date": end_date,
            "timezone": "auto"
        })
    
    def forecast_by_coordinates_and_period_and_hourly_parameters(self, latitude, longitude, start_date, end_date, hourly_parameters):
        return self._http_context.get(self._open_meteo_url + "/forecast", params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ",".join(hourly_parameters),
            "start_date": start_date,
            "end_date": end_date,
            "timezone": "auto"
        })
    
    def search_by_coordinates_and_period(self, latitude, longitude, start_date, end_date):
        
        results = {}
        
        results["hourly"] = self._http_context.get(self._nasa_power_url + "/temporal/hourly/point", params={
            "latitude": latitude,
            "longitude": longitude,
            "community": "sb",
            "parameters": ",".join([
                "T2M",
                "WS10M",
                "PRECSNO"
            ]),
            "time-standard": "utc",
            "start": start_date,
            "end": end_date,
        })
        
        results["daily"] = self._http_context.get(self._nasa_power_url + "/temporal/daily/point", params={
            "latitude": latitude,
            "longitude": longitude,
            "community": "sb",
            "parameters": ",".join([
                "IMERG_PRECTOT",
                "IMERG_PRECLIQUID_PROB"
            ]),
            "time-standard": "utc",
            "start": start_date,
            "end": end_date,
        })
        
        return results