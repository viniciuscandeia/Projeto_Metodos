from ..models.entities.loja_entity import Loja
from ..models.repository.loja_repository import LojaRepository
from ..models.repository.gerente_repository import GerenteRepositorio
from ..models.repository.administrador_repository import AdministradorRepositorio
from ..models.entities_db.loja_db_entity import LojaDB


class LojaController:

    def __init__(self, administradorRepository: AdministradorRepositorio,
                 gerenteRepository: GerenteRepositorio) -> None:
        self.lojaRepository = LojaRepository(
            adm_repositorio=administradorRepository, gerente_repositorio=gerenteRepository)

    def registrarLoja(self, id_administrador: int, loja: Loja) -> bool:
        try:
            self.lojaRepository.registrar_loja(loja=loja, id_administrador=id_administrador)
            return True
        except Exception as e:
            raise Exception(str(e)) from None

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

    def excluir_loja(self, id_adm: int, id_loja: int):
        return self.lojaRepository.excluir_loja(id_adm=id_adm, id_loja=id_loja)

    def list_lojas_adm(self, id_adm: int) -> list[LojaDB]:
        lojas: list[LojaDB] = self.lojaRepository.listar_lojas_adm(
            id_adm=id_adm)
        if lojas:
            return lojas
        return []

    def get_loja_adm(self, id_adm: int, id_loja: int) -> LojaDB:
        loja: LojaDB = self.lojaRepository.get_loja_adm(
            id_adm=id_adm, id_loja=id_loja)
        if loja:
            return loja

    def get_loja_gerente(self, id_gerente: int, id_loja: int) -> LojaDB:
        loja: LojaDB = self.lojaRepository.get_loja_gerente(
            id_gerente=id_gerente, id_loja=id_loja)
        if loja:
            return loja
