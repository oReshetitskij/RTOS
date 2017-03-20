from abc import ABC, abstractmethod


class ActiveRecordBase(ABC):
    @staticmethod
    @abstractmethod
    def set_provider(provider):
        """
        set db provider
        """

    @abstractmethod
    def load_one(self, where):
        """
        load first record from db
        and assign to self
        """

    @staticmethod
    @abstractmethod
    def load(where):
        """
        load multiple records
        and return list of entities
        """

    @abstractmethod
    def save(self):
        """
        create in db if not exists,
        otherwise update
        """

    @abstractmethod
    def delete(self):
        """
        delete from db
        """


class Client(ActiveRecordBase):
    __provider = None

    def __init__(self):
        if Client.__provider is None:
            raise Exception("db provider is not set")

        self.__id = None
        self.__name = None
        self.__passport = None
        self.__check_in_date = None
        self.__check_out_date = None
        self.__room_id = None
        self.__service1 = None
        self.__service2 = None
        self.__service3 = None
        self.__price = None
        self.__employee_id = None

    # region props
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        self.__passport = value

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self.__check_in_date = value

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self.__check_out_date = value

    @property
    def room_id(self):
        return self.__room_id

    @room_id.setter
    def room_id(self, value):
        self.__room_id = value

    @property
    def service1(self):
        return self.__service1

    @service1.setter
    def service1(self, value):
        self.__service1 = value

    @property
    def service2(self):
        return self.__service2

    @service2.setter
    def service2(self, value):
        self.__service2 = value

    @property
    def service3(self):
        return self.__service3

    @service3.setter
    def service3(self, value):
        self.__service3 = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        self.__employee_id = value
    # endregion

    def save(self):
        if self.__id is None:
            self.__create()
        else:
            self.__update()

    @staticmethod
    def set_provider(provider):
        Client.__provider = provider

    @staticmethod
    def load(where):
        def set_fields(arr):
            rec = Client()
            rec.id = arr[0]
            rec.name = arr[1]
            rec.passport = arr[2]
            rec.check_in_date = arr[3]
            rec.check_out_date = arr[4]
            rec.room_id = arr[5]
            rec.service1 = arr[6]
            rec.service2 = arr[7]
            rec.service3 = arr[8]
            rec.price = arr[9]
            rec.employee_id = arr[10]
            return rec
        return list(map(
            set_fields,
            Client.__provider.select_many(where),
        ))

    def delete(self):
        self.__class__.__provider.delete_one(self.id)

    def load_one(self, where=""):
        arr = self.__class__.__provider.select_one(where)
        self.id = arr[0]
        self.name = arr[1]
        self.passport = arr[2]
        self.check_in_date = arr[3]
        self.check_out_date = arr[4]
        self.room_id = arr[5]
        self.service1 = arr[6]
        self.service2 = arr[7]
        self.service3 = arr[8]
        self.price = arr[9]
        self.employee_id = arr[10]

    def __update(self):
        self.__class__.__provider.update_one(self.id, [
            self.name,
            self.passport,
            self.check_in_date,
            self.check_out_date,
            self.room_id,
            self.service1,
            self.service2,
            self.service3,
            self.price,
            self.employee_id
        ])

    def __create(self):
        self.__class__.__provider.insert_one([
            self.id,
            self.name,
            self.passport,
            self.check_in_date,
            self.check_out_date,
            self.room_id,
            self.service1,
            self.service2,
            self.service3,
            self.price,
            self.employee_id
        ])


class Employee(ActiveRecordBase):
    __provider = None

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__age = None
        self.__sex = None
        self.__address = None
        self.__passport = None
        self.__position_id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        self.__sex = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        self.__passport = value

    @property
    def position_id(self):
        return self.__position_id

    @position_id.setter
    def position_id(self, value):
        self.__position_id = value

    def save(self):
        if self.__id is None:
            self.__create()
        else:
            self.__update()

    @staticmethod
    def set_provider(provider):
        Employee.__provider = provider

    @staticmethod
    def load(where):
        def set_fields(arr):
            rec = Employee()
            rec.id = arr[0]
            rec.name = arr[1]
            rec.age = arr[2]
            rec.sex = arr[3]
            rec.address = arr[4]
            rec.passport = arr[5]
            rec.position_id = arr[6]
            return rec
        return list(map(
            set_fields,
            Employee.__provider.select_many(where),
        ))

    def delete(self):
        self.__class__.__provider.delete_one(self.id)

    def load_one(self, where):
        arr = self.__class__.__provider.select_one(where)
        self.id = arr[0]
        self.name = arr[1]
        self.age = arr[2]
        self.sex = arr[3]
        self.address = arr[4]
        self.passport = arr[5]
        self.position_id = arr[6]

    def __update(self):
        self.__class__.__provider.update_one(self.id, [
            self.name,
            self.age,
            self.sex,
            self.address,
            self.passport,
            self.position_id
        ])

    def __create(self):
        self.__class__.__provider.insert_one([
            self.id,
            self.name,
            self.age,
            self.sex,
            self.address,
            self.passport,
            self.position_id
        ])


