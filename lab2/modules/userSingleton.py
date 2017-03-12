import sqlite3

class Employee(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Employee, cls).__new__(cls)
            connection = sqlite3.connect('hotelDB.sqlite3')
            name_query = 'SELECT Name FROM Employees LIMIT 1'
            passport_query = 'SELECT Passport FROM Employees LIMIT 1'
            cls.name = connection.execute(name_query).fetchone()
            cls.passport = connection.execute(passport_query).fetchone()
            connection.close()  # закриваємо з'єднання
        return cls