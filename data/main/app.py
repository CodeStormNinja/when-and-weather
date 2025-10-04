from flask import Flask
from main.config.Config import Config

def create_app():
    
    # CONFIGURATION
    app = Flask(__name__)
    app.config.from_object(Config())

    return app