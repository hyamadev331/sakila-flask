from __init__ import db


class Store(db.Model):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True)
    manager_staff_id = db.Column(db.Integer)
    address_id = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)
