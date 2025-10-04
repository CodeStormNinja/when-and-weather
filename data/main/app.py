from flask import Flask
from flask_restx import Api, Namespace

from main.config.Config import Config
from main.routes.WeatherForecastRoutes import ns as weather_forecast_ns

def create_app():
    
    # CONFIGURATION
    app = Flask(__name__)
    app.config.from_object(Config())
    
    # SWAGGER
    api = Api(
        app=app, 
        version="1.0", 
        title="When & Weather (Data API) - A data API used for weather forecasting", 
        description="Weather Forecast API", 
        doc="/"
    )
    
    # ROUTES
    api.add_namespace(weather_forecast_ns)

    return app