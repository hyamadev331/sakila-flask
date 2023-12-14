from __init__ import db


class Inventory(db.Model):
    __tablename__ = "inventory"

    inventory_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer)
    store_id = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)
