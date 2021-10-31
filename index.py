# -*- coding: utf-8 -*-

from flask import Flask
from dotenv import load_dotenv
import os

from flask.templating import render_template
from backend.router import routers

load_dotenv()

class mainApp(Flask):
    def __init__(self, *args, **options):
        super().__init__(__name__, static_folder="./frontend/static",
                         template_folder="./frontend/templates", *args, **options)

        # 移除 {% if %}空白
        self.jinja_env.trim_blocks = True
        self.jinja_env.lstrip_blocks = True

        # 添加 blueprint
        self.register_blueprint(routers, url_prefix="/api")


app = mainApp()


@app.route("/")
def index():
    # random get 6*8 photos using api
    return render_template("home/index.html", title="Hello World !")


if __name__ == "__main__":
    app.run( debug=True, port=os.getenv( "port" ) or 80 )
