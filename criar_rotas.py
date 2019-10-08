from flask import Flask, render_template, request, url_for, session, redirect
from classe import *
from bdballot import *
from random import randint

app = Flask("__name__")
app.config["SECRET_KEY"] = 'admin'
sessao = False
votacao = Votacao.select()

@app.route("/")
def home():
    global sessao
    if sessao == True:
        return render_template("index.html", usuario=sessao)
    else:
        return render_template("index1.html")

@app.route("/form_criar_votacao")
def form_criar_votacao():
    if sessao == True:
        session['ncandidatos'] = 2  
        return render_template("criar_votacao.html", ncandidatos = session['ncandidatos'], usuario=sessao)
    else:
        return redirect("/form_login")

@app.route("/atualizar_form_criar_votacao")
def atualizar_form_criar_votacao():
    return render_template("criar_votacao.html", ncandidatos = session['ncandidatos'])

@app.route("/criar_votacao", methods=['post'])
def criar_votacao():
    '''titulo = request.form['titulo']
    lista_candidatos = []
    for i in range(ncandidatos):
        lista_candidatos.append(i.)'''
    pass

@app.route("/votar")
def votar():
    global sessao
    return render_template("votar.html", usuario=sessao)

@app.route("/ver_ranking")
def ver_ranking():
    global sessao
    return render_template("ver_ranking.html", usuario=sessao)

@app.route("/form_cadastrar")
def form_cadastrar():
    return render_template("cadastrar.html")

@app.route("/cadastrar", methods=['post'])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    senha = request.form['senha']
    return redirect("/")

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=['post'])
def login():
    global sessao
    email = request.form["email"]
    senha = request.form["senha"]

    if email == "bla@gmail.com" and senha == "admin":
        session['usuario'] = email
        sessao = True
        
        return render_template("index.html")
    else:
        return "erro no login, tente novamente"

@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")

@app.route("/soma")
def soma():
    session['ncandidatos'] += 1
    return redirect("/atualizar_form_criar_votacao")

@app.route("/gerar_senha")
def gerarSenha():
    senha = []
    while range(senha) < 10:
        aleatorio = randint(36,165)
        algarismo = chr(aleatorio)
        senha.append(algarismo)
    return senha

@app.route("/pagina_votacao", methods=['POST'])
def paginaVotacao():
    global votacao
    if votacao.codigo_votacao == "uebs":
        return redirect("/")
    else:
        render_template("/login")

app.run(debug=True, port=7500, host="0.0.0.0")