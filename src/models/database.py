"""
Este módulo contém a configuração da instância do banco de dados SQLite
usando o ORM Peewee. A instância `database` é criada para fornecer uma única
conexão ao banco de dados, que é compartilhada por todo o projeto.

A instância do banco de dados é usada por outros módulos para realizar
operações de leitura e escrita no banco de dados.
"""

from peewee import SqliteDatabase
# Criação da instância do banco de dados SQLite


database_persistente = SqliteDatabase("./src/data/database.db")
database_memoria = SqliteDatabase(':memory:')


