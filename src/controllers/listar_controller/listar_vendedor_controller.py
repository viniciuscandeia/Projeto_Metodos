"""
Módulo para controle da listagem de vendedores no sistema.

Este módulo contém o controlador `VendedoresListController` que é responsável
por verificar a existência de vendedores cadastrados no repositório.
"""

from typing import List

from ...models.entities.vendedor_entity import Vendedor
from ...models.repository.vendedor_repository import vendedor_repositorio


class VendedoresListController:
    """
    Controller para listar vendedores.

    Métodos:
    - listar: Verifica se há vendedores no repositório.
    """

    def listar(self) -> bool:
        """
        Verifica se existem vendedores cadastrados no repositório.

        Retorna:
            bool: True se houver pelo menos um vendedor, False caso contrário.
        """
        repositorio: List[Vendedor] = vendedor_repositorio.pegar_repositorio()
        if repositorio:
            return True
        return False
