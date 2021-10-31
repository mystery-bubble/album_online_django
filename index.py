from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route("/")
def test():
    return "Hello World!"


@app.route("/api")
def api():
    return


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("port") or 80)
