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

            animals = [ 
                Animal(
                    a['id'], a['name'], a['breed'],
                    a['location_id'], a['customer_id'], a['status']
                ).__dict__ for a in dataset 
            ]

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

            animal =  Animal(data['id'], data['name'], data['breed'],
                            data['location_id'], data['customer_id'], data['status'])

            return json.dumps(animal.__dict__)