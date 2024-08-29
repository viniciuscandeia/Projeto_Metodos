"""
Módulo que controla a adição de novos administradores ao sistema.

Este módulo define a classe `AdicionarAdministradorController`, que é responsável por validar,
criar e registrar novos administradores no sistema.
"""

from typing import Dict

from ...models.entities.administrador_entity import Administrador
from ...models.exceptions import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)
from ...models.repository.administrador_repository import adm_repositorio
from .adicionar_usuario_controller import AdicionarUsuarioController


class AdicionarAdministradorController(AdicionarUsuarioController):
    """
    Controller para adicionar um novo administrador.

    Esta classe herda de `AdicionarUsuarioController` e implementa o método abstrato
    necessário para criar uma entidade de administrador e registrá-la no repositório.

    Métodos:
    - `_criar_entidade`: Cria uma entidade de administrador e a registra no repositório.
    """

    def _criar_entidade(self, novo_administrador: Dict) -> None:
        """
        Cria uma entidade de administrador e a registra no repositório.

        Este método extrai os dados do novo administrador do dicionário fornecido,
        cria uma instância da entidade `Administrador` e a registra no repositório
        de administradores.

        Parâmetros:
            novo_administrador (Dict[str, str]): Um dicionário contendo os dados do
            novo administrador,
            com as chaves "Nome", "Email" e "Senha".

        Levanta:
            Exception: Se ocorrer um erro ao tentar registrar o administrador no repositório.
        """

        nome: str = novo_administrador["Nome"]
        email: str = novo_administrador["Email"]
        senha: str = novo_administrador["Senha"]

        objeto_adm = Administrador(nome, email, senha)

        try:
            adm_repositorio.registrar_administrador(objeto_adm)
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None
