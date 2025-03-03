from Models.Stasuses import *

class StasusController:
    # метод вывода всех записей таблицы Статусы
    @classmethod
    def get(cls):
        return Statuses.select()
    # Метод вывода одной записи
    @classmethod
    def show(cls, id):
        return Statuses.get_or_none(id)

if __name__ == "__main__":
    for row in StasusController.get():
        print(row.id, row.stasus_name)
    print(StasusController.show(11))