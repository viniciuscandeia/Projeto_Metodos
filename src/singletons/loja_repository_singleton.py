from src.models.repository.loja_repository import LojaRepository
from src.singletons.meta_singleton import SingletonMeta


class LojaRepositorySingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.repository = LojaRepository()

    def getInstance(self):
        return self.repository
