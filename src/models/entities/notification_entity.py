from datetime import date
from src.models.entities_db.notification_db_entity import NotificationDB

class Notification:
    def __init__(self, mensagem:str,
                 from_user_id:int,
                 to_loja_id:int,
                 created_at = None
                 ) -> None:
        self.mensagem = mensagem
        self.from_user_id = from_user_id
        self.to_loja_id = to_loja_id
        self.created_at = created_at

    def fromDb(notificationDB:NotificationDB):
        return Notification(to_loja_id=notificationDB.to_loja_id,
                            from_user_id=notificationDB.from_user_id,
                            mensagem=notificationDB.mensagem,
                            created_at=notificationDB.created_at
                            )

    def __str__(self)->str:
        return f"[{self.created_at if self.created_at else 'Notificacao'}] Mensagem: {self.mensagem}, Usuário remetente: {self.from_user_id}, Loja Destino: {self.to_loja_id}"
