from typing import List

from src.models.entities.gerente_entity import Gerente


class GerenteRepositorio:
    def __init__(self) -> None:
        self.__gerentes: List[Gerente] = []

    def registrar_gerente(self, gerente: Gerente) -> None:
        self.__gerentes.append(gerente)

    def remover_gerente(self, _id: str) -> None:
        for gerente in self.__gerentes:
            if gerente.id == _id:
                self.__gerentes.remove(gerente)
                return

    def pegar_repositorio(self) -> List[Gerente]:
        return self.__gerentes


gerente_repositorio = GerenteRepositorio()
