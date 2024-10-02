from ....views.adicionar_views.adicionar_vendedor_view import AdicionarVendedorView
from ....controllers.vendedor_controller import VendedorController


def adicionar_vendedor_facade():
    adicionar_vendedor_view = AdicionarVendedorView()
    vendedor_controller = VendedorController()

    novo_vendedor_informacoes = adicionar_vendedor_view.adicionar_vendedor_view()
    resposta = vendedor_controller.adicionar(novo_vendedor_informacoes)

    if resposta["Sucesso"]:
        adicionar_vendedor_view.adicionar_vendedor_sucesso(
            resposta["Mensagem"])
    else:
        adicionar_vendedor_view.adicionar_vendedor_falha(resposta["ERROR"])
