from src.lib.notificator_api import NotificatorApi
from src.models.entities.notification_entity import Notification
from src.models.repository.gerente_repository import GerenteRepositorio
from src.models.repository.administrador_repository import AdministradorRepositorio
from src.models.excecoes import UsuarioNaoGerente, UsuarioNaoAdministrador
from src.singletons.adm_repository_singleton import AdmRepositorySingleton
from src.singletons.gerente_repository_singleton import GerenteRepositorySingleton


class FirebaseAdapterNotificatorApi(NotificatorApi):
    def __init__(self) -> None:
        super().__init__()
        self.notifications = []
        self.gerente_repositorio = GerenteRepositorySingleton().getInstance(),
        self.adm_repositorio = AdmRepositorySingleton().getInstance()

    def send(self, id_loja, id_adm, mensagem):
        try:
            user_adm = self.adm_repositorio.get_one_administrador(id_adm)

            if not user_adm:
                raise UsuarioNaoAdministrador('Usuario não existe ou nao é administrador')
 
            print("Enviando notificação através do firebase")
            notification = Notification(to_loja_id=id_loja, from_user_id=id_adm, mensagem=mensagem)
            print(notification)
            self.notifications.append(notification)
        except Exception as e:
            print(e)
        
    def receive(self, id_loja: int, id_usuario:int):
        try:
            user_gerente = self.gerente_repositorio.get_one_gerente(id_usuario)
            
            if not user_gerente or user_gerente.id_loja != id_loja:
                raise UsuarioNaoGerente(f'Usuario nao existe ou nao esta relacionado com a loja {id_loja}')

            return filter(lambda notification: notification.to_loja_id == id_loja, self.notifications)
        except Exception as e:
             print(e)

firebase_adapter_notificator_api = FirebaseAdapterNotificatorApi()