from Models.Users import *
from bcrypt import hashpw, gensalt, checkpw

class UserController:
    @classmethod
    def get(cls):
        return Users.select()

    @classmethod
    def show(cls):
        return Users.get_or_none(id)

    @classmethod
    def registration(cls, login, password, role_id):
        hash_password = hashpw(password.encode('utf-8'),gensalt())
        Users.create(login = login,
                     password = password,
                     role_id = role_id)

    def login(cls, login, password):
        if Users.get_or_none(Users.login == login)  != None:
            hspassword = Users.get_or_none(Users.login == login).password

            if checkpw(password.encode('utf-8'),hspassword.encode('utf-8')):
                return True
        return False

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Users.update({key: value}).where(Users.id == id).execute()

    @classmethod
    def delete(cls, *id):
        for good_orders in id:
            Users.delete_by_id(good_orders)

if __name__ == "__main__":
    #UserController.registration('Ivan_2023', 'ivan1', '1')
    #UserController.registration('Ivan_2023', 'ivan1', '2')
    #UserController.registration('mARIA_666', 'ivan1', '3')
    #UserController.registration('Josh', 'ivan1', '4')
    #UserController.registration('Sigma', 'ivan1', '5')
    #for row in UserController.get():
    #   print(row.id, row.login, row.password, row.role_id)
    print(UserController.login('Ivan_2023', 'ivan1'))