"""
Módulo que exibe a tela inicial do sistema cadastral.

Contém a função `tela_inicial` que apresenta o menu principal do sistema ao usuário e
retorna o comando selecionado.
"""



def tela_inicial():
    """
    Exibe a tela inicial do sistema cadastral e retorna o comando selecionado pelo usuário.

    :return: Comando digitado pelo usuário.
    :rtype: str
    """


    mensagem = """
Sistema Cadastral

1 - Cadastrar Usuario
2 - Listar Usuario
3 - Editar Usuario
4 - Adcionar Loja 
5 - Listar Lojas
6 - Editar Lojas
7 - Excluir Lojas
* Sair - 9
    """

    print(mensagem)
    comando = input("Comando: ")

    return comando
