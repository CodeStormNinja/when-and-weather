from flask import jsonify
from flask_restx import Namespace, Resource, abort
from pydantic import ValidationError

from main.api.swagger.models.WeatherForecastSwaggerModels import WeatherForecastRequestSwaggerModel, WeatherForecastResponseSwaggerModel
from main.domain.dtos.WeatherForecastRequestDto import WeatherForecastRequestDto
from main.domain.services.WeatherForecastService import WeatherForecastService

ns = Namespace("weather-forecast", description="Weather Forecast operations")
for m in [WeatherForecastRequestSwaggerModel, WeatherForecastResponseSwaggerModel]:
    if m.name not in ns.models:
        ns.add_model(m.name, m)

@ns.route("")
class WeatherForecastResource(Resource):
    
    def __init__(self, api, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self._weather_forecast_service = WeatherForecastService()
    
    @ns.expect(WeatherForecastRequestSwaggerModel, validate=True)
    @ns.marshal_with(WeatherForecastResponseSwaggerModel, code=200, skip_none=True)
    @ns.response(400, "Invalid request")
    @ns.response(500, "Internal server error")
    def post(self):
        
        try:
            dto = WeatherForecastRequestDto.model_validate(ns.payload or {})
        except ValidationError as e:
            abort(400, message="Invalid request body", errors=e.errors())
        
        try:
            result = self._weather_forecast_service.get_forecast(dto.location, dto.datetime)
            return result, 200
        except Exception as e:
            ns.logger.error(f"Error in WeatherForecastResource POST: {str(e)}")
            abort(500, message="An error occurred while processing the request")