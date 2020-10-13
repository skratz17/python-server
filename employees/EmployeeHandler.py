from helpers import BasicHandler
from models import Employee, Location

class EmployeeHandler(BasicHandler):
    _VALID_QUERY_COLUMNS = {
        "id": True,
        "name": True,
        "address": True,
        "location_id": True
    }

    def __build_expanded_employee_from_row(self, row):
        employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

        location = Location(row['location_id'], row['location_name'], row['location_address'])

        employee.location = location.__dict__

        return employee.__dict__

    def _get_all(self, cursor):
        cursor.execute("""
        SELECT 
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM Employee e
        JOIN Location l
            ON l.id = e.location_id
        """)

        results = cursor.fetchall()

        employees = [ self.__build_expanded_employee_from_row(row) for row in results ]

        return employees

    def _get_by_criteria(self, cursor, key, value):
        if key in self._VALID_QUERY_COLUMNS:
            cursor.execute(f"""
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id,
                l.name location_name,
                l.address location_address
            FROM Employee e
            JOIN Location l
                ON l.id = e.location_id
            WHERE e.{key} = ?
            """, ( value, ))

            results = cursor.fetchall()

            employees = [ self.__build_expanded_employee_from_row(row) for row in results ]

            return employees

    def _create(self, cursor, employee):
        cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id )
        VALUES
            ( ?, ?, ? )
        """, ( employee['name'], employee['address'], employee['location_id'] ))

        id = cursor.lastrowid
        employee['id'] = id

        return employee

    def _update(self, cursor, id, employee):
        cursor.execute("""
        UPDATE Employee
        SET
            name = ?,
            address = ?,
            location_id = ?
        WHERE id = ?
        """, ( employee['name'], employee['address'], employee['location_id'], id ))

        rows_affected = cursor.rowcount

        return rows_affected != 0

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE FROM Employee
        WHERE id = ?
        """, ( id, ))