"""
Este módulo contém a função construtora para adicionar um novo administrador.
"""


from ....controllers.adicionar_controller.adicionar_adm_controller import (
    AdicionarAdministradorController,
)
from ....views.adicionar_views.adicionar_adm_view import AdicionarAdministradorView


def adicionar_adm_constructor():
    """
    Função construtora para adicionar um novo administrador.

    Esta função cria as instâncias da view e do controller para adicionar um administrador.
    Solicita as informações do novo administrador, tenta adicioná-lo e exibe o resultado
    na interface do usuário.

    Fluxo:
    - Solicita informações do novo administrador através da view.
    - Tenta adicionar o novo administrador utilizando o controller.
    - Exibe uma mensagem de sucesso ou falha com base no resultado.
    """
    adicionar_adm_view = AdicionarAdministradorView()
    adicionar_adm_controller = AdicionarAdministradorController()

    novo_administrador_informacoes = adicionar_adm_view.adicionar_administrador_view()
    resposta = adicionar_adm_controller.adicionar(
        novo_administrador_informacoes)

    if resposta["Sucesso"]:
        adicionar_adm_view.adicionar_administrador_sucesso(
            resposta["Mensagem"])
    else:
        adicionar_adm_view.adicionar_administrador_falha(resposta["ERROR"])
