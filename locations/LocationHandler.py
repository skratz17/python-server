import sqlite3
import json

from models import Location
from helpers import BasicHandler

class LocationHandler(BasicHandler):
    def get_all(self):
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

    def get_single(self, id):
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