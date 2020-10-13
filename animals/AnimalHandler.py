from helpers import BasicHandler
from models import Animal

class AnimalHandler(BasicHandler):
    _VALID_QUERY_COLUMNS = {
        "id": True,
        "name": True,
        "breed": True,
        "status": True,
        "customer_id": True,
        "location_id": True
    }

    def _get_all(self, cursor):
        cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        """)

        dataset = cursor.fetchall()

        animals = [ (Animal(**animal)).__dict__ for animal in dataset ]

        return animals

    def _get_by_id(self, cursor, id):
        cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        data = cursor.fetchone()

        animal = Animal(**data)

        return animal.__dict__

    def _get_by_criteria(self, cursor, key, value):
        if key in self._VALID_QUERY_COLUMNS:
            cursor.execute(f"""
            SELECT 
                a.id,
                a.name,
                a.breed,
                a.status,
                a.customer_id,
                a.location_id
            FROM animal a
            WHERE a.{key} = ?
            """, ( value, ))

            results = cursor.fetchall()

            animals = [ (Animal(**animal)).__dict__ for animal in results ]

            return animals

    def _update(self, cursor, id, animal):
        cursor.execute("""
        UPDATE Animal
        SET
            name = ?,
            breed = ?,
            status = ?,
            customer_id = ?,
            location_id = ?
        WHERE id = ?
        """, ( animal['name'], animal['breed'], animal['status'], 
                animal['customer_id'], animal['location_id'], id ))

        rows_affected = cursor.rowcount

        return rows_affected != 0

    def _delete(self, cursor, id):
        cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, ( id, ))