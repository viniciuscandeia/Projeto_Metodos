"""
Este módulo define o modelo de dados para o gerenciamento de usuários
em um banco de dados SQLite usando o ORM Peewee. O modelo `Usuario`
representa um usuário com informações básicas, como nome, email,
senha e tipo de usuário. O banco de dados SQLite é utilizado para
persistir os dados.
"""

from peewee import CharField, Check, Model, AutoField

from ...database import database_persistente


class UsuarioBD(Model):
    """
    Modelo de dados que representa um usuário no sistema.

    Atributos:
        id (AutoField): A chave primária do usuário.
        nome (CharField): O nome do usuário.
        email (CharField): O email do usuário.
        senha (CharField): A senha do usuário.
        user_type (CharField): O tipo de usuário, que deve ser um dos seguintes:
            'ADMINISTRADOR', 'GERENTE' ou 'VENDEDOR'.
    """

    id = AutoField()
    nome = CharField()
    username = CharField()
    email = CharField()
    senha = CharField()
    user_type = CharField(
        constraints=[Check("user_type in ('ADMINISTRADOR', 'GERENTE', 'VENDEDOR')")]
    )

    class Meta:
        """
        Configurações de metadados do modelo.

        Atributos:
            database (SqliteDatabase): A instância do banco de dados SQLite a ser
            usada pelo modelo.
        """

        database = database_persistente
