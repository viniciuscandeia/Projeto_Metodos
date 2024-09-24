from ...models.entities.loja_db_entity import LojaDB
from ...models.repository.loja_repository import LojaRepository
from ...models.repository.gerente_repository import GerenteRepositorio
from ...models.repository.administrador_repository import AdministradorRepositorio


class ExcluirLojaController:
    def __init__(self, administradorRepository:AdministradorRepositorio, 
                       gerenteRepository:GerenteRepositorio ):
        self.lojaRepository = LojaRepository(adm_repositorio=administradorRepository, 
                                             gerente_repositorio=gerenteRepository)

    def excluir_loja(self, id_adm:int,id_loja:int):
        return self.lojaRepository.excluir_loja(id_adm=id_adm, id_loja=id_loja)
        
