from Models.Base import *

class Goods(Base):
    id = PrimaryKeyField()
    name = CharField()
    cost = DecimalField(8,2)
    quantity = IntegerField()
    description = TextField()

if __name__ == "__main__":
    connect().create_tables([Goods])