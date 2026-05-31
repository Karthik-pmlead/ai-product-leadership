from flask import Flask
from flask_cors import CORS
from .utils.config import Config

def create_app():
    """Application factory."""
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints
    from .api.endpoints import api
    app.register_blueprint(api, url_prefix='/api')
    
    return app
