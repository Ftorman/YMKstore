from Models.Base import *

class Payments(Base):
    id = PrimaryKeyField()
    payment = DecimalField()
    date = DateTimeField()

    class Meta:
        table_name = 'Payments'