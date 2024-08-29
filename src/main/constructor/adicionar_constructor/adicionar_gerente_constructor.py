"""
Este módulo contém a função construtora para adicionar um novo gerente.
"""

from ....controllers.adicionar_controller.adicionar_gerente_controller import (
    AdicionarGerenteController,
)
from ....views.adicionar_views.adicionar_gerente_view import AdicionarGerenteView


def adicionar_gerente_constructor():
    """
    Função construtora para adicionar um novo gerente.

    Esta função cria as instâncias da view e do controller para adicionar um gerente.
    Solicita as informações do novo gerente, tenta adicioná-lo e exibe o resultado
    na interface do usuário.

    Fluxo:
    - Solicita informações do novo gerente através da view.
    - Tenta adicionar o novo gerente utilizando o controller.
    - Exibe uma mensagem de sucesso ou falha com base no resultado.
    """
    adicionar_gerente_view = AdicionarGerenteView()
    adicionar_gerente_controller = AdicionarGerenteController()

    novo_gerente_informacoes = adicionar_gerente_view.adicionar_gerente_view()
    resposta = adicionar_gerente_controller.adicionar(novo_gerente_informacoes)

    if resposta["Sucesso"]:
        adicionar_gerente_view.adicionar_gerente_sucesso(resposta["Mensagem"])
    else:
        adicionar_gerente_view.adicionar_gerente_falha(resposta["ERROR"])
