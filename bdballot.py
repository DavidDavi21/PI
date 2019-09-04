from peewee import CharField, FloatField, IntegerField, BigBitField, ForeignKeyField, SqliteDatabase, Model
import os

arq = "ballot.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    nomeU = CharField()
    cpf = CharField()
    emailU = CharField()
    senha = CharField()

class Votacao(BaseModel):
    titulo = CharField()
    criador = ForeignKeyField(Usuario)
    estiloVotacao = CharField()

class Candidato(BaseModel):
    nomeC = CharField()
    foto = BigBitField(null=False)
    descricao = CharField()
    votacao = ForeignKeyField(Votacao)

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Usuario, Candidato, Votacao])
    usu = Usuario(nomeU="Alguém", cpf="11111111111", emailU="alguem@gmail.com", senha="111111a")
    vota = Votacao(titulo="Qual a melhor batata?", criador=usu, estiloVotacao="rapida")
    fulano = Candidato(nomeC="Fulano de Tal", descricao="Top", votacao=vota)
    usu.save()
    vota.save()
    fulano.save()
    usu = Candidato.select()
    for i in usu:
        print(i.votacao.titulo)
    