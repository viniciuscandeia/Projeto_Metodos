from abc import ABC

class NotificatorApi(ABC):
    def __init__(self) -> None:
        pass

    def send(id_loja, id_adm, mensagem):
        pass
    def receive(id_loja, id_usuario):
        pass  