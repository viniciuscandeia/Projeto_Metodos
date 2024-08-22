def listar_view():
    mensagem = """
Listar Usuario

* Listar Administradores - 1
* Listar Gerentes - 2
* Listar Vendedores - 3
* Sair - 9
    """

    print(mensagem)
    comando = input("Comando: ")

    return comando
