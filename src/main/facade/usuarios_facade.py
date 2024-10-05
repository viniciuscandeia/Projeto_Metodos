
from ...controllers.vendedor_controller import VendedorController
from ...controllers.gerente_controller import GerenteController
from ...controllers.administrador_controller import AdministradorController

from ...views.usuario_views import UsuarioViews
from ...models.repository.administrador_repository import adm_repositorio
from ...models.repository.gerente_repository import gerente_repositorio
from ...models.repository.vendedor_repository import vendedor_repositorio


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
            self.usuario_views.adicionar_usuario_sucesso(resposta["Mensagem"], 'Gerente')
        else:
            self.usuario_views.adicionar_usuario_falha(resposta["ERROR"])

    def adicionar_vendedor(self):

        novo_vendedor_informacoes = self.usuario_views.adicionar_vendedor_view()
        resposta = self.vendedor_controller.adicionar(novo_vendedor_informacoes)

        if resposta["Sucesso"]:
            self.usuario_views.adicionar_usuario_sucesso(resposta["Mensagem"], 'Vendedor')
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
            self.usuario_views.lista_preenchida(adm_repositorio, 'administrador')
        else:
            self.usuario_views.lista_vazia('administrador')

    def listar_gerente(self):

        resposta: bool = self.gerente_controller.listar()

        if resposta:
            self.usuario_views.lista_preenchida(gerente_repositorio, 'gerente')
        else:
            self.usuario_views.lista_vazia('gerente')

    def listar_vendedor(self):

        resposta: bool = self.vendedor_controller.listar()

        if resposta:
            self.usuario_views.lista_preenchida(vendedor_repositorio, 'vendedor')
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