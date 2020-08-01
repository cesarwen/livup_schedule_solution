import data_base as db
# import hasher as h

def new_client(usuario, name, password, endereco):
    into = 'cliente(usuario, nome, hash, endereco)'
    values = '"{}", "{}","{}","{}"'.format(usuario, name, password, endereco)
    db.insert_query(into,values)

def query_clients():
    query_result = db.select_query('*','cliente')
    return(query_result)

#new_client('Cesar Wen', '1234', 'Verbo Divino 1061')