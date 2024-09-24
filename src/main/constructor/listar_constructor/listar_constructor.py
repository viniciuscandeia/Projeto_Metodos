from abc import ABC, abstractmethod


class ListarConstructor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def listar_adm(self, id_adm:int):
        pass
    
    @abstractmethod
    def get_loja_adm(self, id_adm:int, id_loja:int):
        pass
    
    @abstractmethod
    def get_loja_gerente(self, id_gerente:int, id_loja:int):
        pass
    