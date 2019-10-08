import bdballot
from peewee import CharField, FloatField, IntegerField, BigBitField, ForeignKeyField, SqliteDatabase, Model

votacaozinha = bdballot.Votacao(titulo="Qual a melhor batata?", criador='Amadeu', estiloVotacao="rapida", codigo_votacao="uebs")

votacao1 = bdballot.Votacao.select()
votacao = list(votacao1)

print(votacao1)
print(votacao)

for i in list(votacao):
    print(i.Votacao.titulo)
    print(i.Votacao.criador)
    print(i.Votacao.estiloVotacao)
    print(i.Votacao.codigo_votacao)
