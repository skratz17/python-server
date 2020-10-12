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

def get_single_employee(id):
    for employee in EMPLOYEES:
        if(employee["id"] == id):
            return employee

    return None

def create_employee(employee):
    employee["id"] = get_next_id(EMPLOYEES)

    EMPLOYEES.append(employee)
    return employee

def update_employee(id, employee):
    replace_item_with_matching_id(EMPLOYEES, id, employee)

def delete_employee(id):
    remove_item_by_id(EMPLOYEES, id)