"""
Este módulo define a classe `UsuarioRepositorio`, responsável por gerenciar
a conexão e operações com o banco de dados SQLite para o modelo de dados `UsuarioBD`.
Ele utiliza o ORM Peewee para interagir com o banco de dados e realizar operações
como criação de tabelas e fechamento de conexões.

O `UsuarioRepositorio` fornece métodos para inicializar o banco de dados, obter
a conexão atual e fechar a conexão quando não for mais necessária.
"""

from ..database import database
from ..entities.usuario_db_entity import UsuarioBD


class UsuarioRepositorio:
    """
    Classe para gerenciar a conexão e operações com o banco de dados SQLite.

    Atributos:
        database (SqliteDatabase): A instância do banco de dados SQLite.
    """

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados.
        """

        self.database = database
        self.inicializar()

    def inicializar(self):
        """
        Inicializa o banco de dados, criando as tabelas se necessário.
        """
        with self.database:
            # Cria as tabelas que foram definidas nos modelos.
            self.database.create_tables([UsuarioBD])

    def pegar_repositorio(self):
        """
        Retorna a instância do banco de dados.

        Returns:
            SqliteDatabase: A instância do banco de dados SQLite.
        """
        return self.database

    def fechar(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.database.close()


# Instancia o repositório com o caminho para o banco de dados
usuario_repositorio = UsuarioRepositorio()
