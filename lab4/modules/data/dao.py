import sqlite3

from modules.stringcases import convert_to_snake_case


class TableDAO(object):
    def __init__(self, conn_string, entity_cls):
        self.__conn_string = conn_string
        self.__table = entity_cls.__name__ + "s"
        self.__entity_cls = entity_cls
        # check if table exists in database
        conn = sqlite3.connect(self.__conn_string)
        query = "SELECT * FROM sqlite_master WHERE name = ? and type = 'table'"
        if conn.execute(query, (self.__table,)).rowcount == 0:
            raise ValueError("Database don't contains given table")

        # get column names (works only for SQLite)
        query = "PRAGMA table_info('%s')" % self.__table
        res = conn.execute(query)
        self.__columns = [row[1] for row in res]
        conn.close()

    def create(self, **kwargs):
        obj = self.__entity_cls()
        try:
            [setattr(obj, convert_to_snake_case(k), v) for k, v in kwargs.items()]
        except AttributeError:
            raise AttributeError("Wrong column set")
        return obj

    def get(self, entity_id):
        conn = sqlite3.connect(self.__conn_string)
        query = "SELECT * FROM %s WHERE Id == ?" % self.__table
        res = conn.execute(query, (entity_id,)).fetchone()
        pairs = dict(zip(self.__columns, res))  # column/value binding
        conn.close()
        return self.create(**pairs)

    def get_all(self):
        conn = sqlite3.connect(self.__conn_string)
        query = "SELECT * FROM %s" % self.__table
        res = conn.execute(query).fetchall()
        entities = []
        for row in res:
            pairs = dict(zip(self.__columns, row))  # column/value binding
            obj = self.create(**pairs)
            entities.append(obj)
        conn.close()
        return entities

    def update(self, entity):
        update_values = []
        query = "UPDATE %s SET " % self.__table
        for col in self.__columns:
            col_value = getattr(entity, convert_to_snake_case(col))  # get column value for entity
            update_values.append(col_value)  # get column value for entity
            query += col + " = ? "
            # check if it is last column
            if col != self.__columns[len(self.__columns) - 1]:
                query += ","
        query += "WHERE Id = ?"
        update_values.append(entity.id)
        conn = sqlite3.connect(self.__conn_string)
        conn.execute(query, update_values)
        conn.commit()
        conn.close()

    def add(self, entity):
        conn = sqlite3.connect(self.__conn_string)
        query = "SELECT Id FROM %s ORDER BY Id DESC LIMIT 1" % self.__table
        row = conn.execute(query).fetchone()
        last_id = row[0]
        entity.id = last_id + 1
        col_values = []
        query = "INSERT INTO %s VALUES(" % self.__table
        for col in self.__columns:
            value = getattr(entity, convert_to_snake_case(col))  # get column value for entity
            col_values.append(value)
            query += "?"
            if col != self.__columns[len(self.__columns) - 1]:
                query += ","
        query += ")"
        conn = sqlite3.connect(self.__conn_string)
        conn.execute(query, col_values)
        conn.commit()
        conn.close()

    def delete(self, entity):
        query = "DELETE FROM %s WHERE " % self.__table
        delete_values = []
        for col in self.__columns:
            col_value = getattr(entity, col)()  # get column value for entity
            delete_values.append(col_value)  # get column value for entity
            query += col + " = ? "
            # check if it is last column
            if col == self.__columns[len(self.__columns) - 1]:
                query += ";"
            else:
                query += " AND "
        conn = sqlite3.connect(self.__conn_string)
        conn.execute(query, delete_values)
        conn.commit()
        conn.close()

    def where(self, **kwargs):
        query = "SELECT * FROM %s WHERE " % self.__table
        where_values = []
        for k, v in kwargs.items():
            query += k + " = ? AND "
            where_values.append(v)
        query = query[:len(query) - 5] + ";"
        conn = sqlite3.connect(self.__conn_string)
        res = conn.execute(query, where_values).fetchall()
        entities = []
        for row in res:
            pairs = dict(zip(self.__columns, row))  # column/value binding
            obj = self.create(**pairs)
            entities.append(obj)
        return entities