"""
Módulo que controla a adição de novos vendedores ao sistema.

Este módulo define a classe `AdicionarVendedorController`, responsável por validar, criar e
registrar novos vendedores no sistema.
"""

from typing import Dict

from ...models.entities.vendedor_entity import Vendedor
from ...models.repository.vendedor_repository import vendedor_repositorio
from .adicionar_usuario_controller import AdicionarUsuarioController


class AdicionarVendedorController(AdicionarUsuarioController):
    """
    Controller para adicionar um novo vendedor.

    Esta classe herda de AdicionarUsuarioController e implementa o método abstrato
    necessário para criar uma entidade de vendedor e registrá-la no repositório.

    Métodos:
    - _criar_entidade: Cria uma entidade de vendedor e a registra no repositório.
    """

    def _criar_entidade(self, novo_vendedor: Dict) -> None:
        """
        Cria uma entidade de vendedor e a registra no repositório.

        Parâmetros:
            novo_vendedor (Dict): Um dicionário contendo os dados do novo vendedor.
        """

        nome: str = novo_vendedor["Nome"]
        email: str = novo_vendedor["Email"]
        senha: str = novo_vendedor["Senha"]
        _id_loja: str = novo_vendedor["Id_loja"]

        objeto_vendedor = Vendedor(nome, email, senha, _id_loja)
        vendedor_repositorio.registrar_vendedor(objeto_vendedor)
