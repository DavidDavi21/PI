from flask import Flask, render_template, request, url_for, session, redirect
from classe import *
from bdballot import *
from random import randint

app = Flask("__name__")
app.config["SECRET_KEY"] = 'admin'
sessao = False
lista_votacoes = Votacao.select()
lista_usuarios = Usuario.select()
lista_candidatos = Candidato.select()

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
    nomeU = request.form['nome']
    cpf = request.form['cpf']
    emailU = request.form['email']
    senha = request.form['senha']
    Usuario.create(nomeU=nomeU, cpf=cpf, emailU=emailU, senha=senha)
    #Colocar alert informando que foi bem sucedido! E o verificador se os campos estiverem preenchidos!
    return redirect("/form_login")

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=['post'])
def login():
    global sessao
    emailU = ',1'
    senhadigitada = request.form['senha']
    emailUdigitado = request.form['email']

    for procura in lista_usuarios:
        if emailUdigitado == procura.emailU:
            emailU = procura.emailU
            senha = procura.senha
    
    if emailUdigitado == emailU and senha == senhadigitada:
        sessao_total = (emailU, senha)
        session['usuario'] = sessao_total
        sessao = True
        return render_template("index.html")
    else:
        #Colocar alert e voltar pra tela de login
        #Ainda tem erros com mais de  1 cadastro
        return redirect("/form_login")

@app.route("/logout")
def logout():
    global sessao
    sessao = False
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