"""
Módulo que controla a adição de novos vendedores ao sistema.

Este módulo define a classe `AdicionarVendedorController`, responsável por validar,
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
from .adicionar_usuario_controller import AdicionarUsuarioController


class AdicionarVendedorController(AdicionarUsuarioController):
    """
    Controller para adicionar um novo vendedor.

    Esta classe herda de `AdicionarUsuarioController` e implementa o método abstrato
    necessário para criar uma entidade de vendedor e registrá-la no repositório.

    Métodos:
    - _criar_entidade: Cria uma entidade de vendedor e a registra no repositório.
    """

    def _criar_entidade(self, novo_vendedor: Dict) -> None:
        """
        Cria uma entidade de vendedor e a registra no repositório.

        Este método extrai os dados do novo vendedor do dicionário fornecido,
        cria uma instância da entidade `Vendedor` e a registra no repositório de vendedores.

        Args:
            novo_vendedor (Dict[str, str]): Um dicionário contendo os dados do novo vendedor,
            com as chaves "Nome", "Email", "Senha" e "Id_loja".

        Levanta:
            Exception: Se ocorrer um erro ao tentar registrar o vendedor no repositório.
        """

        nome: str = novo_vendedor["Nome"]
        email: str = novo_vendedor["Email"]
        senha: str = novo_vendedor["Senha"]
        _id_loja: str = novo_vendedor["Id_loja"]

        objeto_vendedor = Vendedor(nome, email, senha, _id_loja)

        try:
            vendedor_repositorio.registrar_vendedor(objeto_vendedor)
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None
