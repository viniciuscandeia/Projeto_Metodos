"""
Módulo para a visualização da listagem de administradores.

Este módulo define a classe `AdministradoresListagemView`, que contém métodos para
exibir a lista de administradores do sistema, seja em um formato preenchido ou
informando que a lista está vazia.
"""

import os
from typing import List

from ...models.entities.administrador_entity import Administrador
from ...models.repository.administrador_repository import adm_repositorio


class AdministradoresListagemView:
    """
    Classe de interface para listar administradores do sistema.

    Esta classe contém métodos para exibir uma lista de administradores,
    seja quando a lista está preenchida ou quando está vazia.
    """

    def lista_preenchida(self) -> None:
        """
        Exibe a lista de administradores quando a mesma não está vazia.

        A lista de administradores é obtida do repositório de administradores
        e exibida no formato de nome e email.
        """

        os.system("cls||clear")

        repositorio: List[Administrador] = adm_repositorio.pegar_repositorio()

        mensagem = """
Lista de Administradores

"""

        # Usando join para eficiência na criação da string
        lista_adm: str = "\n".join(
            [f"\t- {adm.id} {adm.nome}: {adm.email}" for adm in repositorio]
        )

        print(mensagem + lista_adm)

    def lista_vazia(self) -> None:
        """
        Exibe uma mensagem informando que a lista de administradores está vazia.
        """

        os.system("cls||clear")

        mensagem = """
Lista vazia de Administradores.
"""
        print(mensagem)
