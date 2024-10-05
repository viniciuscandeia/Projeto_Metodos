from src.adapters.database_adapter_notificator_api import DatabaseAdapterNotificatorApi
from src.lib.notificator_api import NotificatorApi
from src.main.facade.notification_processo import ListarNotifications
from src.views.listar_views.listar_notifications_view import ListarNotificacoesView


class GerenteFacade:
    def __init__(self) -> None:
        super().__init__()

        self.notificator_api = DatabaseAdapterNotificatorApi()
        self.listar_notifications_view = ListarNotificacoesView()

    def get_notifications(self, id_loja:int, id_gerente:int):
        try:
            notifications = self.notificator_api.receive(id_loja=id_loja, id_usuario=id_gerente)

            if notifications and len(notifications) > 0:
                self.listar_notifications_view.listar(notifications)
        except Exception as e:
            print(e)

gerente_facade = GerenteFacade()