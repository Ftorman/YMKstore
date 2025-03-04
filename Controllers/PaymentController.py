from Models.Payments import *

class OrderController:
    @classmethod
    def get(cls):
        return Payments.select()

    @classmethod
    def show(cls):
        return Payments.get_or_none(id)

    @classmethod
    def add(cls, payment, date):
        Payments.create(payment = payment,
                        date = date)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Payments.update({key: value}).where(Payments.id == id).execute()

    @classmethod
    def count_goods(cls):
        count = Payments.select().count()
        return count