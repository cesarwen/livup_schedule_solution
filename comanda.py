import data_base as db
import ETA
import datetime

# Funcoes responsaveis pela logica de manipulacao e envio de informacoes referentes a criacao
# dos dados a serem salvos nos bancos de dados

def novo_pedido(qtde, produto, comanda, restaurante):
    # cria um novo pedido a ser salvo no banco de dados
    # qtde [int] - quantidade
    # produto [int] - id do produto
    # comanda [int] - id da comanda
    # restaurante [int] - id restaurante

    # retorna o id do pedido realizado

    id_pedido = db.max_select('id_pedido', 'pedido') 
    if (id_pedido == None):
        id_pedido = 1
    else:
        id_pedido += 1
    into = 'pedido (id_pedido, id_produto, quantidade, id_comanda, id_restaurante)'
    values = '{}, {}, {}, {}, {}'.format(id_pedido, produto, qtde, comanda, restaurante)
    db.insert_query(into, values)
    return(id_pedido)

def novo_agendamento(id_pedido, agendamento, ETA):
    # cria um novo agendamento a ser salvo no banco de dados
    # id_pedido [int] - id do pedido relacionado ao agendamento
    # agendamento [string] - instante e diapara o qual o pedido foi agendado
    # (formato yyyy-mm-ddThh-mm-ss)
    # ETA [int] - tempo estimado da duracao da viagem

    today = str(datetime.date.today())

    periferico = 0
    print("agendamento = {} \n[0:9] = {} \ntoday = {}\ncond = {}".format(agendamento, str(agendamento[0:10]), today,today == agendamento[0:10]))
    if (today == agendamento[0:10]):
        periferico = 1

    into = 'agendamento (id_pedido, horario_agendado, tempo_estimado, imediato)'
    values = '{}, "{}", {}, {}'.format(id_pedido, agendamento, round(ETA/60 +1,0)*100, periferico)
    print("My values are: {}".format(values))
    db.insert_query(into,values)
    return

def nova_comanda(cliente, agendamento, produtos):
    # cria uma nova comanda a ser salva no banco de dados
    # cliente [int] - id do cliente relacionado a comanda
    # agendamento [string] - instante e diapara o qual o pedido foi agendado (enviado para a funcao de agendamento)
    # (formato yyyy-mm-ddThh-mm-ss)
    # produtos list[int] - lista de produtos a requeridos pelo cliente

    comanda = db.max_select('id_comanda', 'comanda')

    if (comanda == None):
        comanda = 1

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