from src.controllers.listar.listar_adm_controller import ListarAdministradoresController
from src.views.listar.listar_adm_view import ListarAdministradoresView


def listar_adm_constructor():
    listar_administrador_view = ListarAdministradoresView()
    listar_administrador_controller = ListarAdministradoresController()

    resposta: bool = listar_administrador_controller.listar()

    if resposta:
        listar_administrador_view.lista_preenchida()
    else:
        listar_administrador_view.lista_vazia()
