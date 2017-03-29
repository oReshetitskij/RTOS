import sqlite3


class CollectionProvider:
    def __init__(self, conn_string, table, columns):
        self.__connection_string = conn_string
        self.__table = table
        self.__columns = columns

    def select_one(self, where):
        columns = ", ".join(self.__columns)
        query = "SELECT {} FROM {} WHERE {} LIMIT 1;".format(columns, self.__table, where)
        connection = sqlite3.connect(self.__connection_string)
        result = connection.execute(query).fetchone()
        connection.commit()
        connection.close()
        return result

    def select_many(self, where):
        columns = ", ".join(self.__columns)
        query = "SELECT {} FROM {} WHERE {}".format(columns, self.__table, where)
        connection = sqlite3.connect(self.__connection_string)
        result = connection.execute(query).fetchall()
        connection.commit()
        connection.close()
        return result

    def insert_one(self, values):
        columns = ", ".join(self.__columns[1:])
        values = ", ".join(values)
        query = "INSERT INTO {} ({}) VALUES ({});".format(self.__table, columns, values)
        connection = sqlite3.connect(self.__connection_string)
        connection.execute(query)
        connection.commit()
        connection.close()

    def update_one(self, record_id, values):
        set_clause = ", ".join(map(lambda x: "{}='{}'".format(x[0], x[1]), zip(self.__columns[1:], values)))

        query = "UPDATE {} SET {} WHERE id={};".format(self.__table, set_clause, record_id)
        connection = sqlite3.connect(self.__connection_string)
        connection.execute(query)
        connection.commit()
        connection.close()

    def delete_one(self, record_id):
        query = "DELETE FROM {} WHERE id={};".format(self.__table, record_id)
        connection = sqlite3.connect(self.__connection_string)
        connection.execute(query)
        connection.commit()
        connection.close()
