from __init__ import db


class Film(db.Model):
    __tablename__ = "film"

    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    language_id = db.Column(db.Integer)
    rental_duration = db.Column(db.Integer)
    rental_rate = db.Column(db.Numeric(4, 2))
    length = db.Column(db.Integer)
    replacement_cost = db.Column(db.Numeric(5, 2))
    rating = db.Column(db.String(255))
    special_features = db.Column(db.String(255))
    last_update = db.Column(db.DateTime)
