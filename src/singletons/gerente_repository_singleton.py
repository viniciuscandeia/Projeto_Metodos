from src.models.repository.gerente_repository import GerenteRepositorio
from src.singletons.meta_singleton import SingletonMeta


class GerenteRepositorySingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.repository = GerenteRepositorio()

    def getInstance(self):
        return self.repository
