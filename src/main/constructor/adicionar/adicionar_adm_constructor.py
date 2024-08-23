from src.controllers.adicionar.adicionar_adm_controller import (
    AdicionarAdministradorController,
)
from src.views.adicionar.adicionar_adm_view import AdicionarAdministradorView


def adicionar_adm_constructor():
    adicionar_adm_view = AdicionarAdministradorView()
    adicionar_adm_controller = AdicionarAdministradorController()

    novo_administrador_informacoes = adicionar_adm_view.adicionar_administrador_view()
    resposta = adicionar_adm_controller.adicionar(novo_administrador_informacoes)

    if resposta["Sucesso"]:
        adicionar_adm_view.adicionar_administrador_sucesso(resposta["Mensagem"])
    else:
        adicionar_adm_view.adicionar_administrador_falha(resposta["ERROR"])
