"""
Módulo que controla a adição de novos administradores ao sistema.

Este módulo define a classe `AdicionarAdministradorController`, que é responsável por validar,
criar e registrar novos administradores no sistema.
"""

from typing import Dict

from ...models.entities.administrador_entity import Administrador
from ...models.repository.administrador_repository import adm_repositorio
from .adicionar_usuario_controller import AdicionarUsuarioController


class AdicionarAdministradorController(AdicionarUsuarioController):
    """
    Controller para adicionar um novo administrador.

    Esta classe herda de AdicionarUsuarioController e implementa o método abstrato
    necessário para criar uma entidade de administrador e registrá-la no repositório.

    Métodos:
    - _criar_entidade: Cria uma entidade de administrador e a registra no repositório.
    """

    def _criar_entidade(self, novo_administrador: Dict) -> None:
        """
        Cria uma entidade de administrador e a registra no repositório.

        Parâmetros:
            novo_administrador (Dict): Um dicionário contendo os dados do novo administrador.
        """

        nome: str = novo_administrador["Nome"]
        email: str = novo_administrador["Email"]
        _id: str = novo_administrador["Id"]
        senha: str = novo_administrador["Senha"]

        objeto_adm = Administrador(_id, nome, email, senha)
        adm_repositorio.registrar_administrador(objeto_adm)
