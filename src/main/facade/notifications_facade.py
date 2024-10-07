from ...views.notification_view import NotificationsView


class NotificationsFacade:

    def __init__(self):
        self.notifications_view = NotificationsView()

    def procurar_notificacoes_loja(self):
        comando = self.notifications_view.listar_notificacoes_gerente_view()
        return comando