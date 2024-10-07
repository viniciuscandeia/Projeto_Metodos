
from ...controllers.vendedor_controller import VendedorController
from ...controllers.gerente_controller import GerenteController
from ...controllers.administrador_controller import AdministradorController

from ...views.usuario_views import UsuarioViews

from ...factory.persistencia_factory import PersistenciaFactory

from ...adapters.database_adapter_notificator_api import DatabaseAdapterNotificatorApi
from ...lib.notificator_api import NotificatorApi
from ...views.notification_view import NotificationsView

class UsuariosFacade:

    def __init__(self):
        self.usuario_views: UsuarioViews = UsuarioViews()
        self.adm_controller: AdministradorController = AdministradorController()
        self.gerente_controller: GerenteController = GerenteController()
        self.vendedor_controller: VendedorController = VendedorController()

    def escolher_usuario_adicionar_usuario(self):
        comando = self.usuario_views.escolher_usuario_adicionar_view()
        return comando

    def adicionar_administrador(self):

        novo_administrador_informacoes = self.usuario_views.adicionar_administrador_view()
        resposta = self.adm_controller.adicionar(
            novo_administrador_informacoes)

        if resposta["Sucesso"]:
            self.usuario_views.adicionar_usuario_sucesso(
                resposta['Mensagem'], 'Administrador')
        else:
            self.usuario_views.adicionar_usuario_falha(
                resposta['ERROR'], 'Administrador')

    def adicionar_gerente(self):

        novo_gerente_informacoes = self.usuario_views.adicionar_gerente_view()
        resposta = self.gerente_controller.adicionar(novo_gerente_informacoes)

        if resposta["Sucesso"]:
            self.usuario_views.adicionar_usuario_sucesso(
                resposta["Mensagem"], 'Gerente')
        else:
            self.usuario_views.adicionar_usuario_falha(resposta["ERROR"])

    def adicionar_vendedor(self):

        novo_vendedor_informacoes = self.usuario_views.adicionar_vendedor_view()
        resposta = self.vendedor_controller.adicionar(
            novo_vendedor_informacoes)

        if resposta["Sucesso"]:
            self.usuario_views.adicionar_usuario_sucesso(
                resposta["Mensagem"], 'Vendedor')
        else:
            self.usuario_views.adicionar_usuario_falha(resposta["ERROR"])

    def editar_administrador(self):

        novo_administrador_informacoes = self.usuario_views.editar_administrador_view()
        resposta = self.adm_controller.editar(novo_administrador_informacoes)

        if resposta["Sucesso"]:
            self.usuario_views.editar_administrador_sucesso()
        else:
            self.usuario_views.editar_administrador_falha(resposta["ERROR"])

    def listar_administrador(self):

        resposta: bool = self.adm_controller.listar()

        if resposta:
            self.usuario_views.lista_preenchida(
                PersistenciaFactory.criar_persistencia('adm_db'), 'administrador')
        else:
            self.usuario_views.lista_vazia('administrador')

    def listar_gerente(self):

        resposta: bool = self.gerente_controller.listar()

        if resposta:
            self.usuario_views.lista_preenchida(
                PersistenciaFactory.criar_persistencia('gerente_db'), 'gerente')
        else:
            self.usuario_views.lista_vazia('gerente')

    def listar_vendedor(self):

        resposta: bool = self.vendedor_controller.listar()

        if resposta:
            self.usuario_views.lista_preenchida(
                PersistenciaFactory.criar_persistencia('vendedor_db'), 'vendedor')
        else:
            self.usuario_views.lista_vazia('vendedor')

    def selecionar_usuario_listar_loja(self):
        comando = self.usuario_views.selecionar_usuario_listar_loja_view()
        return comando

    def selecionar_usuario_edicao_loja(self):
        comando = self.usuario_views.selecionar_usuario_edicao_loja_view()
        return comando

    def selecionar_usuario_edicao_usuario(self):
        comando = self.usuario_views.selecionar_usuario_editar_usuario_view()
        return comando

    def selecionar_usuario_excluir_loja(self):
        comando = self.selecionar_usuario_excluir_loja()
        return comando

    def adm_gerar_relatorio(self):
        try:
            self.adm_controller.enviar_relatorio()
        except Exception as e:
            print(e)

    def gerente_gerar_relatorio(self):
        try:
            self.gerente_controller.enviar_relatorio()
        except Exception as e:
            print(e)

    def vendedor_gerar_relatorio(self):
        try:
            self.vendedor_controller.enviar_relatorio()
        except Exception as e:
            print(e)

    def gerente_receber_notificacao(self, id_loja: int, id_gerente: int):
        self.notificator_api = DatabaseAdapterNotificatorApi()
        try:
            notifications = self.notificator_api.receive(
                id_loja=id_loja, id_usuario=id_gerente)

            if notifications and len(notifications) > 0:
                NotificationsView().listar(notifications)
        except Exception as e:
            print(e)
