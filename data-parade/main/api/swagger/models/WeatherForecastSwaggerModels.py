from flask_restx import Model, fields

WeatherForecastRequestSwaggerModel = Model("WeatherForecastRequestSwaggerModel", {
    "location": fields.String(required=True, description="Location name", example="São Paulo"),
    "datetime": fields.String(required=True, description="Local ISO datetime", example="2025-09-12T20:00:00Z")
})

WeatherForecastResponseSwaggerModel = Model("WeatherForecastResponseSwaggerModel", {
    "temperature_2m": fields.Float(required=True, description="Air temperature at 2 meters above ground level in Celsius", example=23.5),
    "rain": fields.Float(required=True, description="Rain from large scale weather systems of the preceding hour in millimeters", example=0.0),
    "precipitation_probability": fields.Float(required=True, description="Probability of precipitation with more than 0.1 mm of the preceding hour. Probability is based on ensemble weather models with 0.25° (~27 km) resolution. 30 different simulations are computed to better represent future weather conditions.", example=0.0),
    "wind_gusts_10m": fields.Float(required=True, description="Wind speed at 10 meters above ground", example=15.0),
    "snowfall": fields.Float(required=True, description="Snowfall amount of the preceding hour in centimeters.", example=0.0)
})