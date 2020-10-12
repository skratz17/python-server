import sqlite3
import json 

from helpers import BasicHandler
from models import Animal

class AnimalHandler(BasicHandler):
    def get_all(self):
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

    def get_single(self, id):
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
            WHERE a.id = ?
            """, ( id, ))

            data = db_cursor.fetchone()

            animal =  Animal(**data)

            return json.dumps(animal.__dict__)

    def get_by_criteria(self, key, value):
        pass