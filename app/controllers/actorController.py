from flask import jsonify
from app.models.actor import Actor


def get_actors():
    actors = Actor.query.all()
    actor_list = []
    for actor in actors:
        actor_data = {
            "actor_id": actor.actor_id,
            "first_name": actor.first_name,
            "last_name": actor.last_name,
            "last_update": actor.last_update,
        }
        actor_list.append(actor_data)
    return actor_list


def get_actor_by_id(actor_id):
    actor = Actor.query.filter_by(actor_id=actor_id).first()
    actor_data = {
        "actor_id": actor.actor_id,
        "first_name": actor.first_name,
        "last_name": actor.last_name,
        "last_update": actor.last_update,
    }
    return actor_data
