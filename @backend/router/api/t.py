from flask import Blueprint, render_template, request, session, redirect, url_for, abort

api_bp = Blueprint("api", __name__)


@api_bp.route("/")
def index():
    return "test"
