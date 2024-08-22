from src.controllers.listar.listar_vendedor_controller import ListarVendedoresController
from src.views.listar.listar_vendedor_view import ListarVendedoresView


def listar_vendedor_constructor():
    listar_vendedor_view = ListarVendedoresView()
    listar_vendedor_controller = ListarVendedoresController()

    resposta: bool = listar_vendedor_controller.listar()

    if resposta:
        listar_vendedor_view.lista_preenchida()
    else:
        listar_vendedor_view.lista_vazia()
