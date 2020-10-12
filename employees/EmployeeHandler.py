import sqlite3
import json

from models import Employee
from helpers import BasicHandler

class EmployeeHandler(BasicHandler):
    def get_all(self):
        with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                e.id,
                e.name,
                e.address,
                e.location_id
            FROM Employee e
            """)

            results = db_cursor.fetchall()

            employees = [ (Employee(**employee)).__dict__ for employee in results ]

        return json.dumps(employees)

    def get_single(self, id):
        with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id
            FROM Employee e
            WHERE e.id = ?
            """, ( id, ))

            result = db_cursor.fetchone()

            employee = Employee(**result)

            return json.dumps(employee.__dict__)