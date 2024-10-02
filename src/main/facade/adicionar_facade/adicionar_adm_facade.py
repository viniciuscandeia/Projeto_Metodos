
from ....controllers.administrador_controller import AdministradorController
from ....views.adicionar_views.adicionar_adm_view import AdicionarAdministradorView


def adicionar_adm_facade():

    adicionar_adm_view = AdicionarAdministradorView()
    adm_controller = AdministradorController()

    novo_administrador_informacoes = adicionar_adm_view.adicionar_administrador_view()
    resposta = adm_controller.adicionar(novo_administrador_informacoes)

    if resposta["Sucesso"]:
        adicionar_adm_view.adicionar_administrador_sucesso(
            resposta["Mensagem"])
    else:
        adicionar_adm_view.adicionar_administrador_falha(resposta["ERROR"])
