"""
Módulo para a visualização da listagem de vendedores.

Este módulo define a classe `ListarVendedoresView`, que contém métodos para
exibir a lista de vendedores do sistema, seja em um formato preenchido ou
informando que a lista está vazia.
"""

import os
from typing import List

from ...models.entities.vendedor_entity import Vendedor
from ...singletons.vendedor_repository_singleton import VendedorRepositorySingleton


class ListarVendedoresView:
    """
    Classe de interface para listar vendedores do sistema.

    Esta classe contém métodos para exibir uma lista de vendedores,
    seja quando a lista está preenchida ou quando está vazia.
    """

    def __init__(self):
        self.vendedor_repositorio = VendedorRepositorySingleton().getInstance()

    def lista_preenchida(self) -> None:
        """
        Exibe a lista de vendedores quando a mesma não está vazia.

        A lista de vendedores é obtida do repositório de vendedores
        e exibida no formato de nome e email.
        """

        os.system("cls||clear")
        #TODO: View nao pode acessar repositorio direto
        repositorio: List[Vendedor] = self.vendedor_repositorio.pegar_repositorio()

        mensagem = """
Lista de Vendedores

"""

        # Usando join para eficiência na criação da string
        lista_vendedor: str = "\n".join(
            [f"\t- [{vendedor.id}] {vendedor.nome}: {vendedor.email}" for vendedor in repositorio]
        )

        print(mensagem + lista_vendedor)

    def lista_vazia(self) -> None:
        """
        Exibe uma mensagem informando que a lista de vendedores está vazia.
        """

        os.system("cls||clear")

        mensagem = """
Lista vazia de Vendedores.
"""
        print(mensagem)
