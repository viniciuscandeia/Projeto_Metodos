from typing import List

from src.models.entities.administrador_entity import Administrador


class AdministradorRepositorio:
    def __init__(self) -> None:
        self.__adm: List[Administrador] = []

    def registrar_administrador(self, administrador: Administrador) -> None:
        self.__adm.append(administrador)

    def remover_administrador(self, id: str) -> None:
        for adm in self.__adm:
            if adm.id == id:
                self.__adm.remove(adm)
                return

    def pegar_repositorio(self) -> List[Administrador]:
        return self.__adm


adm_repositorio = AdministradorRepositorio()
