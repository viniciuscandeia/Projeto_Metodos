from ...models.entities.entities_db.loja_db_entity import LojaDB
from ...models.repository.loja_repository import LojaRepository
from ...models.repository.gerente_repository import GerenteRepositorio
from ...models.repository.administrador_repository import AdministradorRepositorio

from typing import List


class EditarLojaController:
    def __init__(self, gerenteRepository:GerenteRepositorio, administradorRepository:AdministradorRepositorio) -> None:
        self.lojaRepository = LojaRepository(adm_repositorio=administradorRepository, gerente_repositorio=gerenteRepository)

    def editar_loja_adm(self, id_adm: int, id_loja, nova_loja: dict):
        try:
            return self.lojaRepository.editar_loja_administrador(id_adm=id_adm, id_loja=id_loja, nova_loja=nova_loja)
        except Exception as e:
            raise Exception(str(e)) from None
        
    def editar_loja_gerente(self, id_gerente: int, id_loja, nova_loja: dict):
        try:
            return self.lojaRepository.editar_loja_gerente(id_gerente=id_gerente, id_loja=id_loja, nova_loja=nova_loja)
        except Exception as e:
            raise Exception(str(e)) from None

        