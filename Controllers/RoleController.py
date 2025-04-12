from Models.Roles import *

class RoleController:
    @classmethod
    def get(cls):
        return Roles.select()

    @classmethod
    def show(cls, id):
        return Roles.get_or_none(id)

if __name__ == "__main__":
    pass