from models import Location
from helpers import BasicHandler

class LocationHandler(BasicHandler):
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

    def _get_by_id(self, cursor, id):
        cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        WHERE l.id = ?
        """, ( id, ))

        result = cursor.fetchone()

        location = Location(**result)

        return location.__dict__

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE FROM Location
        WHERE id = ?
        """, ( id, ))