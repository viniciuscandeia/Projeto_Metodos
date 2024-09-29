"""
Módulo que controla a adição de novos vendedores ao sistema.

Este módulo define a classe `VendedorAdicaoController`, responsável por validar,
criar e registrar novos vendedores no sistema.
"""

from typing import Dict

from ...models.entities.vendedor_entity import Vendedor
from ...models.excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)
from ...models.repository.vendedor_repository import vendedor_repositorio
from .adicionar_usuario_controller import AbstractUsuarioAdicaoController


class VendedorAdicaoController(AbstractUsuarioAdicaoController):
    """
    Controller para adicionar um novo vendedor.

    Esta classe herda de `AbstractUsuarioAdicaoController` e implementa o método abstrato
    necessário para criar uma entidade de vendedor e registrá-la no repositório.

    Métodos:
    - _criar_entidade: Cria uma entidade de vendedor e a registra no repositório.
    """

    def _criar_entidade(self, novo_usuario: Dict) -> None:
        """
        Cria uma entidade de vendedor e a registra no repositório.

        Este método extrai os dados do novo vendedor do dicionário fornecido,
        cria uma instância da entidade `Vendedor` e a registra no repositório de vendedores.

        Args:
            novo_usuario (Dict[str, str]): Um dicionário contendo os dados do novo vendedor,
            com as chaves "Nome", "Email", "Senha" e "Id_loja".

        Levanta:
            Exception: Se ocorrer um erro ao tentar registrar o vendedor no repositório.
        """

        nome: str = novo_usuario["Nome"]
        username:str = novo_usuario['Username']
        email: str = novo_usuario["Email"]
        senha: str = novo_usuario["Senha"]
        _id_loja: str = novo_usuario["Id_loja"]

        objeto_vendedor = Vendedor(nome, username, email, senha, _id_loja)

        try:
            vendedor_repositorio.registrar_vendedor(objeto_vendedor)
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None
