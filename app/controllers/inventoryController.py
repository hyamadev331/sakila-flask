from app.models.inventory import Inventory
from app.models.store import Store
from app.models.film import Film
from __init__ import db


def getInventory():
    inventory = (
        db.session.query(Inventory, Store, Film)
        .join(Store, Inventory.store_id == Store.store_id)
        .join(Film, Inventory.film_id == Film.film_id)
        .all()
    )
    inventory_list = []
    for item, store, film in inventory:
        inventory_data = {
            "inventory_id": item.inventory_id,
            "title": film.title,
        }
        inventory_list.append(inventory_data)
    return inventory_list
