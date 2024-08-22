from src.controllers.adicionar.adicionar_gerente_controller import (
    AdicionarGerenteController,
)
from src.views.adicionar.adicionar_gerente_view import AdicionarGerenteView


def adicionar_gerente_constructor():
    adicionar_gerente_view = AdicionarGerenteView()
    adicionar_gerente_controller = AdicionarGerenteController()

    novo_gerente_informacoes = adicionar_gerente_view.adicionar_gerente_view()
    resposta = adicionar_gerente_controller.adicionar(
        novo_gerente_informacoes)

    if resposta["Sucesso"]:
        adicionar_gerente_view.adicionar_gerente_sucesso(
            resposta["Mensagem"])
    else:
        adicionar_gerente_view.adicionar_gerente_falha(resposta["ERROR"])
