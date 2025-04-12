from Models.Statuses import *

class StatusController:
    @classmethod
    def get(cls):
        return Statuses.select()

    @classmethod
    def show(cls, id):
        return Statuses.get_or_none(id)

if __name__ == "__main__":
    pass