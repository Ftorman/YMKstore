from Models.Base import *

class Orders(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    payment_id = BigIntegerField()
    delivery_data = CharField()
    client_id = IntegerField()
    status_id = IntegerField()