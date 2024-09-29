"""
Módulo para o processo de listagem de administradores.

Este módulo contém a função `listar_adm_constructor`, que coordena a listagem de administradores
no sistema. A função cria instâncias da view e do controller responsáveis pela exibição
e verificação da lista de administradores.

Funções:
- listar_adm_constructor: Cria as instâncias necessárias para listar administradores e exibe a
  mensagem correspondente na interface do usuário.
"""

from ....controllers.listar_controller.listar_adm_controller import (
    AdministradoresListController,
)
from ....views.listar_views.listar_adm_view import AdministradoresListagemView


def listar_adm_constructor():
    """
    Função construtora para listar administradores.

    Esta função cria as instâncias da view e do controller para listar os administradores.
    Verifica se existem administradores cadastrados e exibe uma mensagem correspondente
    na interface do usuário.

    Fluxo:
    - Verifica a existência de administradores no repositório.
    - Exibe uma mensagem indicando se a lista de administradores está vazia ou preenchida.
    """
    listar_administrador_view = AdministradoresListagemView()
    listar_administrador_controller = AdministradoresListController()

    resposta: bool = listar_administrador_controller.listar()

    if resposta:
        listar_administrador_view.lista_preenchida()
    else:
        listar_administrador_view.lista_vazia()
