from flask import Blueprint, request, current_app, render_template
import os

from backend.utils import rename_image


main_bp = Blueprint("main", __name__, )


@main_bp.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST" and "file" in request.files:
        file = request.files.get("file")
        filename = rename_image(file.filename)
        file.save(os.path.join(current_app.config["UPLOAD_PATH"], filename))
    return render_template("")
