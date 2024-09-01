"""
Este módulo contém a função construtora para adicionar um novo administrador.
"""

from ....controllers.editar_controller.editar_adm_controller import (
    EditarAdministradorController,
)
from ....views.editar_views.editar_adm_view import EditarAdmView


def editar_adm_constructor():
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
    editar_adm_view = EditarAdmView()
    editar_adm_controller = EditarAdministradorController()

    novo_administrador_informacoes = editar_adm_view.editar_administrador_view()
    resposta = editar_adm_controller.editar(novo_administrador_informacoes)

    if resposta["Sucesso"]:
        editar_adm_view.editar_administrador_sucesso()
    else:
        editar_adm_view.editar_administrador_falha(resposta["ERROR"])
