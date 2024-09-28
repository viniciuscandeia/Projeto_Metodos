from ...models.entities.entities_db.loja_db_entity import LojaDB
from ...models.repository.loja_repository import LojaRepository
from ...models.repository.gerente_repository import GerenteRepositorio
from ...models.repository.administrador_repository import AdministradorRepositorio

from typing import List

class ListarLojaController:
    def __init__(self, gerenteRepository:GerenteRepositorio, administradorRepository:AdministradorRepositorio) -> None:
        self.lojaRepository = LojaRepository(adm_repositorio=administradorRepository, gerente_repositorio=gerenteRepository)
   
 
    def list_lojas_adm(self, id_adm:int) -> List[LojaDB]:
        lojas:List[LojaDB]  = self.lojaRepository.listar_lojas_adm(id_adm=id_adm)
        if lojas:
            return lojas
        return []
    
    def get_loja_adm(self, id_adm:int, id_loja:int) -> LojaDB:
        loja:LojaDB  = self.lojaRepository.get_loja_adm(id_adm=id_adm, id_loja=id_loja)
        if loja:
            return loja
    
    def get_loja_gerente(self, id_gerente:int, id_loja:int) -> LojaDB:
        loja:LojaDB  = self.lojaRepository.get_loja_gerente(id_gerente=id_gerente, id_loja=id_loja)
        if loja:
            return loja