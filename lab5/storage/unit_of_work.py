from enum import Enum


class State(Enum):
    NEW = 0
    CLEAN = 1
    DIRTY = 2
    DELETED = 3


class UnitOfWork(object):
    def __init__(self):
        # instance -> state
        self.__pool = {}

    def register_new(self, instance):
        self.__pool[instance] = State.NEW

    def register_clean(self, instance):
        self.__pool[instance] = State.CLEAN

    def register_dirty(self, instance):
        self.__pool[instance] = State.DIRTY

    def register_deleted(self, instance):
        self.__pool[instance] = State.DELETED

    def commit(self):
        for instance in self.__pool:
            state = self.__pool[instance]
            if state is State.NEW or state is State.DIRTY:
                print("saving instance #", instance.id)
                instance.save()
                continue
            if state is State.DELETED:
                print("deleting instance #", instance.id)
                instance.delete()
                continue
