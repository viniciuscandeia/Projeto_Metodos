from typing import List

from src.models.entities.vendedor_entity import Vendedor
from src.models.repository.vendedor_repository import vendedor_repositorio


class ListarVendedoresController:
    def listar(self) -> bool:
        repositorio: List[Vendedor] = vendedor_repositorio.pegar_repositorio()
        if len(repositorio):
            return True
        return False
