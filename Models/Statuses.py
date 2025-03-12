from Models.Base import *

class Statuses(Base):
    id = PrimaryKeyField()
    status_name = CharField()

    class Meta:
        table_name = 'Statuses'