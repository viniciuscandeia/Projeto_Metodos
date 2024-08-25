"""
Módulo que define o repositório para gerenciar objetos do tipo Administrador.

Este módulo contém a classe AdministradorRepositorio, que oferece métodos
para registrar, remover e acessar instâncias de Administrador.
"""

from typing import List

from ..entities.administrador_entity import Administrador


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
        self.__adm: List[Administrador] = []

    def registrar_administrador(self, administrador: Administrador) -> None:
        """
        Registra um novo administrador no repositório.

        :param administrador: Objeto do tipo Administrador a ser adicionado.
        :type administrador: Administrador
        """
        self.__adm.append(administrador)

    def remover_administrador(self, _id: str) -> None:
        """
        Remove um administrador do repositório com base no ID fornecido.

        :param id: ID do administrador a ser removido.
        :type id: str
        """
        for adm in self.__adm:
            if adm.id == _id:
                self.__adm.remove(adm)
                return

    def pegar_repositorio(self) -> List[Administrador]:
        """
        Retorna a lista atual de administradores no repositório.

        :return: Lista de objetos Administrador.
        :rtype: List[Administrador]
        """
        return self.__adm


adm_repositorio = AdministradorRepositorio()
