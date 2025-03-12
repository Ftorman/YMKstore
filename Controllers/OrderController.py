from Models.Orders import *

class OrderController:
    @classmethod
    def get(cls):
        return Orders.select()

    @classmethod
    def show(cls):
        return Orders.get_or_none(id)

    @classmethod
    def add(cls, date, payment_id, delivery_data, client_id, status_id):
        if payment_id is not None:
            status_id = 6
        Orders.create(date = date, payment_id = payment_id, delivery_data = delivery_data, client_id = 5, status_id = 3)

    @classmethod
    def delete(cls, *id):
            Orders.delete_by_id(Orders)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Orders.update({key: value}).where(Orders.id == id).execute()


if __name__ == "__main__":
    OrderController.add('2025-02-02', 1, 'В пути', 9, 5)