from typing import List

from src.models.entities.vendedor_entity import Vendedor


class VendedorRepositorio:
    def __init__(self) -> None:
        self.__vendedores: List[Vendedor] = []

    def registrar_vendedor(self, vendedor: Vendedor) -> None:
        self.__vendedores.append(vendedor)

    def remover_vendedor(self, _id: str) -> None:
        for vendedor in self.__vendedores:
            if vendedor.id == _id:
                self.__vendedores.remove(vendedor)
                return

    def pegar_repositorio(self) -> List[Vendedor]:
        return self.__vendedores


vendedor_repositorio = VendedorRepositorio()
