"""
Módulo para gerenciamento do processo de adição de novos itens.

Este módulo contém a função `adicionar_processo`, que solicita ao usuário a entrada
para adicionar um novo item ao sistema. A função utiliza a view `adicionar_view`
para obter o comando desejado pelo usuário e retorna esse comando para processamento
adicional.

Funções:
- adicionar_processo: Solicita a entrada do usuário para adicionar um novo item e
retorna o comando escolhido.
"""

from ...views.adicionar_views.adicionar_view import adicionar_view


def adicionar_processo():
    """
    Solicita a entrada do usuário para adicionar um novo item e retorna o comando escolhido.

    Esta função utiliza a view `adicionar_view` para obter o comando de adição desejado
    pelo usuário e retorna esse comando para processamento adicional.

    :return: Comando escolhido pelo usuário para adicionar um item.
    :rtype: str
    """
    comando = adicionar_view()
    return comando

    