import os
from typing import List

from src.models.entities.administrador_entity import Administrador
from src.models.repository.administrador_repository import adm_repositorio


class ListarAdministradoresView:
    def lista_preenchida(self) -> None:
        os.system("cls||clear")

        repositorio: List[Administrador] = adm_repositorio.pegar_repositorio()

        mensagem = """
Lista de Administradores

"""

        # Usando join para eficiência na criação da string
        lista_adm: str = "\n".join(
            [f"\t- {adm.id_usuario}: {adm.nome}" for adm in repositorio]
        )

        print(mensagem + lista_adm)

    def lista_vazia(self) -> None:
        os.system("cls||clear")

        mensagem = """
Lista vazia de Administradores
"""
        print(mensagem)
