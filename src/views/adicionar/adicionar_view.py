def adicionar_view():
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
