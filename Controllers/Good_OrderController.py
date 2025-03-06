from Models.Good_Orders import Good_Orders
from Models.Goods import *


class GoodOrderController:
    @classmethod
    def get(cls):
        return Good_Orders.select()

    @classmethod
    def show(cls):
        return Good_Orders.get_or_none(id)

    @classmethod
    def add(cls, order_id, good_id):
        Good_Orders.create(order_id=order_id,good_id=good_id)

    @classmethod
    def delete(cls, id):
        Good_Orders.delete_by_id(id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Goods.update({key: value}).where(Goods.id == id).execute()

    # Метод вывода количества товаров
    @classmethod
    def count(cls, id):
        try:
            return GoodOrderController.show(id).quantity
        except Exception as error:
            print(f"Ошибка: {error}")
            return None

            # if Goods.get_or_none(id) is None:
        #    return None
        # else:
        #    return Goods.get_or_none(id).quantity


if __name__ == "__main__":
    # GoodController.add('Ноутбук', 100000, 5)
    # GoodController.update(21,20000)
    # GoodController.delete(2)
    # for row in GoodController.get():
    #    print(row.id, row.name, row.quantity, row.description)
    # print(GoodController.show(1).quantity)
    #print(GoodController.count(1))

    pass