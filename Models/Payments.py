from Models.Base import *

class Payments(Base):
        id = PrimaryKeyField()
        summ = FloatField()
        date = DateTimeField()

if __name__ == "__main__":
    connect().create_tables([Payments])