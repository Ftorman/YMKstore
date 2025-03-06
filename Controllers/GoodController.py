from Models.Goods import *

class GoodController:
    @classmethod
    def get(cls):
        return Goods.select()

    @classmethod
    def show(cls):
        return Goods.get_or_none(id)

    @classmethod
    def add(cls, name, cost, quantity, description = ''):
        Goods.create(name = name,
                     cost = cost,
                     quantity = quantity,
                     description = description)

    @classmethod
    def delete(cls,id):
        Goods.delete_by_id(id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Goods.update({key:value}).where(Goods.id == id).execute()

    #Метод вывода количества товаров
    @classmethod
    def count(cls, id):
        try:
            return GoodController.show(id).quantity
        except Exception as error:
            print(f"Ошибка: {error}")
            return None

        #if Goods.get_or_none(id) is None:
        #    return None
        #else:
        #    return Goods.get_or_none(id).quantity


if __name__ == "__main__":
    #GoodController.add('Ноутбук', 100000, 5)
    #GoodController.update(21,20000)
    #GoodController.delete(2)
    #for row in GoodController.get():
    #    print(row.id, row.name, row.quantity, row.description)
    #print(GoodController.show(1).quantity)
    print(GoodController.count(1))