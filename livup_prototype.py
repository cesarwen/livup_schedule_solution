from flask import Flask, render_template, request, redirect, session, flash, url_for
import data_base as db
import secrets
import client
import comanda

app = Flask(__name__)
app.secret_key = secrets.key()

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

def atualiza_users():
    usuarios = client.query_clients()
    return(usuarios)

usuarios=(atualiza_users())

@app.route('/')
def index():
    return render_template('dashboard.html', titulo='Dashboard')

@app.route('/signup')
def signup():
    proxima = request.args.get('proxima')
    
    return render_template('signup.html', proxima=proxima)


@app.route('/novo_cliente', methods=['POST', ])
def novo_cliente():
    senha =  (str(request.form['senha']))
    usuario = str(request.form['usuario'])
    nome = str(request.form['nome'])
    endereco = str(request.form['endereco'])
    flash('Seja bem vindo {}'.format(nome))
    proxima_pagina = request.form['proxima']
    
    client.new_client(usuario, nome, senha, endereco)

    usuarios = atualiza_users()

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():

    senha = (str(request.form['senha']))

    for usuario in usuarios:
        if (usuario[1] == request.form['usuario'] and usuario[4] == senha):
            ok = 1
            session['usuario_logado'] = usuario[0]
            flash(usuario[1] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

    flash('Não logado, tente novamente!')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

@app.route('/agendamento')
def agendamento():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        return redirect(url_for('login', proxima=url_for('agendamento')))
    produtos = db.select_query('*', 'produto')
    return render_template('agendamento.html', titulo='Fazer Agendamento', produtos = produtos)

@app.route('/fazer_agendamento', methods=['POST', ])
def fazer_agendamento():

    id_usuario = session['usuario_logado']
    dia_agendamento = request.form['data_prevista']
    prato = request.form['prato']

    comanda.nova_comanda(id_usuario, dia_agendamento, [prato])

    flash('Agendamento realizado com sucesso')
    return redirect(url_for('index'))

app.run(debug=True)