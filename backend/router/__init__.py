from flask import Blueprint
from .error import error_tem
from .api import api_tem

routers = Blueprint("routers", __name__)
routers.register_blueprint(error_tem)
routers.register_blueprint(api_tem)
