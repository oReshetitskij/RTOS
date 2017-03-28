from active_records.entities import *
from storage.collectionProvider import CollectionProvider
from storage.unit_of_work import UnitOfWork
from copy import deepcopy

dbname = 'hotelDB.sqlite3'

if __name__ == '__main__':
    Employee.set_provider(
        CollectionProvider(dbname, "Employees", [
            "Id",
            "Name",
            "Age",
            "Sex",
            "Address",
            "Passport",
            "PositionId"]))

    uow = UnitOfWork()

    employee1 = Employee()
    employee2 = Employee()
    employee3 = Employee()
    employee1.load_one("id = 1")
    employee2.load_one("id = 2")
    employee3.load_one("id = 3")

    uow.register_clean(employee1)
    uow.register_clean(employee2)
    uow.register_clean(employee3)

    print("before transaction:")
    print("employee 1: ", employee1.passport)
    print("employee 2: ", employee2.passport)
    print("employee 3: ", employee3.passport)

    employee1.passport, employee2.passport = \
        employee2.passport, employee1.passport

    uow.register_dirty(employee1)
    uow.register_dirty(employee2)

    uow.commit()

    updatedEmployees = Employee.load("id = 1 or id = 2 or id = 3")

    print("after transaction:")
    print("employee 1: ", updatedEmployees[0].passport)
    print("employee 2: ", updatedEmployees[1].passport)
    print("employee 3: ", updatedEmployees[2].passport)

