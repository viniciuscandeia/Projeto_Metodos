from ....views.listar_views.listar_adm_view import ListarAdministradoresView
from ....controllers.administrador_controller import AdministradorController


def listar_adm_facade():

    listar_administrador_view = ListarAdministradoresView()
    adm_controller = AdministradorController()

    resposta: bool = adm_controller.listar()

    if resposta:
        listar_administrador_view.lista_preenchida()
    else:
        listar_administrador_view.lista_vazia()
