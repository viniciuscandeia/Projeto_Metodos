"""
Módulo para controle de adição de novos gerentes ao sistema.

Este módulo contém a classe `AdicionarGerenteController`, responsável por validar
os dados de um novo gerente, criar a entidade gerente e registrá-la no repositório.
"""

from typing import Dict

from ...models.entities.gerente_entity import Gerente
from ...models.repository.gerente_repository import gerente_repositorio
from .adicionar_usuario_controller import AdicionarUsuarioController


class AdicionarGerenteController(AdicionarUsuarioController):
    """
    Controller para adicionar um novo gerente.

    Esta classe herda de AdicionarUsuarioController e implementa o método abstrato
    necessário para criar uma entidade de gerente e registrá-la no repositório.

    Métodos:
    - _criar_entidade: Cria uma entidade de gerente e a registra no repositório.
    """

    def _criar_entidade(self, novo_gerente: Dict) -> None:
        """
        Cria uma entidade de gerente e a registra no repositório.

        Parâmetros:
            novo_gerente (Dict): Um dicionário contendo os dados do novo gerente.
        """

        nome: str = novo_gerente["Nome"]
        email: str = novo_gerente["Email"]
        _id: str = novo_gerente["Id"]
        senha: str = novo_gerente["Senha"]
        _id_loja: str = novo_gerente["Id_loja"]

        objeto_gerente = Gerente(_id, nome, email, senha, _id_loja)
        gerente_repositorio.registrar_gerente(objeto_gerente)
