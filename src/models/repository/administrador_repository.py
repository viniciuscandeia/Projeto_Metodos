"""
Módulo que define o repositório para gerenciar objetos do tipo Administrador.

Este módulo contém a classe AdministradorRepositorio, que oferece métodos
para registrar, remover e acessar instâncias de Administrador.
"""

from typing import List

from peewee import DoesNotExist

from ..entities.administrador_entity import Administrador
from ..entities.usuario_db_entity import UsuarioBD
from .usuario_db_repository import usuario_repositorio


class AdministradorRepositorio:
    """
    Classe que gerencia o repositório de administradores.

    Esta classe oferece métodos para registrar, remover e acessar administradores
    dentro do sistema.
    """

    def __init__(self) -> None:
        """
        Inicializa um novo repositório de administradores.
        """

        self.usuario = usuario_repositorio

    def registrar_administrador(self, administrador: Administrador) -> None:
        """
        Registra um novo administrador no repositório.

        :param administrador: Objeto do tipo Administrador a ser adicionado.
        :type administrador: Administrador
        """

        UsuarioBD.create(
            nome=administrador.nome,
            email=administrador.email,
            senha=administrador.senha,
            user_type="VENDEDOR",
        )

    def remover_administrador(self, _id: str) -> None:
        """
        Remove um administrador do repositório com base no ID fornecido.

        :param _id: ID do administrador a ser removido.
        :type _id: str
        """

        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            return None

    def pegar_repositorio(self) -> List[Administrador]:
        """
        Retorna a lista atual de administradores no repositório.

        :return: Lista de objetos Administrador.
        :rtype: List[Administrador]
        """
        """
        Retorna a lista atual de administradores no repositório.

        :return: Lista de objetos Administrador.
        :rtype: List[Administrador]
        """

        lista_administradores = [
            Administrador(nome=adm.nome, email=adm.email, senha=adm.senha)
            for adm in UsuarioBD.select().where(UsuarioBD.user_type == "ADMINISTRADOR")
        ]
        return lista_administradores
        lista_administradores = [
            Administrador(nome=adm.nome, email=adm.email, senha=adm.senha)
            for adm in UsuarioBD.select().where(UsuarioBD.user_type == "ADMINISTRADOR")
        ]
        return lista_administradores


adm_repositorio = AdministradorRepositorio()
