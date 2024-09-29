from ...models.entities.loja_entity import Loja
from ...models.repository.loja_repository import LojaRepository
from ...models.repository.gerente_repository import GerenteRepositorio
from ...models.repository.administrador_repository import AdministradorRepositorio


class LojaAdicaoController: 
    def __init__(self, administradorRepository:AdministradorRepositorio,  
                gerenteRepository:GerenteRepositorio) -> None:
        self.lojaRepository = LojaRepository(adm_repositorio=administradorRepository, gerente_repositorio=gerenteRepository)

   
    def registrarLoja(self, id_administrador:int, loja: Loja)->bool:
        try:
            return self.lojaRepository.registrar_loja(loja=loja, id_administrador=id_administrador)
        except Exception as e:
            raise Exception(str(e)) from None
        