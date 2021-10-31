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
        self.register_blueprint(routers)

        # errors
        @self.errorhandler(400)
        def error_400(error):
            return render_template("errors/400.html")

        @self.errorhandler(404)
        def error_404(error):
            """404錯誤處理"""
            return render_template("errors/404.html")

        @self.errorhandler(500)
        def error_500(error):
            """500錯誤處理"""
            return render_template("errors/500.html")


app = mainApp()


@app.route("/")
def index():
    # random get 6*8 photos using api
    return render_template("home/index.html", title="Hello World !", imgLinks=[{
        "user": "",
        "alt": "",
        "uptime": "",
    }])


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("port") or 80)
