import datetime
from ..extensions import db

"""
primary_key = True (設定為主鍵)
unique = True (設定為不重複值)
nullable = True (允許為空值)
index = True (建立索引值)
default = "預設值"
"""


class User(db.Model):
    """ 用戶 """
    __tablename__ = "User"
    id: str = db.Column(db.Integer, unique=True, primary_key=True)
    name: str = db.Column(db.String(30), unique=True)
    account: str = db.Column(db.String(30), unique=True)
    password: str = db.Column(db.String(30))

    def __init__(self, id: int, name: str, account: str, password: str):
        self.id = id
        self.name = name
        self.account = account
        self.password = password


class Photo(db.Model):
    """ 圖片 """
    __tablename__ = "Photo"
    id: str = db.Column(db.Integer, unique=True, primary_key=True)
    name: str = db.Column(db.String(30), unique=True)
    belongs: User = db.Column(db.relationship("", back_populates=""), unique=True, index=True)
    upload_time: str = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    private: bool = db.Column(db.Boolean, default=False)
    description: str = db.Column(db.String(200))

    def __init__(self, id: int, name: str, belongs: User, upload_time: str, private: bool, description: str):
        self.id = id
        self.name = name
        self.belongs = belongs
        self.upload_time = upload_time
        self.private = private
        self.description = description


class Tag(db.Model):
    """ 標籤 """
    __tablename__ = "Tag"
    content: str = db.Column(db.String(200))
    color: str = db.Column(db.String(20))
    attach: Photo = db.relationship("User", )

    def __init__(self, content: str, color: str, attach: Photo):
        self.content = content
        self.color = color
        self.attach = attach
