"""
Módulo de inicialização de banco de dados.

Este módulo contém a função responsável por inicializar o banco de dados,
permitindo escolher entre um banco de dados em memória ou uma instância persistente,
e criar as tabelas necessárias para a aplicação.

Classes:
    UsuarioBD: Classe de entidade representando os usuários no banco de dados.

Funções:
    inicializar_database(usar_memoria: bool): Inicializa o banco de dados, utilizando uma
    base de dados em memória ou persistente, e cria as tabelas necessárias.
"""

from .database import database_memoria, database_persistente
from .entities.entities_db.usuario_db_entity import UsuarioBD
from .entities.entities_db.loja_db_entity import LojaDB


def inicializar_database(usar_memoria: bool):
    """
    Inicializa o banco de dados e cria as tabelas da aplicação.

    Conecta ao banco de dados escolhido (memória ou persistente) e
    cria as tabelas necessárias para a aplicação.

    Args:
        usar_memoria (bool): Define se o banco de dados deve ser armazenado em memória.
                             Se True, utiliza o banco de dados em memória, caso contrário,
                             utiliza o banco de dados persistente.

    Raises:
        peewee.OperationalError: Se houver problemas ao conectar ou criar as tabelas
        no banco de dados.
    """

    if usar_memoria:
        database_memoria.connect()
        database_memoria.create_tables([UsuarioBD, LojaDB])
    else:
        database_persistente.connect()
        database_persistente.create_tables([UsuarioBD, LojaDB])

    # UsuarioBD._meta.database.connect()
    # UsuarioBD._meta.database.create_tables([UsuarioBD])
