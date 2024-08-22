import os
from typing import List

from src.models.entities.gerente_entity import Gerente
from src.models.repository.gerente_repository import gerente_repositorio


class ListarGerentesView:
    def lista_preenchida(self) -> None:
        os.system("cls||clear")

        repositorio: List[Gerente] = gerente_repositorio.pegar_repositorio()

        mensagem = """
Lista de Gerentes

"""

        # Usando join para eficiência na criação da string
        lista_gerentes: str = "\n".join(
            [f"\t- {gerente.id_usuario}: {gerente.nome}" for gerente in repositorio]
        )

        print(mensagem + lista_gerentes)

    def lista_vazia(self) -> None:
        os.system("cls||clear")

        mensagem = """
Lista vazia de Gerentes
"""
        print(mensagem)
