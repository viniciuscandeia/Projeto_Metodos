from ...views.listar_views.listar_vendedor_view import ListarVendedoresView
from ...views.listar_views.listar_gerente_view import ListarGerentesView
from ...views.listar_views.listar_adm_view import ListarAdministradoresView
from ...views.editar_views.editar_adm_view import EditarAdmView
from ...views.adicionar_views.adicionar_vendedor_view import AdicionarVendedorView
from ...controllers.vendedor_controller import VendedorController
from ...controllers.gerente_controller import GerenteController
from ...views.adicionar_views.adicionar_gerente_view import AdicionarGerenteView
from ...controllers.administrador_controller import AdministradorController
from ...views.adicionar_views.adicionar_adm_view import AdicionarAdministradorView


class UsuariosFacade:

    def adicionar_administrador():

        adicionar_adm_view = AdicionarAdministradorView()
        adm_controller = AdministradorController()

        novo_administrador_informacoes = adicionar_adm_view.adicionar_administrador_view()
        resposta = adm_controller.adicionar(novo_administrador_informacoes)

        if resposta["Sucesso"]:
            adicionar_adm_view.adicionar_administrador_sucesso(
                resposta["Mensagem"])
        else:
            adicionar_adm_view.adicionar_administrador_falha(resposta["ERROR"])

    def adicionar_gerente():
        adicionar_gerente_view = AdicionarGerenteView()
        gerente_controller = GerenteController()

        novo_gerente_informacoes = adicionar_gerente_view.adicionar_gerente_view()
        resposta = gerente_controller.adicionar(novo_gerente_informacoes)

        if resposta["Sucesso"]:
            adicionar_gerente_view.adicionar_gerente_sucesso(
                resposta["Mensagem"])
        else:
            adicionar_gerente_view.adicionar_gerente_falha(resposta["ERROR"])

    def adicionar_vendedor():
        adicionar_vendedor_view = AdicionarVendedorView()
        vendedor_controller = VendedorController()

        novo_vendedor_informacoes = adicionar_vendedor_view.adicionar_vendedor_view()
        resposta = vendedor_controller.adicionar(novo_vendedor_informacoes)

        if resposta["Sucesso"]:
            adicionar_vendedor_view.adicionar_vendedor_sucesso(
                resposta["Mensagem"])
        else:
            adicionar_vendedor_view.adicionar_vendedor_falha(resposta["ERROR"])

    def editar_administrador():
        editar_adm_view = EditarAdmView()
        adm_controller = AdministradorController()

        novo_administrador_informacoes = editar_adm_view.editar_administrador_view()
        resposta = adm_controller.editar(novo_administrador_informacoes)

        if resposta["Sucesso"]:
            editar_adm_view.editar_administrador_sucesso()
        else:
            editar_adm_view.editar_administrador_falha(resposta["ERROR"])

    def listar_administrador():

        listar_administrador_view = ListarAdministradoresView()
        adm_controller = AdministradorController()

        resposta: bool = adm_controller.listar()

        if resposta:
            listar_administrador_view.lista_preenchida()
        else:
            listar_administrador_view.lista_vazia()

    def listar_gerente():
        listar_gerente_view = ListarGerentesView()
        gerente_controller = GerenteController()

        resposta: bool = gerente_controller.listar()

        if resposta:
            listar_gerente_view.lista_preenchida()
        else:
            listar_gerente_view.lista_vazia()

    def listar_vendedor():
        listar_vendedor_view = ListarVendedoresView()
        vendedor_controller = VendedorController()

        resposta: bool = vendedor_controller.listar()

        if resposta:
            listar_vendedor_view.lista_preenchida()
        else:
            listar_vendedor_view.lista_vazia()
