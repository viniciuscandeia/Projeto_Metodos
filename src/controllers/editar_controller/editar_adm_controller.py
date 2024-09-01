from ..editar_controller.editar_usuario_controller import EditarUsuarioController
from ...models.repository.administrador_repository import adm_repositorio
from ...models.excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)
from typing import Dict

class EditarAdministradorController(EditarUsuarioController):
    def _editar_entidade(self, administrador_editado: Dict) -> None:
        try:
            adm_repositorio.editar_administrador(administrador_editado )
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None
