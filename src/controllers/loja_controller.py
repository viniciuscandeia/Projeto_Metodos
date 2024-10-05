from ..adapters.database_adapter_notificator_api import DatabaseAdapterNotificatorApi
from ..lib.notificator_api import NotificatorApi
from ..models.entities.loja_entity import Loja
from ..models.entities_db.loja_db_entity import LojaDB
from ..singletons.loja_repository_singleton import LojaRepositorySingleton
from ..singletons.notification_repository_singleton import NotificationRepositorySingleton


class LojaController:

    def __init__(self) -> None:
        self.lojaRepository = LojaRepositorySingleton().getInstance()
        self.notificatorApi = DatabaseAdapterNotificatorApi()

    def registrarLoja(self, id_administrador: int, loja: Loja) -> bool:
        try:
            self.lojaRepository.registrar_loja(loja=loja, id_administrador=id_administrador)
            return True
        except Exception as e:
            raise Exception(str(e)) from None

    def editar_loja_adm(self, id_adm: int, id_loja, nova_loja: dict):
        try:
            edited_loja = self.lojaRepository.editar_loja_administrador(id_adm=id_adm, id_loja=id_loja, nova_loja=nova_loja)
            if edited_loja:
                self.notificatorApi.send(id_loja=id_loja, id_adm=id_adm, mensagem=f"Loja com id {id_loja} foi editada pelo adm de id {id_adm}")

                return edited_loja
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
