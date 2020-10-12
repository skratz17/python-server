import sqlite3
import json 

from models import Animal
from helpers import get_next_id, remove_item_by_id, replace_item_with_matching_id

ANIMALS = []

def get_all_animals():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        """)

        dataset = db_cursor.fetchall()

        animals = [ (Animal(**animal)).__dict__ for animal in dataset ]

    return json.dumps(animals)

def get_single_animal(id):
    requested_animal = None

    # each animal variable here is a "dictionary" in Python, basically analogous to an "object" in JS
    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    animal["id"] = get_next_id(ANIMALS)

    ANIMALS.append(animal)
    return animal

def update_animal(id, new_animal):
    replace_item_with_matching_id(ANIMALS, id, new_animal)

def delete_animal(id):
    remove_item_by_id(ANIMALS, id)