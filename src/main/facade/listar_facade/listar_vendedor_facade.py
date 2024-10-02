from ....views.listar_views.listar_vendedor_view import ListarVendedoresView
from ....controllers.vendedor_controller import VendedorController


def listar_vendedor_facade():
    listar_vendedor_view = ListarVendedoresView()
    vendedor_controller = VendedorController()

    resposta: bool = vendedor_controller.listar()

    if resposta:
        listar_vendedor_view.lista_preenchida()
    else:
        listar_vendedor_view.lista_vazia()
