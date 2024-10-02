from src.lib.notificator_api import NotificatorApi
from src.models.entities.notification_entity import Notification
from src.models.repository.gerente_repository import GerenteRepositorio
from src.models.repository.administrador_repository import AdministradorRepositorio
from src.models.excecoes import UsuarioNaoGerente, UsuarioNaoAdministrador

class FirebaseAdapterNotificatorApi(NotificatorApi):
    def __init__(self, gerente_repositorio:GerenteRepositorio, adm_repositorio: AdministradorRepositorio) -> None:
        super().__init__()
        self.notifications = []
        self.gerente_repositorio = gerente_repositorio
        self.adm_repositorio = adm_repositorio

    def send(self, id_loja, id_adm, mensagem):
        try:
            user_adm = self.adm_repositorio.get_one_administrador(id=id_adm)

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
            user_gerente = self.gerente_repositorio.get_one_gerente(id=id_usuario)
            
            if not user_gerente or user_gerente.id_loja != id_loja:
                raise UsuarioNaoGerente(f'Usuario nao existe ou nao esta relacionado com a loja {id_loja}')

            return filter(lambda notification: notification.to_loja_id == id_loja, self.notifications)
        except Exception as e:
             print(e)

#TODO: Da pra criar um singleton pros repositorios
firebase_adapter_notificator_api = FirebaseAdapterNotificatorApi(gerente_repositorio=GerenteRepositorio(), adm_repositorio=AdministradorRepositorio())