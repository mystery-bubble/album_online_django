# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv
from flask import Flask
from flask.templating import render_template
from flask_cors import CORS

from backend.blueprints import routers
from backend.db import db
from backend.settings import config

load_dotenv()


class mainApp(Flask):
    def __init__(self, *args, **options):
        super().__init__(__name__, static_folder="./frontend/static",
                         template_folder="./frontend/templates",
                         *args, **options)

        self.cors = CORS(self, resources={
            "/*": {
                "origins": "*"
            }
        })

        self.db = db.init_app(self)
        self.config.from_object(config["BaseConfig"])

        # 移除 {% if %}空白
        self.jinja_env.trim_blocks = True
        self.jinja_env.lstrip_blocks = True

        # 添加 blueprint
        self.register_blueprint(routers)

        # errors
        @self.errorhandler(400)
        def error_400(error):
            """400錯誤處理"""
            return render_template("errors/400.html")

        @self.errorhandler(403)
        def error_403(error):
            """403錯誤處理"""
            return render_template("errors/403.html")

        @self.errorhandler(404)
        def error_404(error):
            """404錯誤處理"""
            return render_template("errors/404.html")

        @self.errorhandler(413)
        def error_413(error):
            """413錯誤處理"""
            return render_template("errors/413.html")

        @self.errorhandler(500)
        def error_500(error):
            """500錯誤處理"""
            return render_template("errors/500.html")


app = mainApp()


@app.route("/")
def index():
    # random get 6*8 photos using api
    return render_template("main/index.html", title="Hello World !", imgLinks=[{
        "user": "",
        "alt": "",
        "uptime": "",
    }])


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT") or 8080)
