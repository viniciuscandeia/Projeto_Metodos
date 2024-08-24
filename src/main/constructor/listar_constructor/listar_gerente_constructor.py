"""
Módulo para o processo de listagem de gerentes.

Este módulo contém a função `listar_gerente_constructor`, que coordena a listagem de gerentes
no sistema. A função cria instâncias da view e do controller responsáveis
pela exibição e verificação da lista de gerentes.

Funções:
- listar_gerente_constructor: Cria as instâncias necessárias para listar gerentes e exibe a
  mensagem correspondente na interface do usuário.
"""

from ....controllers.listar_controller.listar_gerente_controller import ListarGerentesController
from ....views.listar_views.listar_gerente_view import ListarGerentesView


def listar_gerente_constructor():
    """
    Função construtora para listar gerentes.

    Esta função cria as instâncias da view e do controller para listar os gerentes.
    Verifica se existem gerentes cadastrados e exibe uma mensagem correspondente
    na interface do usuário.

    Fluxo:
    - Verifica a existência de gerentes no repositório.
    - Exibe uma mensagem indicando se a lista de gerentes está vazia ou preenchida.
    """
    listar_gerente_view = ListarGerentesView()
    listar_gerente_controller = ListarGerentesController()

    resposta: bool = listar_gerente_controller.listar()

    if resposta:
        listar_gerente_view.lista_preenchida()
    else:
        listar_gerente_view.lista_vazia()
