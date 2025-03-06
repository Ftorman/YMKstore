from datetime import datetime

from Models.Payments import *

class PaymentController:
    @classmethod
    def get(cls):
        return Payments.select()

    @classmethod
    def show(cls):
        return Payments.get_or_none(id)

    @classmethod
    def add(cls, payment, date = datetime.now()):
        Payments.create(payment = payment,
                        date = date)

if __name__ == "__main__":
    PaymentController.add(1662.25)
    for row in PaymentController.get():
        print(row.id, row.payment, row.date)