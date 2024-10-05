from src.controllers.administrador_controller import AdministradorController
from src.controllers.relatorios.relatorio import Relatorio
from src.controllers.relatorios.relatorio_html import RelatorioHTML
from src.controllers.relatorios.relatorio_pdf import RelatorioPdf
from src.singletons.adm_repository_singleton import AdmRepositorySingleton
from src.singletons.gerente_repository_singleton import GerenteRepositorySingleton
from src.singletons.vendedor_repository_singleton import VendedorRepositorySingleton


class AdministradorFacade:
    def __init__(self, ):
        self.adm_controller = AdministradorController()

    def gerar_relatorio(self):
        try:
            self.adm_controller.enviar_relatorio()
        except Exception as e:
            print(e)

adm_facade = AdministradorFacade()