from models import Customer
from helpers import BasicHandler

class CustomerHandler(BasicHandler):
    _VALID_QUERY_COLUMNS = { 
        "id": True,
        "name": True,
        "address": True,
        "email": True
    }

    def _get_all(self, cursor):
        cursor.execute("""
        SELECT 
            c.id,
            c.name,
            c.address,
            c.email
        FROM Customer c
        """)

        dataset = cursor.fetchall()

        customers = [ (Customer(**customer)).__dict__ for customer in dataset ]

        return customers

    def _get_by_criteria(self, cursor, key, value):
        if key in self._VALID_QUERY_COLUMNS:
            cursor.execute(f"""
            SELECT
                c.id,
                c.name,
                c.address,
                c.email,
                c.password
            FROM Customer c
            WHERE c.{key} = ?
            """, (value, ))

            results = cursor.fetchall()

            customers = [ (Customer(**customer)).__dict__ for customer in results ]
            return customers

    def _create(self, cursor, customer):
        cursor.execute("""
        INSERT INTO Customer
            ( name, address, email, password )
        VALUES
            ( ?, ?, ?, ? )
        """, ( customer['name'], customer['address'], customer['email'], customer['password'] ))

        id = cursor.lastrowid
        customer['id'] = id

        return customer

    def _update(self, cursor, id, customer):
        cursor.execute("""
        UPDATE Customer
        SET
            name = ?,
            address = ?,
            email = ?,
            password = ?
        WHERE id = ?
        """, ( customer['name'], customer['address'], customer['email'],
                customer['password'], id ))

        rows_affected = cursor.rowcount

        return rows_affected != 0

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE FROM Customer
        WHERE id = ?
        """, ( id, ))

        return cursor.rowcount != 0