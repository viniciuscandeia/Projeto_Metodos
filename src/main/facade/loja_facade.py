from src.main.facade.listar_facade.listar_facade import Listarfacade
from src.views.listar_views.listar_lojas_view import ListarLojasView
from src.controllers.listar_controller.listar_loja_controller import ListarLojaController
from src.controllers.editar_controller.editar_loja_controller import EditarLojaController
from src.models.repository.gerente_repository import GerenteRepositorio
from src.models.repository.administrador_repository import AdministradorRepositorio
from src.controllers.excluir_controller.excluir_loja_controller import ExcluirLojaController
from src.controllers.adicionar_controller.adicionar_loja_controller import RegistrarLojaController
from src.models.entities.loja_entity import Loja

class Lojafacade(Listarfacade):
    def __init__(self,gerenteRepository:GerenteRepositorio, administradorRepository:AdministradorRepositorio) -> None:
        super().__init__()
        self.listar_loja_view = ListarLojasView()
        self.listar_loja_controller = ListarLojaController(administradorRepository=administradorRepository,
                                                           gerenteRepository=gerenteRepository)
        self.editar_loja_controller = EditarLojaController(administradorRepository=administradorRepository,
                                                           gerenteRepository=gerenteRepository)
        self.excluir_loja_controller = ExcluirLojaController(administradorRepository=administradorRepository,
                                                           gerenteRepository=gerenteRepository)
        self.registrar_loja_controller = RegistrarLojaController(administradorRepository=administradorRepository,
                                                           gerenteRepository=gerenteRepository)

    def registrar_loja(self, id_admnistrador:int, loja:Loja):
        try:
            created = self.registrar_loja_controller.registrarLoja(id_administrador=id_admnistrador, loja=loja)
            if created:
                print('Loja Criada')
        except Exception as error:
            print(error)
    def listar_adm(self, id_adm:int):
        try:
            list = self.listar_loja_controller.list_lojas_adm(id_adm=id_adm)

            self.listar_loja_view.listar(list)
        except Exception as error:
            print(error);

    def get_loja_adm(self, id_adm:int, id_loja:int):
         try:
            list = self.listar_loja_controller.get_loja_adm(id_adm=id_adm, id_loja=id_loja)

            self.listar_loja_view.listar([list])
            return list
         except Exception as error:
            print(error);

    def get_loja_gerente(self, id_gerente:int, id_loja:int):
        try:
            list = self.listar_loja_controller.get_loja_gerente(id_gerente=id_gerente, id_loja=id_loja)

            self.listar_loja_view.listar([list])
            return list
        except Exception as error:
            print(error);

    def editar_loja_adm(self, id_adm:int, id_loja:int, nova_loja:dict):
        try:
            item = self.editar_loja_controller.editar_loja_adm(id_adm=id_adm, id_loja=id_loja, nova_loja=nova_loja)
            self.listar_loja_view.listar([item])

            return item
        except Exception as error:
            print(error);

    def editar_loja_gerente(self, id_gerente:int, id_loja:int, nova_loja:dict):
        try:
            item = self.editar_loja_controller.editar_loja_gerente(id_gerente=id_gerente, id_loja=id_loja, nova_loja=nova_loja)
            self.listar_loja_view.listar([item])

            return item
        except Exception as error:
            print(error);

    def excluir_loja(self, id_administrador: int, id_loja: int):
        try:
            item_excluido = self.excluir_loja_controller.excluir_loja(id_adm=id_administrador, id_loja=id_loja)

            self.listar_loja_view.listar([item_excluido])

            return item_excluido
        except Exception as error:
            print(error)


loja_facade = Lojafacade(administradorRepository=AdministradorRepositorio(),
                                                gerenteRepository=GerenteRepositorio(),)