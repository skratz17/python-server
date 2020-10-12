import sqlite3
import json

from models import Customer
from helpers import remove_item_by_id, replace_item_with_matching_id

CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct"
    },
    {
        "id": 2,
        "name": "Zap \"BrowserRouter\" Rowsdower",
        "address": "100 Main Street"
    },
    {
        "id": 3,
        "name": "Brom Grombo",
        "address": "200 Pain Street"
    },
    {
        "email": "jweckert17@gmail.com",
        "password": "test",
        "name": "Jacob Eckert",
        "id": 4
    }
]

def get_all_customers():
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

def get_single_customer(id):
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

def update_customer(id, customer):
    replace_item_with_matching_id(CUSTOMERS, id, customer)

def delete_customer(id):
    remove_item_by_id(CUSTOMERS, id)