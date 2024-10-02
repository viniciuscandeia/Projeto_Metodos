from ...models.excecoes import CampoInvalido

class ProcessoHelpers:  

    def __init__(self) -> None:
        pass

    def getIdLoja(self):
        try:
            mensagem = """
            Escolha Id de loja
                """

            print(mensagem)
            comando = input("Id loja: ")

            if len(comando) == 0:
                raise CampoInvalido("Valor inválido para campo Id Loja.")
            
            return comando
        except CampoInvalido as error:
            print(error)
    
    def getNomeLoja(self, lancarErroSeVazio = True):
        try:
            mensagem = """
            Digite o Nome da loja 
                """
            print(mensagem)
            nome = input("Nome: ")
            if len(nome) == 0 and lancarErroSeVazio:
                raise CampoInvalido("Valor inválido para campo Nome Loja.")
            return nome
        except CampoInvalido as error:
            raise Exception(error)

    def getEnderecoLoja(self, lancarErroSeVazio = True):
        try:
            mensagem = """
            Digite o Endereco da loja 
                """
            print(mensagem)
            nome = input("Nome: ")
            if len(nome) == 0 and lancarErroSeVazio:
                raise CampoInvalido("Valor inválido para campo Nome Loja.")
            return nome
        except CampoInvalido as error:
            raise Exception(error)


    def getIdUsuario(self):
        try:
            mensagem = """
            Escolha Id de usuario
                """

            print(mensagem)
            comando = input("Id usuario: ")

            if len(comando) == 0:
                raise CampoInvalido("Valor inválido para campo Id Usuário.")
            
            return comando
        except Exception as error:
            print(error)
        
    def getDataToEditLoja(self):
        new_loja = {}
        
        
        new_loja['Nome'] = self.getNomeLoja(False)
        new_loja['Endereco'] = self.getEnderecoLoja(False)
        return new_loja
        
    def getDataToCreateLoja(self):
        try: 
            new_loja = {}
            new_loja['Nome'] = self.getNomeLoja()
            new_loja['Endereco'] = self.getEnderecoLoja()
            return new_loja
        except Exception as error:
            print(error)


processo_helpers = ProcessoHelpers()