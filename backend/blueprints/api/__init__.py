from flask import Blueprint

api_bp = Blueprint("api", __name__, )


@api_bp.route("/")
def index():
    return "喵這是API"
