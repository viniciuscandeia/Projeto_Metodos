"""
Módulo que define o repositório para gerenciar objetos do tipo Vendedor.

Este módulo contém a classe VendedorRepositorio, que oferece métodos
para registrar, remover e acessar instâncias de Vendedor.
"""

from typing import List

from ..entities.vendedor_entity import Vendedor


class VendedorRepositorio:
    """
    Classe que gerencia o repositório de vendedores.

    Esta classe oferece métodos para registrar, remover e acessar vendedores
    dentro do sistema.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório de vendedores como uma lista vazia.
        """
        self.__vendedores: List[Vendedor] = []

    def registrar_vendedor(self, vendedor: Vendedor) -> None:
        """
        Registra um novo vendedor no repositório.

        :param vendedor: Objeto do tipo Vendedor a ser adicionado.
        :type vendedor: Vendedor
        """
        self.__vendedores.append(vendedor)

    def remover_vendedor(self, _id: str) -> None:
        """
        Remove um vendedor do repositório com base no ID fornecido.

        :param _id: ID do vendedor a ser removido.
        :type _id: str
        """
        for vendedor in self.__vendedores:
            if vendedor.id == _id:
                self.__vendedores.remove(vendedor)
                return

    def pegar_repositorio(self) -> List[Vendedor]:
        """
        Retorna a lista atual de vendedores no repositório.

        :return: Lista de objetos Vendedor.
        :rtype: List[Vendedor]
        """
        return self.__vendedores


vendedor_repositorio = VendedorRepositorio()
