from flask import Blueprint, render_template, request, session, redirect, url_for, abort

api_tem = Blueprint("api", __name__, )


@api_tem.route("/")
def index():
    return "awa"
