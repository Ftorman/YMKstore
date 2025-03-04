from Models.Base import *

class Users(Base):
    id = PrimaryKeyField()
    login = DateTimeField()
    password = BigIntegerField()
    role_id = IntegerField()