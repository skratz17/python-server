import sqlite3
import json

from models import Location
from helpers import get_next_id, remove_item_by_id, replace_item_with_matching_id

LOCATIONS = [
  {
    "id": 1,
    "name": "Nashville North",
    "address": "8422 Johnson Pike"
  },
  {
    "id": 2,
    "name": "Nashville South",
    "address": "209 Emory Drive"
  }
]

def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        """)

        results = db_cursor.fetchall()

        locations = [ (Location(**location)).__dict__ for location in results ]

    return json.dumps(locations)

def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        WHERE l.id = ?
        """, ( id, ))

        result = db_cursor.fetchone()

        location = Location(**result)

        return json.dumps(location.__dict__)

def create_location(location):
    location["id"] = get_next_id(LOCATIONS)

    LOCATIONS.append(location)
    return location

def update_location(id, location):
    replace_item_with_matching_id(LOCATIONS, id, location)

def delete_location(id):
    remove_item_by_id(LOCATIONS, id)