"""
Módulo que exibe o menu de listagem de usuários no sistema.

Contém a função `listar_view`, que apresenta as opções para listar diferentes
tipos de usuários e retorna o comando selecionado pelo usuário.
"""


def listar_view():
    """
    Exibe o menu de opções para listar usuários e retorna o comando selecionado pelo usuário.

    :return: Comando digitado pelo usuário.
    :rtype: str
    """

    mensagem = """
Listar Usuario

* Listar Administradores - 1
* Listar Gerentes - 2
* Listar Vendedores - 3
* Voltar - 9
    """

    print(mensagem)
    comando = input("Comando: ")

    return comando
