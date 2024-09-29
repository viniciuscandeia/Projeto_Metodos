"""
Este módulo contém a função construtora para adicionar um novo vendedor.
"""

from ....controllers.adicionar_controller.adicionar_vendedor_controller import (
    VendedorAdicaoController,
)
from ....views.adicionar_views.adicionar_vendedor_view import AdicaoVendedorView


def adicionar_vendedor_constructor():
    """
    Função construtora para adicionar um novo vendedor.

    Esta função cria as instâncias da view e do controller para adicionar um vendedor.
    Solicita as informações do novo vendedor, tenta adicioná-lo e exibe o resultado
    na interface do usuário.

    Fluxo:
    - Solicita informações do novo vendedor através da view.
    - Tenta adicionar o novo vendedor utilizando o controller.
    - Exibe uma mensagem de sucesso ou falha com base no resultado.
    """
    adicionar_vendedor_view = AdicaoVendedorView()
    adicionar_vendedor_controller = VendedorAdicaoController()

    novo_vendedor_informacoes = adicionar_vendedor_view.adicionar_vendedor_view()
    resposta = adicionar_vendedor_controller.adicionar(novo_vendedor_informacoes)

    if resposta["Sucesso"]:
        adicionar_vendedor_view.adicionar_vendedor_sucesso(resposta["Mensagem"])
    else:
        adicionar_vendedor_view.adicionar_vendedor_falha(resposta["ERROR"])
