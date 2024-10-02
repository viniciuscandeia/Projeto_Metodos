from ....controllers.gerente_controller import GerenteController
from ....views.adicionar_views.adicionar_gerente_view import AdicionarGerenteView


def adicionar_gerente_facade():
    adicionar_gerente_view = AdicionarGerenteView()
    gerente_controller = GerenteController()

    novo_gerente_informacoes = adicionar_gerente_view.adicionar_gerente_view()
    resposta = gerente_controller.adicionar(novo_gerente_informacoes)

    if resposta["Sucesso"]:
        adicionar_gerente_view.adicionar_gerente_sucesso(resposta["Mensagem"])
    else:
        adicionar_gerente_view.adicionar_gerente_falha(resposta["ERROR"])
