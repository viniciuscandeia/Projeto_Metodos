from src.models.repository.vendedor_repository import VendedorRepositorio
from src.singletons.meta_singleton import  SingletonMeta

class VendedorRepositorySingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.repository = VendedorRepositorio()

    def getInstance(self):
        return self.repository