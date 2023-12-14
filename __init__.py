from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+pymysql://root:pass@localhost:3306/sakila"

    db.init_app(app)

    return app
