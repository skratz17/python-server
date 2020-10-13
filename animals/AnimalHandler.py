from helpers import BasicHandler
from models import Animal, Location, Customer

class AnimalHandler(BasicHandler):
    _VALID_QUERY_COLUMNS = {
        "id": True,
        "name": True,
        "breed": True,
        "status": True,
        "customer_id": True,
        "location_id": True
    }

    # given a row from a dataset that included a JOIN on location, return the fully expanded animal
    # object with the location object embedded in the animal
    def __build_expanded_animal_from_row(self, row):
        animal = Animal(row['id'], row['name'], row['breed'],
                    row['location_id'], row['customer_id'], row['status'])
        
        location = Location(row['location_id'], row['location_name'], row['location_address'])

        customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'],
                    row['customer_email'])

        animal.location = location.__dict__
        animal.customer = customer.__dict__

        return animal.__dict__

    def _get_all(self, cursor):
        cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email
        FROM animal a
        JOIN location l
            ON l.id = a.location_id
        JOIN customer c
            ON c.id = a.customer_id
        """)

        dataset = cursor.fetchall()

        animals = [ self.__build_expanded_animal_from_row(row) for row in dataset ]

        return animals

    def _get_by_id(self, cursor, id):
        cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email
        FROM animal a
        JOIN location l
            ON l.id = a.location_id
        JOIN customer c
            ON c.id = a.customer_id
        WHERE a.id = ?
        """, ( id, ))

        data = cursor.fetchone()

        animal = self.__build_expanded_animal_from_row(data)

        return animal

    def _get_by_criteria(self, cursor, key, value):
        if key in self._VALID_QUERY_COLUMNS:
            cursor.execute(f"""
            SELECT 
                a.id,
                a.name,
                a.breed,
                a.status,
                a.customer_id,
                a.location_id,
                l.name location_name,
                l.address location_address,
                c.name customer_name,
                c.address customer_address,
                c.email customer_email
            FROM animal a
            JOIN location l
                ON l.id = a.location_id
            JOIN customer c
                ON c.id = a.customer_id
            WHERE a.{key} = ?
            """, ( value, ))

            results = cursor.fetchall()

            animals = [ self.__build_expanded_animal_from_row(row) for row in results ]

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