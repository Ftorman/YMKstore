from Models.Goods import *

class OrderController:
    @classmethod
    def get(cls):
        return Goods.select()

    @classmethod
    def show(cls):
        return Goods.get_or_none(id)

    @classmethod
    def add(cls, name, cost, quantity, description):
        Goods.create(name = name,
                     cost = cost,
                     quantity = quantity,
                     description = description)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Goods.update({key: value}).where(Goods.id == id).execute()

    @classmethod
    def count_goods(cls):
        count = Goods.select().count()
        return count