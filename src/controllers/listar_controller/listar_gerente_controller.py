"""
Módulo para controle da listagem de gerentes no sistema.

Este módulo contém o controlador `ListarGerentesController` que é responsável
por verificar a existência de gerentes cadastrados no repositório.
"""

from typing import List

from ...models.entities.gerente_entity import Gerente
from ...models.repository.gerente_repository import gerente_repositorio


class ListarGerentesController:
    """
    Controller para listar gerentes.

    Métodos:
    - listar: Verifica se há gerentes no repositório.
    """

    def listar(self) -> bool:
        """
        Verifica se existem gerentes cadastrados no repositório.

        Retorna:
            bool: True se houver pelo menos um gerente, False caso contrário.
        """
        repositorio: List[Gerente] = gerente_repositorio.pegar_repositorio()
        if repositorio:
            return True
        return False
