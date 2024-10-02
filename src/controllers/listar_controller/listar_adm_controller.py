"""
Módulo para controle da listagem de administradores no sistema.

Este módulo contém o controlador `ListarAdministradoresController` que é responsável
por verificar a existência de administradores cadastrados no repositório.
"""

from typing import List

from ...models.entities.usuario_db_entity import UsuarioBD
from ...models.repository.administrador_repository import adm_repositorio


class ListarAdministradoresController:
    """
    Controller para listar administradores.

    Métodos:
    - listar: Verifica se há administradores no repositório.
    """

    def listar(self) -> bool:
        repositorio: List[UsuarioBD] = adm_repositorio.pegar_repositorio()
        if repositorio:
            return True
        return False
