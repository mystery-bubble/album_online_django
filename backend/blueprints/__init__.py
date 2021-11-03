from flask import Blueprint
from .api import api_bp
from .main import main_bp

routers = Blueprint("routers", __name__)
routers.register_blueprint(api_bp, url_prefix="/api")
routers.register_blueprint(main_bp, url_prefix="/")
