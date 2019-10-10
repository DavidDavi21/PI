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
    codigo_votacao = CharField()

class Candidato(BaseModel):
    nomeC = CharField()
    foto = BigBitField(null=False)
    descricao = CharField()
    votacao = ForeignKeyField(Votacao)
    quantidade_votos = IntegerField()

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Usuario, Candidato, Votacao])
