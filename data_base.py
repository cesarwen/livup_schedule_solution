import mysql.connector
import db_credentials as cred

def max_select(coluna, tabela):
    m = select_query('max({})'.format(coluna), tabela)[0][0]
    return (m)

def select_query(what, table):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("select {} from {}".format(what,table))

    cursor.execute(query)
    
    disconnect(cnx)

    output = []
    for c in cursor:
        output.append(c)

    return(output)

def select_query_where(what, table, where):
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT {} FROM {} WHERE {}".format(what, table, where))
    cursor.execute(query)
    
    disconnect(cnx)

    output = []
    for c in cursor:
        output.append(c)

    return(output)


def insert_query(into, values):
       
    cnx = connect()
    cursor = cnx.cursor()

    query = ("INSERT INTO {} VALUES ({})".format(into,values))

    cursor.execute(query)
    cnx.commit()
    disconnect(cnx)
    return


def show_query():
       
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SHOW TABLES")

    cursor.execute(query)

    cnx.close()    

    output = []
    for c in cursor:
        output.append(c[0])

    disconnect(cnx)
    return(output)

def columns_query(table):
       
    cnx = connect()
    cursor = cnx.cursor()

    query = ("SHOW COLUMNS FROM {}".format(table))

    cursor.execute(query)

    cnx.close()    

    output = []
    for c in cursor:
        output.append(c[0])

    disconnect(cnx)
    return(output)

def connect():
    cnx = mysql.connector.connect(user=cred.user(), password=cred.password(),host=cred.host(),database=cred.db())
    return(cnx)

def disconnect(cnx):
    cnx.close()
    return