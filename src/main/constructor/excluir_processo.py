from .processo import Processo

class ProcessoExclusaoLoja(Processo):
    def executar():
        mensagem = """
        Excluir Loja

        * Excluir Loja como administrador - 1
        * Voltar - 9 """

        print(mensagem)

        comando = input('Comando: ')
        return comando