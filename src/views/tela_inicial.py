def tela_inicial():
    mensagem = """
Sistema Cadastral

* Cadastrar Usuario - 1
* Listar Usuario - 2
* Sair - 9

    """

    print(mensagem)
    comando = input("Comando: ")

    return comando
