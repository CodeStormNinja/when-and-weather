from flask import current_app

class GeocodeHttpContext:

    def __init__(self):
        self._http_context = HttpContext()
        self.base_url = current_app.config.get("GEOCODE_API_URL")

    def get(self, params):
        return self._http_context.get(
            self.base_url,
            params=params
        )