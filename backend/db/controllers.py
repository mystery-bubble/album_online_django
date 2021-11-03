import jwt
import hashlib
from werkzeug import exceptions
from dotenv import load_dotenv
import datetime
import os

from . import models
from . import errors


class User:
    def __init__(self):
        load_dotenv()
        self.session = models.db.session
        self.secret = os.getenv("JWT_SECRET")

    def signup(self, **data):
        data.password = hashlib.sha256(bytes(data.password, encoding="ascii")).hexdigest()
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        pass

    def login(self, account, password):
        target_user = models.Users.query.filter_by(account=account).first()
        if not target_user:
            raise errors.UserNotFound
        else:
            hash_password = hashlib.sha256(bytes(password, encoding="ascii")).hexdigest()
            if hash_password == target_user.password:
                data = {
                    "exp": datetime.datetime.now() + datetime.timedelta(minutes=30),
                    "uid": target_user.id
                }
                return jwt.encode(data, self.secret)
            else:
                raise errors.PasswordIncorrect

    def authorization(self, reauth: bool, token):
        if not reauth:
            try:
                decoded_token = jwt.decode(token, self.secret, leeway=20)
            except jwt.ExpiredSignatureError:
                raise errors.TokenExpired
            except jwt.exceptions.DecodeError:
                raise errors.TokenInvalid
            target_user = User.query.get(decoded_token.id)
            if not target_user:
                raise errors.UserNotFound
            return target_user
        else:
            raise errors.TokenUpdateRequired

    def logout():
        # need logger
        pass

    def delete(self, user_id):
        target_user = User.query.get(user_id)
        if not target_user:
            raise errors.UserNotFound
        self.session.delete(target_user)
        self.session.commit()


class Photo:
    def getRandom(amount):
        pass

    def getUserAlbum(user_id):
        pass

    def getSpecificOne(photo_id):
        pass

    def deleteOne(photo_id):
        pass

    def deleteMany(photo_id_array):
        pass

    def upload(**data):
        pass

    def updateDescription(photo_id, new_description):
        pass

    def changePublic(photo_id):
        pass

    def updateName(photo_id, new_name):
        pass


class Tag:
    def create(**data):
        pass

    def getPhotoTags(photo_id):
        pass

    def delete(tag_id):
        pass
