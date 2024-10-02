"""
Módulo que controla a adição de novos administradores ao sistema.

Este módulo define a classe `AdicionarAdministradorController`, que é responsável por validar,
criar e registrar novos administradores no sistema.
"""

from typing import Dict

from ...models.entities.administrador_entity import Administrador
from ...models.excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)
from ...models.repository.administrador_repository import adm_repositorio
from .adicionar_usuario_controller import AdicionarUsuarioController


class AdicionarAdministradorController(AdicionarUsuarioController):

    def _criar_entidade(self, novo_usuario: Dict) -> None:
        nome: str = novo_usuario["Nome"]
        email: str = novo_usuario["Email"]
        senha: str = novo_usuario["Senha"]
        username: str = novo_usuario['Username']

        objeto_adm = Administrador(nome, username, email, senha)

        try:
            adm_repositorio.registrar_administrador(objeto_adm)
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None
