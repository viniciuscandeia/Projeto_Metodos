"""
Módulo para o processo de listagem de vendedores.

Este módulo contém a função `listar_vendedor_constructor`, que coordena a listagem de vendedores
no sistema. A função cria instâncias da view e do controller responsáveis pela
exibição e verificação da lista de vendedores.

Funções:
- listar_vendedor_constructor: Cria as instâncias necessárias para listar vendedores e exibe a
  mensagem correspondente na interface do usuário.
"""

from ....controllers.listar_controller.listar_vendedor_controller import (
    ListarVendedoresController,
)
from ....views.listar_views.listar_vendedor_view import ListarVendedoresView


def listar_vendedor_constructor():
    """
    Função construtora para listar vendedores.

    Esta função cria as instâncias da view e do controller para listar os vendedores.
    Verifica se existem vendedores cadastrados e exibe uma mensagem correspondente
    na interface do usuário.

    Fluxo:
    - Verifica a existência de vendedores no repositório.
    - Exibe uma mensagem indicando se a lista de vendedores está vazia ou preenchida.
    """
    listar_vendedor_view = ListarVendedoresView()
    listar_vendedor_controller = ListarVendedoresController()

    resposta: bool = listar_vendedor_controller.listar()

    if resposta:
        listar_vendedor_view.lista_preenchida()
    else:
        listar_vendedor_view.lista_vazia()
