"""
Módulo para gerenciamento da adição de usuários.

Este módulo define a classe base `AdicionarUsuarioController` que fornece uma estrutura
para a adição de novos usuários em um sistema. Ele inclui métodos para validar campos
do usuário, criar entidades de usuários (que devem ser implementadas em subclasses) e
formatar a resposta após a adição do usuário.

Classes:
- AdicionarUsuarioController: Classe abstrata para adicionar novos usuários,
com métodos para validação e criação de entidades.

Dependências:
- abc: Para permitir a criação de classes abstratas.
- typing: Para suporte a tipos genéricos como Dict.
"""

from abc import ABC, abstractmethod
from typing import Dict


class AdicionarUsuarioController(ABC):
    """
    Classe base para adicionar um novo usuário.

    Esta classe define o esqueleto para adicionar novos usuários, fornecendo
    métodos para validar os dados de entrada,
    criar a entidade de usuário e formatar a resposta após a adição do usuário.

    Métodos:
    - adicionar: Adiciona um novo usuário após validar e criar a entidade.
    - __validar_campos: Valida os campos do usuário fornecido.
    - __validar_nome: Valida o campo 'Nome' do usuário.
    - __validar_email: Valida o campo 'Email' do usuário.
    - __validar_senha: Valida o campo 'Senha' do usuário.
    - __criar_entidade: Método abstrato para criar uma entidade de usuário.
    - __formatar_resposta: Formata a resposta de confirmação após a adição do usuário.
    """

    def adicionar(self, novo_usuario: Dict) -> Dict:
        """
        Adiciona um novo usuário após validar os campos e criar a entidade.

        Args:
            novo_usuario (Dict): Dicionário contendo os dados do novo usuário.

        Returns:
            Dict: Dicionário contendo o resultado da operação, indicando sucesso ou erro.
        """

        try:
            self.__validar_campos(novo_usuario)
            self._criar_entidade(novo_usuario)
            resposta = self.__formatar_resposta(novo_usuario)
            return {"Sucesso": True, "Mensagem": resposta}
        except ValueError as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_usuario: Dict) -> None:
        """
        Valida todos os campos do usuário fornecido.

        Args:
            novo_usuario (Dict): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se qualquer campo não for válido.
        """

        try:
            self.__validar_nome(novo_usuario)
            self.__validar_email(novo_usuario)
            self.__validar_senha(novo_usuario)
        except ValueError as erro:
            raise ValueError(str(erro)) from None

    def __validar_nome(self, novo_usuario: Dict) -> None:
        """
        Valida o campo 'Nome' do usuário.

        Args:
            novo_usuario (Dict): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se o nome estiver vazio ou não for uma string.
        """

        if not isinstance(novo_usuario["Nome"], str) or len(novo_usuario["Nome"]) == 0:
            raise ValueError("O campo 'Nome' esta vazio!")

    def __validar_email(self, novo_usuario: Dict) -> None:
        """
        Valida o campo 'Email' do usuário.

        Args:
            novo_usuario (Dict): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se o email estiver incorreto, contiver números ou
            exceder o limite de 12 caracteres.
        """

        if (
            not isinstance(novo_usuario["Email"], str)
            or len(novo_usuario["Email"]) == 0
            or len(novo_usuario["Email"]) > 12
        ):
            raise ValueError(
                "O campo 'Email' esta incorreto ou excede o limite de 12 caracteres!"
            )

        if any(char.isdigit() for char in novo_usuario["Email"]):
            raise ValueError("O campo 'Email' nao pode conter numeros!")

    def __validar_senha(self, novo_usuario: Dict) -> None:
        """
        Valida o campo 'Senha' do usuário.

        Args:
            novo_usuario (Dict): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se a senha não cumprir os requisitos de comprimento,
            letras maiúsculas, minúsculas, números e caracteres especiais.
        """

        senha = novo_usuario["Senha"]
        if len(senha) < 8 or len(senha) > 128:
            raise ValueError("O campo 'Senha' deve ter entre 8 e 128 caracteres!")
        if senha in novo_usuario["Nome"] or senha in novo_usuario["Email"]:
            raise ValueError(
                "O campo 'Senha' nao pode ser igual ao campo 'Nome' ou 'Email'!"
            )

        if not any(char.isupper() for char in senha):
            raise ValueError(
                "O campo 'Senha' deve conter ao menos uma letra maiuscula!"
            )
        if not any(char.islower() for char in senha):
            raise ValueError(
                "O campo 'Senha' deve conter ao menos uma letra minuscula!"
            )
        if not any(char.isdigit() for char in senha):
            raise ValueError("O campo 'Senha' deve conter ao menos um numero!")
        if not any(char in "!@#$%^&*()_+-=[]{}|" for char in senha):
            raise ValueError(
                "O campo 'Senha' deve conter ao menos um caractere especial!"
            )

    @abstractmethod
    def _criar_entidade(self, novo_usuario: Dict) -> None:
        """
        Método abstrato para criar uma entidade de usuário.

        Este método deve ser implementado por classes derivadas para definir a
        lógica de criação de entidades específicas.

        Args:
            novo_usuario (Dict): Dicionário contendo os dados do novo usuário.
        """

    def __formatar_resposta(self, novo_usuario: Dict) -> Dict:
        """
        Formata a resposta de confirmação após a adição do usuário.

        Args:
            novo_usuario (Dict): Dicionário contendo os dados do novo usuário.

        Returns:
            Dict: Dicionário formatado com o tipo de usuário, nome, email e ID.
        """

        return {
            "Tipo": self.__class__.__name__.replace("Adicionar", "").replace(
                "Controller", ""
            ),
            "Nome": novo_usuario["Nome"],
            "Email": novo_usuario["Email"],
            "Id": novo_usuario["Id"],
        }
