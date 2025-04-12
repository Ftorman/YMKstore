from Models.Payments import *

class PaymentsController:
    @classmethod
    def get(cls):
        return Payments.select()

    @classmethod
    def show(cls, id):
        return Payments.get_or_none(id)

    @classmethod
    def add(cls, summ, date):
        Payments.create(summ = summ, date = date)

if __name__ == "__main__":
   pass