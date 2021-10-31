# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route("/")
def test():
    return render_template("")


@app.route("/api")
def api():
    return


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("port") or 80)
