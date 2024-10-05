from src.main.facade.processo import Processo


class ListarNotifications(Processo):
    def executar(self):
        mensagem = """
        Listar Lojas

        * 1 - buscar notificacoes como gerente
        * Voltar - 9
            """

        print(mensagem)
        comando = input("Comando: ")

        return comando

