"""
Módulo que define o repositório para gerenciar objetos do tipo Administrador.

Este módulo contém a classe AdministradorRepositorio, que oferece métodos
para registrar, remover e acessar instâncias de Administrador.
"""

from typing import List

from ..entities.administrador_entity import Administrador
from ..entities.usuario_entity import Usuario as UsuarioEntity
from db import Usuario

class AdministradorRepositorio:
    """
    Classe que gerencia o repositório de administradores.

    Esta classe oferece métodos para registrar, remover e acessar administradores
    dentro do sistema.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório de administradores como uma lista vazia.
        """
        self.usuario = Usuario

    def registrar_administrador(self, administrador: Administrador) -> None:
        """
        Registra um novo administrador no repositório.

        :param administrador: Objeto do tipo Administrador a ser adicionado.
        :type administrador: Administrador
        """
        self.usuario.create(nome=administrador.nome, email=administrador.email, senha=administrador.senha, user_type="ADMINISTRADOR")


    def remover_administrador(self, _id: str) -> None:
        """
        Remove um administrador do repositório com base no ID fornecido.

        :param id: ID do administrador a ser removido.
        :type id: str
        """
        for adm in self.__adm:
            if adm.id == _id:
                self.usuario.delete().where(self.usuario.id == _id).execute()
                return

    def pegar_repositorio(self) -> List[Administrador]:
        """
        Retorna a lista atual de administradores no repositório.

        :return: Lista de objetos Administrador.
        :rtype: List[Administrador]
        """
        users_list = [ UsuarioEntity(id_usuario=user.id, nome=user.nome, email=user.email, senha=user.senha ) for user in self.usuario.select()]
        return users_list

adm_repositorio = AdministradorRepositorio()
