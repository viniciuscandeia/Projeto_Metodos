"""
Este módulo contém a função `adicionar_view`, que exibe um menu para a adição
de novos usuários ao sistema.

Funções:
- adicionar_view: Exibe o menu de cadastro e retorna o comando escolhido pelo usuário.

A função permite ao usuário escolher entre cadastrar um administrador, gerente, ou vendedor,
ou retornar ao menu anterior.
"""


def adicionar_view():
    """
    Exibe o menu para cadastrar um novo usuário e retorna o comando selecionado pelo usuário.

    :return: Comando digitado pelo usuário.
    :rtype: str
    """

    mensagem = """
Cadastrar Usuario

* Cadastrar Administrador - 1
* Cadastrar Gerente - 2
* Cadastrar Vendedor - 3
* Voltar - 9
    """

    print(mensagem)
    comando = input("Comando: ")

    return comando
