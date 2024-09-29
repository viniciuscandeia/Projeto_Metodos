from abc import ABC, abstractmethod

class AbstractListView(ABC):
    @abstractmethod
    def listar(self)->None:
        pass

    @abstractmethod
    def _lista_vazia(self)->None:
        pass

    @abstractmethod
    def _lista_preenchida(self, list)->None:
        pass