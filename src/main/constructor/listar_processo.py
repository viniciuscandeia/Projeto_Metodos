"""
Módulo para o processo de listagem de itens.

Este módulo contém a função `listar_processo`, que solicita ao usuário o comando para listar
itens no sistema. A função utiliza a view `listar_view` para capturar a entrada do usuário e
retorna o comando selecionado para processamento adicional.

Funções:
- listar_processo: Solicita a entrada do usuário para listar itens e retorna o comando escolhido.
"""

from ...views.listar_views.listar_view import listar_view


def listar_processo():
    """
    Solicita a entrada do usuário para listar itens e retorna o comando escolhido.

    Esta função utiliza a view `listar_view` para obter o comando de listagem desejado pelo
    usuário e retorna esse comando para processamento adicional.

    :return: Comando escolhido pelo usuário para listar itens.
    :rtype: str
    """
    comando = listar_view()
    return comando
