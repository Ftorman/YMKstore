from Models.Base import *
from Models.Payments import Payments
from Models.Statuses import Statuses
from Models.Users import Users

class Orders(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    payment_id = ForeignKeyField(Payments)
    delivery_data = CharField()
    client_id = ForeignKeyField(Users)
    status_id = ForeignKeyField(Statuses)

    class Meta:
        table_name = 'Orders'