from src.lib.notificator_api import NotificatorApi
from src.models.entities.notification_entity import Notification
from src.models.repository.notification_repository import NotificationRepository
from src.models.repository.gerente_repository import GerenteRepositorio
from src.models.repository.administrador_repository import AdministradorRepositorio

class DatabaseAdapterNotificatorApi(NotificatorApi):
    def __init__(self, notification_repository:NotificationRepository) -> None:
        super().__init__()
        self.notification_repository = notification_repository

    
    def send(self, id_loja, id_adm, mensagem):
        try:
            notificacao = Notification(from_user_id=id_adm, to_loja_id=id_loja, mensagem=mensagem)
            self.notification_repository.send(notification=notificacao)
            notificacao
        except Exception as error:  
            print(f'Erro ao enviar notificacao: {error}')

    def receive(self, id_loja, id_usuario):
        try:
            listNotificationsFromDb = self.notification_repository.receive(id_loja=id_loja, id_usuario=id_usuario)
            listNotifications = []
 
            if listNotificationsFromDb:
                for notificationDb in listNotificationsFromDb:
                    listNotifications.append(Notification.fromDb(notificationDb))

            return listNotifications
        except Exception as error:
            print(f'Erro ao receber notificacoes: {error}')
        
database_adapter_notificator_api = DatabaseAdapterNotificatorApi(notification_repository=
                                                                 NotificationRepository(gerente_repositorio=GerenteRepositorio(), 
                                                                                        adm_repositorio=AdministradorRepositorio()))