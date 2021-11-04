import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ALLOWED_EXTENSIONS = ["jpeg", "gif", "jpg", "png",
                          "mov", "mp4", "mpg"]
    MAX_CONTENT_LENGTH = 1000 * 1024 * 1024  # 1000 MB
    SQLALCHEMY_DATABASE_URI = os.getenv("SQL_URL")
    UPLOAD_PATH = os.path.join(basedir, 'uploads')


config = {
    "BaseConfig": BaseConfig
}
