import data_base as db
import mysql.connector
import datetime

def sql_test():
    produtos = db.select_query_where('hash','cliente','usuario = "{}"'.format('cesarwn'))
    print(produtos[0][0])
    for produto in produtos:
        print((produto))
    return

def datetime_test():
    a = (datetime.date.today())
    print(type(str(a)))


def sql_test2():
    produtos = db.columns_query('produto')
    print(produtos)
    for produto in produtos:
        print((produto))
    return

sql_test()


# 2020-07-31T14:33", 1700.0
# 2020-07-30
