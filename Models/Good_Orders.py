from Models.Base import *
from Models.Goods import Goods
from Models.Orders import Orders

class Good_Orders(Base):
    id = PrimaryKeyField()
    order_id = ForeignKeyField(Orders)
    good_id = ForeignKeyField(Goods)

    class Meta:
        table_name = 'Good_Orders'