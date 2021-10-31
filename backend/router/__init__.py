from flask import Blueprint
from .api import api_tem

routers = Blueprint("routers", __name__)
routers.register_blueprint(api_tem, url_prefix="/api")
