"""
Módulo que define o repositório para gerenciar objetos do tipo Vendedor.

Este módulo contém a classe VendedorRepositorio, que oferece métodos
para registrar, remover e acessar instâncias de Vendedor.
"""

from typing import List

from peewee import DoesNotExist

from ..entities.usuario_db_entity import UsuarioBD
from ..entities.vendedor_entity import Vendedor
from .usuario_db_repository import usuario_repositorio


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
        self.__vendedores = usuario_repositorio

    def registrar_vendedor(self, vendedor: Vendedor) -> None:
        """
        Registra um novo vendedor no repositório.

        :param vendedor: Objeto do tipo Vendedor a ser adicionado.
        :type vendedor: Vendedor
        """

        UsuarioBD.create(
            nome=vendedor.nome,
            email=vendedor.email,
            senha=vendedor.senha,
            user_type="VENDEDOR",
        )

    def remover_vendedor(self, _id: str) -> None:
        """
        Remove um vendedor do repositório com base no ID fornecido.

        :param _id: ID do vendedor a ser removido.
        :type _id: str
        """

        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            return None

    def pegar_repositorio(self) -> List[Vendedor]:
        """
        Retorna a lista atual de vendedores no repositório.

        :return: Lista de objetos Vendedor.
        :rtype: List[Vendedor]
        """

        lista_vendedores = [
            Vendedor(nome=vendedor.nome, email=vendedor.email,
                     senha=vendedor.senha, id_store=0)
            for vendedor in UsuarioBD.select().where(
                UsuarioBD.user_type == "VENDEDOR"
            )
        ]
        return lista_vendedores


vendedor_repositorio = VendedorRepositorio()
