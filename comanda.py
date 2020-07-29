import data_base as db
import ETA

def novo_pedido(qtde, produto, comanda, restaurante):
    id_pedido = db.max_select('id_pedido', 'pedido') 
    if (id_pedido == None):
        id_pedido = 1
    else:
        id_pedido += 1
    into = 'pedido (id_pedido, id_produto, quantidade, id_comanda)'
    values = '{}, {}, {}, {}'.format(id_pedido, produto, qtde, comanda)
    db.insert_query(into, values)
    return(id_pedido)

def novo_agendamento(id_pedido, agendamento, ETA):
    into = 'agendamento (id_pedido, horario_agendado, tempo_estimado)'
    values = '{}, "{}", {}'.format(id_pedido, agendamento, ETA/60)
    db.insert_query(into,values)
    return

def nova_comanda(cliente, agendamento, produtos):
    comanda = db.max_select('id_comanda', 'comanda')

    valor = 0
    for produto in produtos:

        origin = db.select_query_where('endereco', 'cliente', 'id_cliente = {}'.format(cliente))[0][0]
        destination = db.select_query_where('endereco', 'restaurante', 'id_restaurante = {}'.format('1'))[0][0]

        estimate = ETA.ETA(origin, destination)

        id_pedido = novo_pedido(1, produto, comanda, 1)
        novo_agendamento(id_pedido, agendamento, estimate)

        valor_produto = db.select_query_where('preco', 'produto', 'id_produto = {}'.format(produto))
        print(valor_produto)
        valor_produto = float(valor_produto[0][0])

        valor = valor + valor_produto

    into = 'comanda(id_cliente, valor)'
    values = '{}, {}'.format(cliente, valor)
    db.insert_query(into, values)