from ....views.editar_views.editar_adm_view import EditarAdmView
from ....controllers.administrador_controller import AdministradorController


def editar_adm_facade():
    editar_adm_view = EditarAdmView()
    adm_controller = AdministradorController()

    novo_administrador_informacoes = editar_adm_view.editar_administrador_view()
    resposta = adm_controller.editar(novo_administrador_informacoes)

    if resposta["Sucesso"]:
        editar_adm_view.editar_administrador_sucesso()
    else:
        editar_adm_view.editar_administrador_falha(resposta["ERROR"])
