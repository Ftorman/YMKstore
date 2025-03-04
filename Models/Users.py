from Models.Base import *

class Statuses(Base):
    id = PrimaryKeyField()
    login = CharField()
    password = CharField()
    role_id = CharField()