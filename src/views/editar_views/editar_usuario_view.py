
def editar_usuario_view():
    mensagem = """
Editar Usuario

* Editar Administradores - 1
* Editar Gerentes - 2
* Editar Vendedores - 3
* Voltar - 9
    """

    print(mensagem)
    comando = input("Comando: ")

    return comando
