from Models.Users import *
import bcrypt

class UserController:
    @classmethod
    def get(cls):
        return Users.select()

    @classmethod
    def show(cls, id):
        return Users.get_or_none(id)

    @classmethod
    def show_login(cls,login):
        return Users.get_or_none(Users.login==login)


    @classmethod
    def registration(cls,login,password):
        try:
            password = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt())
            Users.create(login=login,password=password,role_id=3)
        except Exception as error:
            print(error)

    @classmethod
    def auth(cls,login,password):
        try:
            user = Users.get_or_none(Users.login == login)
            if user is None:
                return False
            if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
                return True
            else:
                return False
        except Exception as error:
            print(error)


    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Users.update({key: value}).where(Users.id == id).execute()

    @classmethod
    def delete(cls, *id):
            for good_orders in id:
                Users.delete_by_id(good_orders)


if __name__ == "__main__":
    UserController.registration('lEnA', '123456')

    # for row in UserController.get():
    #     print(row.id, row.login, row.password, row.role_id)
    # print(UserController.login('Ivan_2023', 'ivan'))
