from typing import List

from src.models.entities.gerente_entity import Gerente
from src.models.repository.gerente_repository import gerente_repositorio


class ListarGerentesController:
    def listar(self) -> bool:
        repositorio: List[Gerente] = gerente_repositorio.pegar_repositorio()
        if len(repositorio):
            return True
        return False
