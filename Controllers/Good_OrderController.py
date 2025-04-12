from Models.Good_Orders import *

class Good_OrderController:
    @classmethod
    def get(cls):
        return Good_Orders.select()

    @classmethod
    def show(cls, id):
        return Good_Orders.get_or_none(id)

    @classmethod
    def add(cls, order_id, good_id):
        Good_Orders.create(order_id = order_id, good_id = good_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Good_Orders.update({key: value}).where(Good_Orders.id == id).execute()

    @classmethod
    def delete(cls, *id):
            for good_orders in id:
                Good_Orders.delete_by_id(good_orders)

    @classmethod
    def count_goods(cls):
        count = Good_Orders.select().count()


if __name__ == "__main__":
    pass