import data_base as db
import mysql.connector

produtos = db.select_query('cliente')

for produto in produtos:
    print(len(produto))