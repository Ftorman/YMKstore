from itertools import count
from turtledemo.forest import start

from Models.Orders import *
import calendar
from datetime import datetime, timedelta

class OrderController:
    @classmethod
    def get(cls):
        return Orders.select()

    @classmethod
    def show(cls, id):
        return Orders.get_or_none(id)

    @classmethod
    def add(cls, date,  client_id, payment_id = None , delivery_data_id = 4, status_id = 1):
        if payment_id is not None:
            status_id = 6
        Orders.create(date = date,
                      payment_id = payment_id,
                      delivery_data_id = delivery_data_id,
                      client_id = client_id,
                      status_id = status_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Orders.update({key: value}).where(Orders.id == id).execute()

    @classmethod
    def delete(cls, *id):
            for orders in id:
                Orders.delete_by_id(orders)

    @classmethod
    def count(cls, date):
        count = Orders.select().where(Orders.date == date).count()
        return count

    @classmethod
    def get_orders_in_month(cls,start_date, end_date):
        start_date = datetime.strptime(start_date,'%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        count = Orders.select().where((Orders.date >= start_date) & (Orders.date <= end_date)).count()
        return count

    @classmethod
    def report_day(cls, day):
        return Orders.select().where(Orders.date == day).count()

    @classmethod
    def report_range(cls, day1, day2):
        return Orders.select().where(Orders.date.between(day1, day2)).count()



if __name__ == "__main__":
    # OrderController.add('2025-03-01','2','2025-03-09','3','1')
    # for row in OrderController.get():
    #     print(row.id, row.date, row.payment_id, row.delivery_data, row.client_id, row.status_id)

    # try:
        order_count = OrderController.get_orders_in_month('2025-02-01', '2025-02-28')
        print(order_count)
    # except ValueError as e:
    #     print(e)
    # OrderController.add('2025-03-05',2, payment_id=2)