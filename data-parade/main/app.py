from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from main.common.utils.DateTimeUtils import DateTimeUtils
from main.config.Config import Config
from main.api.routes.MonitoringRoutes import ns as monitoring_ns
from main.api.routes.WeatherForecastRoutes import ns as weather_forecast_ns

def create_app():
    
    # CONFIGURATION
    app = Flask(__name__)
    app.config.from_object(Config())
    app.config["APPLICATION_STARTED_AT_UTC"] = DateTimeUtils.utc_now_iso()
    
    # SWAGGER
    api = Api(
        app=app, 
        version="1.0", 
        title="When & Weather (Data API) - A data API used for weather forecasting", 
        description="Weather Forecast API", 
        doc="/"
    )
    
    # ROUTES
    api.add_namespace(monitoring_ns)
    api.add_namespace(weather_forecast_ns)

    # CORS
    CORS(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)