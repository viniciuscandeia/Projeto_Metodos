from typing import List

from src.models.entities.administrador_entity import Administrador
from src.models.repository.administrador_repository import adm_repositorio


class ListarAdministradoresController:
    def listar(self) -> bool:
        repositorio: List[Administrador] = adm_repositorio.pegar_repositorio()
        if len(repositorio):
            return True
        return False
