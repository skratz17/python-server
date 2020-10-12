import sqlite3
import json

from models import Customer
from helpers import BasicHandler

class CustomerHandler(BasicHandler):
    _VALID_QUERY_COLUMNS = { 
        "id": True,
        "name": True,
        "address": True,
        "email": True
    }

    def get_all(self):
        with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                c.id,
                c.name,
                c.address,
                c.email,
                c.password
            FROM Customer c
            """)

            dataset = db_cursor.fetchall()

            customers = [ (Customer(**customer)).__dict__ for customer in dataset ]

        return json.dumps(customers)

    def get_single(self, id):
        with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                c.id,
                c.name,
                c.address,
                c.email,
                c.password
            FROM Customer c
            WHERE c.id = ?
            """, ( id, ))

            result = db_cursor.fetchone()

            customer = Customer(**result)

            return json.dumps(customer.__dict__)

    def get_by_criteria(self, key, value):
        if key in self._VALID_QUERY_COLUMNS:
            with sqlite3.connect("./kennel.db") as conn:
                conn.row_factory = sqlite3.Row
                db_cursor = conn.cursor()

                db_cursor.execute(f"""
                SELECT
                    c.id,
                    c.name,
                    c.address,
                    c.email,
                    c.password
                FROM Customer c
                WHERE c.{key} = ?
                """, (value, ))

                results = db_cursor.fetchall()

                customers = [ (Customer(**customer)).__dict__ for customer in results ]
                return json.dumps(customers)