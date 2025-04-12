from Models.Goods import *

class GoodController:
    @classmethod
    def get(cls):
        return Goods.select()

    @classmethod
    def show(cls, id):
        return Goods.get_or_none(id)

    @classmethod
    def add(cls, name, cost, quantity, description):
        Goods.create(name = name, cost = cost, quantity = quantity, description = description)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Goods.update({key: value}).where(Goods.id == id).execute()

    @classmethod
    def delete(cls, *id):
            for goods in id:
                Goods.delete_by_id(goods)

    # @classmethod
    # def count_goods(cls):
    #     count = Goods.select().count()
    #     return count

    @classmethod
    def count(cls, id):
        try:
            return GoodController.show(id).quantity
        except Exception as error:
            print(f"Ошибка: {error}")
            return None

if __name__ == "__main__":
    print(GoodController.count(12))