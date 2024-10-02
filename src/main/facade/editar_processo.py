"""
Módulo para gerenciamento do processo de edição de itens.

Este módulo contém a função `editar_processo`, que solicita ao usuário a entrada
para editar um item existente no sistema. A função utiliza a view `editar_view`
para obter o comando desejado pelo usuário e retorna esse comando para processamento
adicional.

Funções:
- editar_processo: Solicita a entrada do usuário para editar um item existente e
retorna o comando escolhido.
"""

from ...views.editar_views.editar_view import editar_view
from ..facade.processo import Processo

def editar_processo():
    """
    Solicita a entrada do usuário para editar um item existente e retorna o comando escolhido.

    Esta função utiliza a view `editar_view` para obter o comando de edição desejado
    pelo usuário e retorna esse comando para processamento adicional.

    :return: Comando escolhido pelo usuário para editar um item.
    :rtype: str
    """
    comando = editar_view()
    return comando

class EditarProcessoLoja(Processo):
    def executar():
        mensagem = """
        Editar Loja

        * 1 - Editar Lojas como adm
        * 2 - Editar uma loja como gerente
        * 3 - Buscar uma loja como gerente
        * Voltar - 9
            """

        print(mensagem)
        comando = input("Comando: ")

        return comando

