"""
Módulo que define o repositório para gerenciar objetos do tipo Gerente.

Este módulo contém a classe GerenteRepositorio, que oferece métodos
para registrar, remover e acessar instâncias de Gerente.
"""

from typing import List

from ..entities.gerente_entity import Gerente


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
        self.__gerentes: List[Gerente] = []

    def registrar_gerente(self, gerente: Gerente) -> None:
        """
        Registra um novo gerente no repositório.

        :param gerente: Objeto do tipo Gerente a ser adicionado.
        :type gerente: Gerente
        """
        self.__gerentes.append(gerente)

    def remover_gerente(self, _id: str) -> None:
        """
        Remove um gerente do repositório com base no ID fornecido.

        :param _id: ID do gerente a ser removido.
        :type _id: str
        """
        for gerente in self.__gerentes:
            if gerente.id == _id:
                self.__gerentes.remove(gerente)
                return

    def pegar_repositorio(self) -> List[Gerente]:
        """
        Retorna a lista atual de gerentes no repositório.

        :return: Lista de objetos Gerente.
        :rtype: List[Gerente]
        """
        return self.__gerentes


gerente_repositorio = GerenteRepositorio()
