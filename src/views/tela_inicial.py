"""
Módulo que exibe a tela inicial do sistema cadastral.

Contém a função `tela_inicial` que apresenta o menu principal do sistema ao usuário e
retorna o comando selecionado.
"""

import os


def tela_inicial():
    """
    Exibe a tela inicial do sistema cadastral e retorna o comando selecionado pelo usuário.

    :return: Comando digitado pelo usuário.
    :rtype: str
    """

    os.system("cls||clear")

    mensagem = """
Sistema Cadastral

* Cadastrar Usuario - 1
* Listar Usuario - 2
* Sair - 9
    """

    print(mensagem)
    comando = input("Comando: ")

    return comando
