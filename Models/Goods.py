from Models.Base import *

class Goods(Base):
    id = PrimaryKeyField()
    name = CharField()
    cost = DecimalField(6,2)
    quantity = IntegerField()
    description = TextField()

    class Meta:
        table_name = 'Goods'