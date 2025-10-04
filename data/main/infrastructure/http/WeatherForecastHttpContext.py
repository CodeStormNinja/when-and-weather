from flask import current_app

from main.infrastructure.http.HttpContext import HttpContext

class WeatherForecastHttpContext:

    def __init__(self):
        self._http_context = HttpContext()
        self._base_url = current_app.config.get("OPEN_METEO_API_URL") + "/v1"

    def forecast_by_coordinates_and_period(self, latitude, longitude, start_date, end_date):
        return self._http_context.get(self._base_url + "/forecast", params={
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