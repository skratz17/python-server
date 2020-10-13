from models import Location
from helpers import BasicHandler

class LocationHandler(BasicHandler):
    _VALID_QUERY_COLUMNS = {
        "id": True,
        "name": True,
        "address": True
    }

    def _get_all(self, cursor):
        cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        """)

        results = cursor.fetchall()

        locations = [ (Location(**location)).__dict__ for location in results ]

        return locations

    def _get_by_criteria(self, cursor, key, value):
        if key in self._VALID_QUERY_COLUMNS:
            cursor.execute(f"""
            SELECT
                l.id,
                l.name,
                l.address
            FROM Location l
            WHERE l.{key} = ?
            """, ( value, ))

        results = cursor.fetchall()

        locations = [ (Location(**location)).__dict__ for location in results ]

        return locations

    def _create(self, cursor, location):
        cursor.execute("""
        INSERT INTO Location
            ( name, address )
        VALUES
            ( ?, ? )
        """, ( location['name'], location['address'] ))

        id = cursor.lastrowid
        location['id'] = id

        return location

    def _update(self, cursor, id, location):
        cursor.execute("""
        UPDATE Location
        SET
            name = ?,
            address = ?
        WHERE id = ?
        """, ( location['name'], location['address'], id ))

        rows_affected = cursor.rowcount

        return rows_affected != 0

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE FROM Location
        WHERE id = ?
        """, ( id, ))