from Models.Base import *
from Models.Payments import Payments
from Models.Statuses import Statuses
from Models.Users import Users


class Orders(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    payment_id = ForeignKeyField(Payments)
    delivery_data_id = DateTimeField(Statuses)
    client_id = ForeignKeyField(Users)
    status_id = ForeignKeyField(Statuses)

if __name__ == "__main__":
    connect().create_tables([Orders])