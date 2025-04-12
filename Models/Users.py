
from Models.Base import *
from Models.Roles import Roles
from flask_login import UserMixin


class Users(UserMixin, Base):
    id = PrimaryKeyField()
    login = CharField(unique=True)
    password = CharField()
    role_id = ForeignKeyField(Roles)

if __name__ == "__main__":
    connect().create_tables([Users])