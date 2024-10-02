from ....views.listar_views.listar_gerente_view import ListarGerentesView
from ....controllers.gerente_controller import GerenteController

def listar_gerente_facade():
    listar_gerente_view = ListarGerentesView()
    gerente_controller = GerenteController()

    resposta: bool = gerente_controller.listar()

    if resposta:
        listar_gerente_view.lista_preenchida()
    else:
        listar_gerente_view.lista_vazia()
