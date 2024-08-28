"""
Módulo que define o repositório para gerenciar objetos do tipo Gerente.

Este módulo contém a classe GerenteRepositorio, que oferece métodos
para registrar, remover e acessar instâncias de Gerente.
"""

from typing import List

from peewee import DoesNotExist

from ..entities.gerente_entity import Gerente
from ..entities.usuario_db_entity import UsuarioBD
from .usuario_db_repository import usuario_repositorio


class GerenteRepositorio:
    """
    Classe que gerencia o repositório de gerentes.

    Esta classe oferece métodos para registrar, remover e acessar gerentes
    dentro do sistema.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório de gerentes como uma lista vazia.
        """
        self.__gerentes = usuario_repositorio

    def registrar_gerente(self, gerente: Gerente) -> None:
        """
        Registra um novo gerente no repositório.

        :param gerente: Objeto do tipo Gerente a ser adicionado.
        :type gerente: Gerente
        """
        UsuarioBD.create(
            nome=gerente.nome,
            email=gerente.email,
            senha=gerente.senha,
            user_type="GERENTE",
        )

    def remover_gerente(self, _id: str) -> None:
        """
        Remove um gerente do repositório com base no ID fornecido.

        :param _id: ID do gerente a ser removido.
        :type _id: str
        """
        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            return None

    def pegar_repositorio(self) -> List[Gerente]:
        """
        Retorna a lista atual de gerentes no repositório.

        :return: Lista de objetos Gerente.
        :rtype: List[Gerente]
        """
        lista_gerentes = [
            Gerente(nome=gerente.nome, email=gerente.email,
                    senha=gerente.senha, id_store=0)
            for gerente in UsuarioBD.select().where(UsuarioBD.user_type == "GERENTE")
        ]
        return lista_gerentes


gerente_repositorio = GerenteRepositorio()
