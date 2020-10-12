import sqlite3
import json

from models import Employee
from helpers import get_next_id, remove_item_by_id, replace_item_with_matching_id

EMPLOYEES = [
    {
        "name": "TEST CRAETION",
        "locationId": 2,
        "animalId": 3,
        "id": 1
    }
]

def get_all_employees():
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

def get_single_employee(id):
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

def create_employee(employee):
    employee["id"] = get_next_id(EMPLOYEES)

    EMPLOYEES.append(employee)
    return employee

def update_employee(id, employee):
    replace_item_with_matching_id(EMPLOYEES, id, employee)

def delete_employee(id):
    remove_item_by_id(EMPLOYEES, id)