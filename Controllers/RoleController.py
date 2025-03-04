from Models.Roles import *

class OrderController:
    @classmethod
    def get(cls):
        return Roles.select()

    @classmethod
    def show(cls):
        return Roles.get_or_none(id)

    @classmethod
    def add(cls, role_name):
        Roles.create(role_name = role_name)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Roles.update({key: value}).where(Roles.id == id).execute()

    @classmethod
    def count_goods(cls):
        count = Roles.select().count()
        return count