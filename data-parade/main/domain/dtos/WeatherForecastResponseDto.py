from pydantic import BaseModel, Field

class WeatherForecastResponseDto(BaseModel):
    temperature_2m: float = Field(..., example=0.0)
    rain: float = Field(..., example=0.0)
    precipitation_probability: float = Field(..., example=0.0)
    wind_gusts_10m: float = Field(..., example=0.0)
    snowfall: float = Field(..., example=0.0)