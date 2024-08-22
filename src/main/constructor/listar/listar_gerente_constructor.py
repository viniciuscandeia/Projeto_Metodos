from src.controllers.listar.listar_gerente_controller import ListarGerentesController
from src.views.listar.listar_gerente_view import ListarGerentesView


def listar_gerente_constructor():
    listar_gerente_view = ListarGerentesView()
    listar_gerente_controller = ListarGerentesController()

    resposta: bool = listar_gerente_controller.listar()

    if resposta:
        listar_gerente_view.lista_preenchida()
    else:
        listar_gerente_view.lista_vazia()
