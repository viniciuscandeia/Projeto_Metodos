
def editar_loja_view():
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
