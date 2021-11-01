from flask import Blueprint

api_tem = Blueprint("api", __name__, )


@api_tem.route("/")
def index():
    return "喵這是API"
