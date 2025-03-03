from peewee import *

# функция подключения к базе данных
def connect():
    mysql_db = MySQLDatabase(
        'AliA1234_ISIP22',
        user='AliA1234_ALALAL',
        password='1111111',
        host='10.11.13.118',
        port=3306)
    return mysql_db

if __name__ == "__main__":
    connect().connect()