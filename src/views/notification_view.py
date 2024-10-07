from src.models.entities.notification_entity import Notification

class NotificationsView:
    def listar_notificacoes_gerente_view(self):
        mensagem = """
        Listar Lojas

        * 1 - buscar notificacoes como gerente
        * Voltar - 9
            """

        print(mensagem)
        comando = input("Comando: ")

        return comando

    def listar(self, list: list[Notification]):
        if len(list) > 0:
            self._lista_preenchida(list=list)
            return

        self._lista_vazia()
        return

    def _lista_vazia(self) -> None:
        mensagem = """
Lista vazia de Notificacoes.
"""
        print(mensagem)

        return

    def _lista_preenchida(self, list: list[Notification]) -> None:
        mensagem = """
Notificações

"""
        lista_lojas = '\n'.join(
            [f"\t - {notification.mensagem}" for notification in list])

        print(mensagem + lista_lojas)

        return
