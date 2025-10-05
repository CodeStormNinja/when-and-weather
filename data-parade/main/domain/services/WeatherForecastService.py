from datetime import datetime
import pandas as pd

from main.common.utils.DateTimeUtils import DateTimeUtils
from main.domain.constants import KeyMapConstants
from main.domain.dtos.WeatherForecastResponseDto import WeatherForecastResponseDto
from main.infrastructure.http.GeocodeHttpContext import GeocodeHttpContext
from main.infrastructure.http.WeatherForecastHttpContext import WeatherForecastHttpContext

class WeatherForecastService:
    
    def __init__(self):
        
        self._weather_forecast_http_context = WeatherForecastHttpContext()
        self._geocode_http_context = GeocodeHttpContext()
    
    def get_forecast(self, location, iso_datetime):
        
        converted_datetime = datetime.fromisoformat(iso_datetime)
        response_geocode = self._geocode_http_context.get_coordinates_by_location_name(location)
        lat = response_geocode[0]["lat"]
        lon = response_geocode[0]["lon"]
        
        if DateTimeUtils.is_before_tomorrow(converted_datetime.date()) is False:
            date_string = converted_datetime.date().strftime("%Y-%m-%d")
            response_forecast = self._weather_forecast_http_context.forecast_by_coordinates_and_period(lat, lon, date_string, date_string)
            response = self._extract_forecast_hourly_data_from_current_hour(response_forecast, converted_datetime)
            
        else:
            nasa_date_string = converted_datetime.date().strftime("%Y%m%d")
            response_search = self._weather_forecast_http_context.search_by_coordinates_and_period(lat, lon, nasa_date_string, nasa_date_string)
            
            hourly_data = pd.DataFrame(response_search["hourly"]["properties"]["parameter"])
            daily_data = pd.DataFrame(response_search["daily"]["properties"]["parameter"])
            current_hour_data = hourly_data.loc[hourly_data.index == nasa_date_string + str(converted_datetime.hour).zfill(2)].to_dict(orient="records")[0]
            current_day_data = daily_data.loc[daily_data.index == nasa_date_string].to_dict(orient="records")[0]
            joined_data = {**current_hour_data, **current_day_data}
            nasa_missing_params = self._get_missing_nasa_params(joined_data)
            if len(nasa_missing_params) > 0:
                open_meteo_date_string = converted_datetime.date().strftime("%Y-%m-%d")
                open_meteo_missing_params = [KeyMapConstants.NASA_PARAMS_TO_OPEN_METEO_PARAMS[nasa_param] for nasa_param in nasa_missing_params]
                joined_data = {key: value for key, value in joined_data.items() if key not in nasa_missing_params}
                response_forecast = self._weather_forecast_http_context.forecast_by_coordinates_and_period_and_hourly_parameters(lat, lon, open_meteo_date_string, open_meteo_date_string, open_meteo_missing_params)
                open_meteo_found_data = self._extract_forecast_hourly_data_from_current_hour(response_forecast, converted_datetime)
                joined_data = {**joined_data, **open_meteo_found_data}
            response = joined_data
            
        response = {KeyMapConstants.WEATHER_FORECAST_PARAMS_TO_RESPONSE_DTO[key]: value for key, value in response.items()}
        
        return WeatherForecastResponseDto.model_validate(response)
    
    def _get_missing_nasa_params(self, nasa_results):
        return [key for key, value in nasa_results.items() if value == -999.0]
    
    def _extract_forecast_hourly_data_from_current_hour(self, forecast_response, converted_datetime):
        forecast_dataframe = pd.DataFrame(forecast_response["hourly"])
        forecast_dataframe["time"] = pd.to_datetime(forecast_dataframe["time"])
        selected_hour = forecast_dataframe.loc[forecast_dataframe["time"].dt.hour == converted_datetime.hour]
        selected_hour = selected_hour.drop(columns=["time"])
        return selected_hour.to_dict(orient="records")[0]