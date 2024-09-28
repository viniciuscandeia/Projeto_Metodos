from peewee import Model
from peewee import CharField, Model, AutoField
from ...database import database_persistente

class LojaDB(Model):
    id = AutoField()
    nome = CharField()
    endereco = CharField()

    class Meta:
        database = database_persistente
