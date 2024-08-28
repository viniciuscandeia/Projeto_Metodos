from peewee import *

db = SqliteDatabase("database.db")

class Usuario(Model):
    nome = CharField()
    email = CharField()
    senha = CharField()
    user_type = CharField(constraints=[Check("user_type in ('ADMINISTRADOR', 'GERENTE', 'VENDEDOR') ")])
    class Meta:
        database = db
