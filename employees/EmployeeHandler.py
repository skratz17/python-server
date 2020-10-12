from models import Employee
from helpers import BasicHandler

class EmployeeHandler(BasicHandler):
    _VALID_QUERY_COLUMNS = {
        "id": True,
        "name": True,
        "address": True,
        "location_id": True
    }

    def _get_all(self, cursor):
        cursor.execute("""
        SELECT 
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        """)

        results = cursor.fetchall()

        employees = [ (Employee(**employee)).__dict__ for employee in results ]

        return employees

    def _get_by_id(self, cursor, id):
        cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        WHERE e.id = ?
        """, ( id, ))

        result = cursor.fetchone()

        employee = Employee(**result)

        return employee.__dict__

    def _get_by_criteria(self, cursor, key, value):
        if key in self._VALID_QUERY_COLUMNS:
            cursor.execute(f"""
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id
            FROM Employee e
            WHERE e.{key} = ?
            """, ( value, ))

            results = cursor.fetchall()

            employees = [ (Employee(**employee)).__dict__ for employee in results ]

            return employees

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE FROM Employee
        WHERE id = ?
        """, ( id, ))