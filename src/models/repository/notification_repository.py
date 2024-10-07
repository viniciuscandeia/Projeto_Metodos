from src.models.entities.notification_entity import Notification
from src.models.entities_db.notification_db_entity import NotificationDB
from src.models.excecoes import NotificacaoNaoEnviada, NotificacaoNaoRecebida, UsuarioNaoGerente, UsuarioNaoAdministrador
from ...factory.persistencia_factory import PersistenciaFactory


class NotificationRepository():
    def __init__(self) -> None:
        self.gerente_repositorio = PersistenciaFactory.criar_persistencia(
            'gerente_db')
        self.adm_repositorio = PersistenciaFactory.criar_persistencia('adm_db')

    def send(self, notification: Notification) -> None:
        try:
            user_adm = self.adm_repositorio.get_one_administrador(
                notification.from_user_id)

            if not user_adm:
                raise UsuarioNaoAdministrador(
                    'Usuario não é admin ou nao existe')

            NotificationDB.create(mensagem=notification.mensagem,
                                  from_user_id=notification.from_user_id,
                                  to_loja_id=notification.to_loja_id)
        except Exception as e:
            raise NotificacaoNaoEnviada(
                f"Noficacao nao enviada: {e}") from None

    def receive(self, id_loja: int, id_usuario: int) -> NotificationDB:
        try:
            user_gerente = self.gerente_repositorio.get_one_gerente(id_usuario)

            if not user_gerente or user_gerente.id_loja != int(id_loja):
                raise UsuarioNaoGerente(
                    f'Usuario nao existe ou nao esta relacionado com a loja {id_loja}')

            return NotificationDB.select().where(NotificationDB.to_loja_id == id_loja)
        except Exception as e:
            raise NotificacaoNaoRecebida(
                f"Noficacoes nao recebidas: {e}") from None
