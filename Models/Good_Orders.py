from Models.Base import *
from Models.Goods import Goods
from Models.Orders import Orders


class Good_Orders(Base):
    id = PrimaryKeyField()
    order_id = ForeignKeyField(Orders)
    good_id = ForeignKeyField(Goods)

if __name__ == "__main__":
    connect().create_tables([Good_Orders])