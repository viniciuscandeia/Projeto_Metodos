from src.models.entities.notification_entity import Notification
from src.views.listar_views.listar_view_interface import ListarView
from typing import List

class ListarNotificacoesView(ListarView):
    def listar(self, list:List[Notification]):
        if len(list) > 0:
            self._lista_preenchida(list=list)
            return

        self._lista_vazia()
        return

    def _lista_vazia(self) -> None:
        mensagem = """
Lista vazia de Notificacoes.
"""
        print(mensagem)

        return

    def _lista_preenchida(self, list:List[Notification]) -> None:
        mensagem = """
Notificações

"""
        lista_lojas = '\n'.join([f"\t - {notification.mensagem}" for notification in list])

        print(mensagem + lista_lojas)

        return
