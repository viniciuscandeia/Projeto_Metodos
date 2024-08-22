from src.controllers.adicionar.adicionar_vendedor_controller import (
    AdicionarVendedorController,
)
from src.views.adicionar.adicionar_vendedor_view import AdicionarVendedorView


def adicionar_vendedor_constructor():
    adicionar_vendedor_view = AdicionarVendedorView()
    adicionar_vendedor_controller = AdicionarVendedorController()

    novo_vendedor_informacoes = adicionar_vendedor_view.adicionar_vendedor_view()
    resposta = adicionar_vendedor_controller.adicionar(
        novo_vendedor_informacoes)

    if resposta["Sucesso"]:
        adicionar_vendedor_view.adicionar_vendedor_sucesso(
            resposta["Mensagem"])
    else:
        adicionar_vendedor_view.adicionar_vendedor_falha(
            resposta["ERROR"])
