import sqlite3
import json

class BasicHandler:
    _VALID_QUERY_COLUMNS = {
        "id": True
    }

    def __exec_query(self, callback):
        with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            return callback(cursor)

    def get_all(self):
        result = self.__exec_query(lambda cursor: self._get_all(cursor))
        return json.dumps(result)

    def get_by_id(self, id):
        result = self.__exec_query(lambda cursor: self._get_by_criteria(cursor, 'id', id))

        if(len(result)):
            result = result.pop()
        else:
            result = None
        
        return json.dumps(result)

    def get_by_criteria(self, key, value):
        result = self.__exec_query(lambda cursor: self._get_by_criteria(cursor, key, value))
        return json.dumps(result)

    def create(self, obj):
        result = self.__exec_query(lambda cursor: self._create(cursor, obj))
        return json.dumps(result)

    def update(self, id, obj):
        result = self.__exec_query(lambda cursor: self._update(cursor, id, obj))
        if(result == False):
            return False
        return json.dumps(result)

    def delete(self, id):
        self.__exec_query(lambda cursor: self._delete(cursor, id))

    # derived classes need to implement the below functions if they want to 
    # implement the corresponding functionality
    def _get_all(self, cursor):
        pass

    def _get_by_criteria(self, cursor, key, value):
        pass

    def _create(self, cursor, obj):
        pass

    def _update(self, cursor, id, obj):
        pass

    def _delete(self, cursor, id):
        pass