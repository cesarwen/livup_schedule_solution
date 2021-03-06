from flask import Flask, render_template, request, redirect, session, flash, url_for
import data_base as db
import secrets
import client
import comanda

app = Flask(__name__)
app.secret_key = secrets.key()


def atualiza_users():
    usuarios = client.query_clients()
    return(usuarios)


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

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():

    usuarios = atualiza_users()
    user = db.select_query_where('hash, id_cliente, nome','cliente','usuario = "{}"'.format(request.form['usuario']))[0]
    senha = (str(request.form['senha']))

    if (user != None):
        if (user[0] == senha):
            session['usuario_logado'] = user[1]
            flash(user[2] + ' logou com sucesso!')
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
    return render_template('agendamento.html', titulo = 'Fazer Agendamento', produtos = produtos)


@app.route('/fazer_agendamento', methods=['POST', ])
def fazer_agendamento():

    id_usuario = session['usuario_logado']
    dia_agendamento = request.form['data_prevista']
    prato = request.form['prato']

    comanda.nova_comanda(id_usuario, dia_agendamento, [prato])

    flash('Agendamento realizado com sucesso')
    return redirect(url_for('index'))


@app.route('/db_show')
def db_show():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        return redirect(url_for('login', proxima=url_for('db_show')))
    tables = db.show_query()
    return render_template('db_show.html', titulo = 'Ver Banco de Dados', tables = tables)


@app.route('/select_db', methods=['POST', ])
def select_db():
    session['db'] = request.form['db']
    return redirect(url_for('view_db'))

@app.route('/view_db')
def view_db():
    headers = db.columns_query(session['db'])
    contents = db.select_query('*', session['db'])
    return render_template('view_db.html', titulo = session['db'], headers = headers, contents = contents)

app.run(debug=True)