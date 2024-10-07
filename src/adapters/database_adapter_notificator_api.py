from src.lib.notificator_api import NotificatorApi
from src.models.entities.notification_entity import Notification
from src.singletons.notification_repository_singleton import NotificationRepositorySingleton


class DatabaseAdapterNotificatorApi(NotificatorApi):
    def __init__(self) -> None:
        super().__init__()
        self.notification_repository = NotificationRepositorySingleton().getInstance()

    def send(self, id_loja: int, id_adm: int, mensagem: str):
        try:
            notificacao = Notification(
                from_user_id=id_adm, to_loja_id=id_loja, mensagem=mensagem)
            self.notification_repository.send(notification=notificacao)
            return notificacao
        except Exception as error:
            print(f'Erro ao enviar notificacao: {error}')

    def receive(self, id_loja, id_usuario):
        try:
            listNotificationsFromDb = self.notification_repository.receive(
                id_loja=id_loja, id_usuario=id_usuario)
            listNotifications = []

            if listNotificationsFromDb:
                for notificationDb in listNotificationsFromDb:
                    listNotifications.append(
                        Notification.fromDb(notificationDb))

            return listNotifications
        except Exception as error:
            print(f'Erro ao receber notificacoes: {error}')
