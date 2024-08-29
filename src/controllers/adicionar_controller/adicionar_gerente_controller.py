"""
Módulo para controle de adição de novos gerentes ao sistema.

Este módulo contém a classe `AdicionarGerenteController`, responsável por validar
os dados de um novo gerente, criar a entidade gerente e registrá-la no repositório.
"""

from typing import Dict

from ...models.entities.gerente_entity import Gerente
from ...models.exceptions import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)
from ...models.repository.gerente_repository import gerente_repositorio
from .adicionar_usuario_controller import AdicionarUsuarioController


class AdicionarGerenteController(AdicionarUsuarioController):
    """
    Controller para adicionar um novo gerente.

    Esta classe herda de `AdicionarUsuarioController` e implementa o método abstrato
    necessário para criar uma entidade de gerente e registrá-la no repositório.

    Métodos:
    - `_criar_entidade`: Cria uma entidade de gerente e a registra no repositório.
    """

    def _criar_entidade(self, novo_gerente: Dict) -> None:
        """
        Cria uma entidade de gerente e a registra no repositório.

        Este método extrai os dados do novo gerente do dicionário fornecido,
        cria uma instância da entidade `Gerente` e a registra no repositório de gerentes.

        Parâmetros:
            novo_gerente (Dict[str, str]): Um dicionário contendo os dados do novo gerente,
            com as chaves "Nome", "Email", "Senha" e "Id_loja".

        Levanta:
            Exception: Se ocorrer um erro ao tentar registrar o gerente no repositório.
        """

        nome: str = novo_gerente["Nome"]
        email: str = novo_gerente["Email"]
        senha: str = novo_gerente["Senha"]
        _id_loja: str = novo_gerente["Id_loja"]

        objeto_gerente = Gerente(nome, email, senha, _id_loja)

        try:
            gerente_repositorio.registrar_gerente(objeto_gerente)
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None
