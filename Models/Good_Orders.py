from Models.Base import *

class Good_Orders(Base):
    id = PrimaryKeyField()
    order_id = IntegerField()
    good_id = IntegerField()