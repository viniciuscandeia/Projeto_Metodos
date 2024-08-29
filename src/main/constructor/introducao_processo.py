"""
Módulo para gerenciamento do processo de introdução do sistema.

Este módulo contém a função `introducao_processo`, que exibe a tela inicial do sistema para
o usuário e captura o comando escolhido. A função utiliza a view `tela_inicial` para apresentar
as opções iniciais e retorna o comando selecionado para determinar o próximo
passo no fluxo do programa.

Funções:
- introducao_processo: Exibe a tela inicial e retorna o comando escolhido pelo usuário.
"""

from ...views.tela_inicial import tela_inicial


def introducao_processo():
    """
    Exibe a tela inicial do sistema e retorna o comando escolhido pelo usuário.

    Esta função utiliza a view `tela_inicial` para apresentar as opções iniciais ao usuário
    e captura o comando selecionado para determinar o próximo passo no fluxo do programa.

    :return: Comando escolhido pelo usuário na tela inicial.
    :rtype: str
    """
    comando = tela_inicial()
    return comando
