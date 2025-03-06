from Models.Roles import *

class RoleController:
    @classmethod
    def get(cls):
        return Roles.select()

    @classmethod
    def show(cls):
        return Roles.get_or_none(id)

if __name__ == "__main__":
    for row in RoleController.get():
        print(row.id, row.role_name)