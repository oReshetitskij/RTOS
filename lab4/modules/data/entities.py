class Client(object):
    def __init__(self):
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


class Employee(object):
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


class Position(object):
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


class Room(object):
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


class Service(object):
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
