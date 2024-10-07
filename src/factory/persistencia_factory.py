from ..singletons.adm_repository_singleton import AdmRepositorySingleton
from ..singletons.gerente_repository_singleton import GerenteRepositorySingleton
from ..singletons.vendedor_repository_singleton import VendedorRepositorySingleton


class PersistenciaFactory:

    @classmethod
    def criar_persistencia(self, tipo: str):
        if tipo == 'adm_db':
            return AdmRepositorySingleton()
        elif tipo == 'gerente_db':
            return GerenteRepositorySingleton()
        elif tipo == 'vendedor_db':
            return VendedorRepositorySingleton()
        else:
            raise Exception("Tipo de persistência inválida")
