from src.models.entities.notification_entity import Notification
from src.models.entities_db.notification_db_entity import NotificationDB
from src.models.excecoes import NotificacaoNaoEnviada, NotificacaoNaoRecebida, UsuarioNaoGerente, UsuarioNaoAdministrador
from src.models.repository.gerente_repository import GerenteRepositorio
from src.models.repository.administrador_repository import AdministradorRepositorio

class NotificationRepository():
    def __init__(self, gerente_repositorio:GerenteRepositorio, adm_repositorio: AdministradorRepositorio) -> None:
        self.gerente_repositorio = gerente_repositorio
        self.adm_repositorio = adm_repositorio

    def send(self, notification:Notification)->None:
        try:
            user_adm = self.adm_repositorio.get_one_administrador(id=notification.from_user_id)

            if not user_adm:
                raise UsuarioNaoAdministrador('Usuario não é admin ou nao existe')

            NotificationDB.create( mensagem=notification.mensagem,
                    from_user_id = notification.from_user_id,
                    to_loja_id = notification.to_loja_id)
        except Exception as e:
            raise NotificacaoNaoEnviada(f"Noficacao nao enviada: {e}")

    def receive(self, id_loja: int, id_usuario:int)->NotificationDB:
        try:
            user_gerente = self.gerente_repositorio.get_one_gerente(id=id_usuario)

            if not user_gerente or user_gerente.id_loja != id_loja:
                raise UsuarioNaoGerente(f'Usuario nao existe ou nao esta relacionado com a loja {id_loja}')

            return NotificationDB.select().where(NotificationDB.to_loja_id==id_loja)
        except Exception as e:
            raise NotificacaoNaoRecebida(f"Noficacoes nao recebidas: {e}")

