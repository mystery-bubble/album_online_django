import os

from backend.utils import rename_image
from flask import (Blueprint, current_app, render_template, request,
                   send_from_directory)

main_bp = Blueprint("main", __name__, )


@main_bp.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST" and "file" in request.files:
        file = request.files.get("file")
        filename = rename_image(file.filename)
        file.save(os.path.join(current_app.config["UPLOAD_PATH"], filename))
    return render_template("")


@main_bp.route("/photo/<path:id>")
def photo(id):
    return send_from_directory(f"{current_app.config['UPLOAD_PATH']}/img", id)


@main_bp.route("/avatars/<path:id>")
def avatars(id):
    return send_from_directory(f"{current_app.config['UPLOAD_PATH']}/avatars", id)
