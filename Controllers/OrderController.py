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
        Orders.create(date = date,
                      payment_id = payment_id,
                      delivery_data = delivery_data,
                      client_id = client_id,
                      status_id = status_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Orders.update({key: value}).where(Orders.id == id).execute()

    @classmethod
    def delete(cls, *id):
        for Orders in id:
            Orders.delete_by_id(Orders)

    @classmethod
    def count_goods(cls):
        count = Orders.select().count()

if __name__ == "__main__":
    for row in OrderController.get():
        print(row.id, row.name)
    print(OrderController.show(1).name)