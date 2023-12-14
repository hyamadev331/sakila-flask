from flask_login import login_user, logout_user, current_user
from app.models.user import User
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, flash


def logout():
    logout_user()


def profile():
    return "Hello, {}".format(current_user.username)


def set_password(self, password):
    self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")


def check_password(self, password):
    set_password(password)
    return check_password_hash(self.password_hash, password)


def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.get(username)

    if user is None or not user.check_password(password):
        flash("Invalid username or password")
        return

    login_user(user)
