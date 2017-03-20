from active_records.entities import *
from storage.collectionProvider import CollectionProvider

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

    Client.set_provider(
        CollectionProvider(dbname, "Clients", [
            "Id",
            "Name",
            "Passport",
            "CheckInDate",
            "CheckOutDate",
            "RoomId",
            "Service1",
            "Service2",
            "Service3",
            "Price",
            "EmployeeId"
        ])
    )

    print("loading employee:")
    employee = Employee()
    employee.load_one("id = 1")
    print(employee.__dict__)

    print("saving employee:")
    employee.name = "changed name"
    employee.save()

    print("checking if saved:")
    another_employee = Employee()
    another_employee.load("id = 1")
    print(employee.__dict__)

    employees = Employee.load("sex = 1")
    print(len(employees))
    print([el.__dict__ for el in employees])

