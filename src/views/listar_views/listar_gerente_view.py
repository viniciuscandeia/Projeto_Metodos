"""
Módulo para a visualização da listagem de gerentes.

Este módulo define a classe `ListarGerentesView`, que contém métodos para
exibir a lista de gerentes do sistema, seja em um formato preenchido ou
informando que a lista está vazia.
"""

import os
from typing import List

from ...models.entities.gerente_entity import Gerente
from ...singletons.gerente_repository_singleton import GerenteRepositorySingleton


class ListarGerentesView:
    def __init__(self):
        self.gerente_repositorio = GerenteRepositorySingleton().getInstance()
    """
    Classe de interface para listar gerentes do sistema.

    Esta classe contém métodos para exibir uma lista de gerentes,
    seja quando a lista está preenchida ou quando está vazia.
    """

    def lista_preenchida(self) -> None:
        """
        Exibe a lista de gerentes quando a mesma não está vazia.

        A lista de gerentes é obtida do repositório de gerentes
        e exibida no formato de nome e email.
        """

        os.system("cls||clear")

        #TODO: isso ta errado, uma view n pode acessar direto uma instancia do repositorio
        repositorio: List[Gerente] = self.gerente_repositorio.pegar_repositorio()

        mensagem = """
Lista de Gerentes

"""

        # Usando join para eficiência na criação da string
        lista_gerentes: str = "\n".join(
            [f"\t- [{gerente.id}] {gerente.nome}: {gerente.email}" for gerente in repositorio]
        )

        print(mensagem + lista_gerentes)

    def lista_vazia(self) -> None:
        """
        Exibe uma mensagem informando que a lista de gerentes está vazia.
        """

        os.system("cls||clear")

        mensagem = """
Lista vazia de Gerentes.
"""
        print(mensagem)
