from datetime import datetime
import pandas as pd

from main.domain.dtos.WeatherForecastResponseDto import WeatherForecastResponseDto
from main.infrastructure.http.GeocodeHttpContext import GeocodeHttpContext
from main.infrastructure.http.WeatherForecastHttpContext import WeatherForecastHttpContext

class WeatherForecastService:
    
    def __init__(self):
        
        self._weather_forecast_http_context = WeatherForecastHttpContext()
        self._geocode_http_context = GeocodeHttpContext()
    
    def get_forecast(self, location, iso_datetime):
        
        converted_datetime = datetime.fromisoformat(iso_datetime)
        date_string = converted_datetime.date().strftime("%Y-%m-%d")
        response_geocode = self._geocode_http_context.get_coordinates_by_location_name(location)
        lat = response_geocode[0]["lat"]
        lon = response_geocode[0]["lon"]
        response_forecast = self._weather_forecast_http_context.forecast_by_coordinates_and_period(lat, lon, date_string, date_string)
        forecast_dataframe = pd.DataFrame(response_forecast["hourly"])
        forecast_dataframe["time"] = pd.to_datetime(forecast_dataframe["time"])
        selected_hour = forecast_dataframe.loc[forecast_dataframe["time"].dt.hour == converted_datetime.hour]
        response = selected_hour.to_dict(orient="records")[0]
        
        return WeatherForecastResponseDto.model_validate(response)