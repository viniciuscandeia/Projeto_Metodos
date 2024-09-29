"""
Módulo para gerenciamento da adição de usuários.

Este módulo define a classe base `AbstractUsuarioAdicaoController`, que fornece uma estrutura
para a adição de novos usuários em um sistema. Ele inclui métodos para validar campos
do usuário, criar entidades de usuários (que devem ser implementadas em subclasses) e
formatar a resposta após a adição do usuário.

Classes:
- AbstractUsuarioAdicaoController: Classe abstrata para adicionar novos usuários,
com métodos para validação e criação de entidades.

Dependências:
- abc: Para permitir a criação de classes abstratas.
- typing: Para suporte a tipos genéricos como Dict.
"""

from abc import ABC, abstractmethod
from typing import Dict
from ...lib.validar_inputs import ValidadorInputs


class AbstractUsuarioAdicaoController(ABC):
    """
    Classe base para adicionar um novo usuário.

    Esta classe define o esqueleto para adicionar novos usuários, fornecendo
    métodos para validar os dados de entrada, criar a entidade de usuário e formatar
    a resposta após a adição do usuário.

    Métodos:
    - adicionar: Adiciona um novo usuário após validar e criar a entidade.
    - __validar_campos: Valida os campos do usuário fornecido.
    - __validar_nome: Valida o campo 'Nome' do usuário.
    - __validar_email: Valida o campo 'Email' do usuário.
    - __validar_senha: Valida o campo 'Senha' do usuário.
    - _criar_entidade: Método abstrato para criar uma entidade de usuário.
    - __formatar_resposta: Formata a resposta de confirmação após a adição do usuário.
    """

    def adicionar(self, novo_usuario: Dict) -> Dict:
        """
        Adiciona um novo usuário após validar os campos e criar a entidade.

        Este método valida os dados do usuário, cria a entidade correspondente e
        retorna um dicionário com o resultado da operação, indicando sucesso ou erro.

        Args:
            novo_usuario (Dict[str, str]): Dicionário contendo os dados do novo usuário.

        Returns:
            Dict[str, str]: Dicionário contendo o resultado da operação, com campos
            "Sucesso" e "Mensagem" indicando o status da adição.
        """

        try:
            self.__validar_campos(novo_usuario)
            self._criar_entidade(novo_usuario)
            resposta = self.__formatar_resposta(novo_usuario)

            return {"Sucesso": True, "Mensagem": resposta}
        except ValueError as erro:
            return {"Sucesso": False, "ERROR": str(erro)}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_usuario: Dict) -> None:
        """
        Valida todos os campos do usuário fornecido.

        Este método verifica se os campos 'Nome', 'Email' e 'Senha' estão corretos e
        seguem as regras definidas.

        Args:
            novo_usuario (Dict[str, str]): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se qualquer campo não for válido.
        """
        try:
            ValidadorInputs.validar_nome(novo_usuario)
            ValidadorInputs.validar_email(novo_usuario)
            ValidadorInputs.validar_senha(novo_usuario)
            ValidadorInputs.validar_username(novo_usuario)
        except ValueError as erro:
            raise ValueError(str(erro)) from None

    @abstractmethod
    def _criar_entidade(self, novo_usuario: Dict) -> None:
        """
        Método abstrato para criar uma entidade de usuário.

        Este método deve ser implementado por classes derivadas para definir a
        lógica de criação de entidades específicas.

        Args:
            novo_usuario (Dict[str, str]): Dicionário contendo os dados do novo usuário.
        """

    def __formatar_resposta(self, novo_usuario: Dict) -> Dict:
        """
        Formata a resposta de confirmação após a adição do usuário.

        Este método cria um dicionário formatado com o tipo de usuário, nome e email.

        Args:
            novo_usuario (Dict[str, str]): Dicionário contendo os dados do novo usuário.

        Returns:
            Dict[str, str]: Dicionário formatado com o tipo de usuário, nome e email.
        """

        return {
            "Tipo": self.__class__.__name__.replace("Adicionar", "").replace(
                "Controller", ""
            ),
            "Nome": novo_usuario["Nome"],
            "Username": novo_usuario["Username"],
            "Email": novo_usuario["Email"],
        }
