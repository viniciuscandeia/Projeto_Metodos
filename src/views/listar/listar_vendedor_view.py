import os
from typing import List

from src.models.entities.vendedor_entity import Vendedor
from src.models.repository.vendedor_repository import vendedor_repositorio


class ListarVendedoresView:
    def lista_preenchida(self) -> None:
        os.system("cls||clear")

        repositorio: List[Vendedor] = vendedor_repositorio.pegar_repositorio()

        mensagem = """
Lista de Vendedores

"""

        # Usando join para eficiência na criação da string
        lista_vendedor: str = "\n".join(
            [f"\t- {vendedor.id_usuario}: {vendedor.nome}" for vendedor in repositorio]
        )

        print(mensagem + lista_vendedor)

    def lista_vazia(self) -> None:
        os.system("cls||clear")

        mensagem = """
Lista vazia de Vendedores
"""
        print(mensagem)
