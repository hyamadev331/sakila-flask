from flask import Blueprint, render_template, redirect, url_for
from app.controllers.actorController import get_actors, get_actor_by_id
from app.controllers.loginController import login, logout, profile
from app.controllers.inventoryController import getInventory

routes = Blueprint("routes", __name__)


@routes.route("/")
def login():
    return render_template("login.html")


@routes.route("/authenticate", methods=["POST"])
def authenticate():
    if login():
        return redirect(url_for("routes.home"))
    else:
        return redirect(url_for("routes.login"))


@routes.route("/home")
def home():
    return render_template("home.html")


@routes.route("/inventory")
def inventory():
    inventory = getInventory()
    return render_template("inventory.html", inventory=inventory)


@routes.route("/actors")
def actors():
    actors = get_actors()
    return render_template("inventory.html", actors=actors)


@routes.route("/actors/<int:actor_id>")
def actor(actor_id):
    return get_actor_by_id(actor_id)