class Position(ActiveRecordBase):
    __provider = None

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__sallary = None
        self.__responsibilities = None
        self.__requirements = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def sallary(self):
        return self.__sallary

    @sallary.setter
    def sallary(self, value):
        self.__sallary = value

    @property
    def responsibilities(self):
        return self.__responsibilities

    @responsibilities.setter
    def responsibilities(self, value):
        self.__responsibilities = value

    @property
    def requirements(self):
        return self.__requirements

    @requirements.setter
    def requirements(self, value):
        self.__requirements = value

    def save(self):
        if self.__id is None:
            self.__create()
        else:
            self.__update()

    @staticmethod
    def set_provider(provider):
        Position.__provider = provider

    @staticmethod
    def load(where):
        def set_fields(arr):
            rec = Position()
            rec.id = arr[0]
            rec.name = arr[1]
            rec.sallary = arr[2]
            rec.responsibilities = arr[3]
            rec.requirements = arr[4]
            return rec
        return list(map(
            set_fields,
            Position.__provider.select_many(where),
        ))

    def delete(self):
        self.__class__.__provider.delete_one(self.id)

    def load_one(self, where=""):
        if where == "":
            where = "id = {}".format(self.id)
        self.__class__.__provider.select_one(where)

    def __update(self):
        self.__class__.__provider.update_one(self.id, [
            self.name,
            self.sallary,
            self.responsibilities,
            self.requirements,
        ])

    def __create(self):
        self.__class__.__provider.insert_one([
            self.id,
            self.name,
            self.sallary,
            self.responsibilities,
            self.requirements,
        ])


class Room(ActiveRecordBase):
    __provider = None

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__capacity = None
        self.__description = None
        self.__price = None
        self.__employee_id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        self.__employee_id = value

    def save(self):
        if self.__id is None:
            self.__create()
        else:
            self.__update()

    @staticmethod
    def set_provider(provider):
        Room.__provider = provider

    @staticmethod
    def load(where):
        def set_fields(arr):
            rec = Room()
            rec.id = arr[0]
            rec.name = arr[1]
            rec.capacity = arr[2]
            rec.description = arr[3]
            rec.price = arr[4]
            rec.employee_id = arr[5]
            return rec
        return list(map(
            set_fields,
            Room.__provider.select_many(where),
        ))

    def delete(self):
        self.__class__.__provider.delete_one(self.id)

    def load_one(self, where=""):
        if where == "":
            where = "id = {}".format(self.id)
        self.__class__.__provider.select_one(where)

    def __update(self):
        self.__class__.__provider.update_one(self.id, [
            self.name,
            self.capacity,
            self.description,
            self.price,
            self.employee_id,
        ])

    def __create(self):
        self.__class__.__provider.insert_one([
            self.id,
            self.name,
            self.capacity,
            self.description,
            self.price,
            self.employee_id,
        ])


class Service(ActiveRecordBase):
    __provider = None

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__description = None
        self.__price = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def save(self):
        if self.__id is None:
            self.__create()
        else:
            self.__update()

    @staticmethod
    def set_provider(provider):
        Service.__provider = provider

    @staticmethod
    def load(where):
        def set_fields(arr):
            rec = Service()
            rec.id = arr[0]
            rec.name = arr[1]
            rec.description = arr[2]
            rec.price = arr[3]
            return rec
        return list(map(
            set_fields,
            Service.__provider.select_many(where),
        ))

    def delete(self):
        self.__class__.__provider.delete_one(self.id)

    def load_one(self, where=""):
        if where == "":
            where = "id = {}".format(self.id)

        self.__class__.__provider.select_one(where)

    def __update(self):
        self.__class__.__provider.update_one(self.id, [
            self.name,
            self.description,
            self.price
        ])

    def __create(self):
        self.__class__.__provider.insert_one([
            self.id,
            self.name,
            self.description,
            self.price
        ])
