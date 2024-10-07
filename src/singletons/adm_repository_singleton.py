from src.models.repository.administrador_repository import AdministradorRepositorio
from src.singletons.meta_singleton import SingletonMeta


class AdmRepositorySingleton(metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        self.repository = AdministradorRepositorio()

    def getInstance(self):
        return self.repository
