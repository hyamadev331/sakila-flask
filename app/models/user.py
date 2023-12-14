from flask_login import UserMixin
from __init__ import db


class User(db.Model, UserMixin):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(45))
    password = db.Column(db.String(45))

    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id
