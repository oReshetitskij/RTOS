from random import randint

from modules.data.dao import TableDAO
from modules.data.entities import Client, Position
from modules.header import header


@header(title="get all test")
def get_all_test():
    clients = client_dao.get_all()
    for client in clients:
        print("%s|%s|%s" % (str(client.id).ljust(5), client.name.ljust(10), client.passport.ljust(10)))


@header(title="Single get test")
def get_test():
    client = client_dao.get(entity_id=1)
    print("%s|%s|%s" % (str(client.id).ljust(5), client.name.ljust(10), client.passport.ljust(10)))


@header(title="UPDATE test")
def update_test():
    client = client_dao.get(entity_id=1)
    client.passport = client.passport[:len(client.passport) - 1] + str(randint(0, 10))
    client_dao.update(client)
    client_updated = client_dao.get(entity_id=1)
    print("%s|%s" % (client.passport, client_updated.passport))


@header(title="ADD test")
def add_test():
    position = Position()
    position.name = "Receptionist"
    position.requirements = "Communication skills"
    position.responsibilities = "Client meeting"
    position.sallary = 5300
    position_dao.add(position)
    position_added = position_dao.get(position.id)
    print("%s|%s" % (position.name, position_added.name))


@header(title="WHERE test")
def where_test():
    clients = client_dao.where(Service1=4, Service2=5)
    for client in clients:
        print("%s|%s|%s|%s" % (client.name.ljust(10), client.passport.ljust(10), client.service1, client.service2))

if __name__ == '__main__':
    conn_string = "hotelDB.sqlite3"
    client_dao = TableDAO(conn_string, Client)
    position_dao = TableDAO(conn_string, Position)

    get_all_test()
    get_test()
    update_test()
    add_test()
    where_test()