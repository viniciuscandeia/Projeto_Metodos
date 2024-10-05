from abc import ABC

class NotificatorApi(ABC):
    def __init__(self) -> None:
        pass

    def send(id_loja:int, id_adm:int, mensagem:str):
        print('Enviando notificação')
        pass
    def receive(id_loja, id_usuario):
        print('Recebendo notificações')
        pass