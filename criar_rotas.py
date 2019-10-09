from flask import Flask, render_template, request, url_for, session, redirect
# from classe import *
from bdballot import *

app = Flask("__name__")

app.config["SECRET_KEY"] = 'admin'

listaUE = []
listaUS = []

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/form_criar_votacao")
def form_criar_votacao():
    return render_template("criar_votacao.html")

@app.route("/atualizar_form_add_candidato")
def atualizar_form_criar_votacao():
    return render_template("adicionar_candidatos.html", ncandidatos = session['ncandidatos'])

@app.route("/criar_votacao", methods=['post'])
def criar_votacao():
    return render_template("eleicao.html")

@app.route("/form_add_candidato")
def add_candidato():
    session['ncandidatos'] = 2 
    return render_template("adicionar_candidatos.html", ncandidatos = session['ncandidatos'])

@app.route("/votar")
def votar():
    return render_template("votar.html")

@app.route("/ver_ranking")
def ver_ranking():
    return render_template("ver_ranking.html")

@app.route("/form_cadastrar")
def form_cadastrar():
    return render_template("cadastrar.html")

@app.route("/cadastrar", methods=['post'])
def cadastrar():
    nomeUsu = request.form["nome"]
    cpf = request.form["cpf"]
    emailUsu = request.form["email"]
    emailUsu = emailUsu.upper()
    senhaUsu = request.form["senha"]
    print(nomeUsu, cpf, emailUsu, senhaUsu)
    usu = Usuario.create(nomeU = nomeUsu, cpf = cpf, emailU = emailUsu, senha = senhaUsu)
    dado = Usuario.select()
    for i in dado:
        print(i.nomeU)
    return redirect("/")

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=['post'])
def login():
    email = request.form["email"].upper()
    senha = request.form["senha"]
    dado = Usuario.select()
    for i in dado:
        listaUE.append(i.emailU)
        listaUS.append(i.senha)

    if email in listaUE and senha in listaUS:
        session['usuario'] = email
        
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
    return redirect("/atualizar_form_add_candidato")

@app.route("/resetar")
def resetar():
    session['ncandidatos'] = 2
    return redirect("/atualizar_form_add_candidato")

@app.route("/voltar")
def voltar():
    return render_template("index.html")

app.run(debug=True, port=7500, host="0.0.0.0")