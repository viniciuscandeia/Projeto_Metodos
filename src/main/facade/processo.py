from abc import ABC, abstractmethod

class Processo(ABC):
    @abstractmethod
    def executar(self):
        pass