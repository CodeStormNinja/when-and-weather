class Config:
    
    # BASIC CONFIG
    API_NAME = "when-and-weather-data-api"
    
    # HTTP CONFIG
    DEFAULT_HTTP_TIMEOUT_SECS = 5
    
    # EXTERNAL SERVICES
    OPEN_METEO_API_URL = "https://api.open-meteo.com"
    GEOCODE_API_URL = "https://nominatim.openstreetmap.org"
    NASA_POWER_API_URL = "https://power.larc.nasa.gov/api"
    
    # HEALTH-CHECK
    APPLICATION_STARTED_AT_UTC = None
    
    # SWAGGER
    RESTX_MASK_SWAGGER = False