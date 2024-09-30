from peewee import Model, CharField, AutoField, IntegerField, DateField
from datetime import date
from ..database import database_persistente

class NotificationDB(Model): 
    id = AutoField()
    mensagem = CharField()
    from_user_id = IntegerField()
    to_loja_id = IntegerField()
    created_at = DateField(default=date.today)

    class Meta:
        database = database_persistente

