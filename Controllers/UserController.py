from Models.Users import *

class OrderController:
    @classmethod
    def get(cls):
        return Users.select()

    @classmethod
    def show(cls):
        return Users.get_or_none(id)

    @classmethod
    def add(cls, login, password, role_id):
        Users.create(login = login,
                     password = password,
                     role_id = role_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Users.update({key: value}).where(Users.id == id).execute()

    @classmethod
    def delete(cls, *id):
        for Orders in id:
            Orders.delete_by_id(Orders)

    @classmethod
    def count_goods(cls):
        count = Users.select().count()
        return count