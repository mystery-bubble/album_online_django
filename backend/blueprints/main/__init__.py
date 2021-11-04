import os

from backend.utils import rename_image
from flask import (Blueprint, current_app, render_template, request,
                   send_from_directory)

main_bp = Blueprint("main", __name__, )


@main_bp.route("/upload", methods=["GET", "POST"])
def upload():
    print(request.files)
    if request.method == "POST" and "file" in request.files:
        file = request.files.get("file")
        filename = rename_image(file.filename)
        file.save(os.path.join(f"{current_app.config['UPLOAD_PATH']}/img", filename))
    return "awa"


@main_bp.route("/uploads", methods=["GET", "POST"])
def uploads():
    print(request.files)
    if request.method == "POST" and "files[]" in request.files:
        file = request.files.get("files[]")
        filename = rename_image(file.filename)
        file.save(os.path.join(f"{current_app.config['UPLOAD_PATH']}/img", filename))
    # return
    return "awa"


@main_bp.route("/photo/<path:id>")
def photo(id):
    return send_from_directory(f"{current_app.config['UPLOAD_PATH']}/img", id)


@main_bp.route("/avatars/<path:id>")
def avatars(id):
    return send_from_directory(f"{current_app.config['UPLOAD_PATH']}/avatars", id)
