from typing import Dict
import re


class ValidadorInputs:
    @classmethod
    def validar_nome(cls, novo_usuario: Dict) -> None:
        """
        Valida o campo 'Nome' do usuário.

        Este método verifica se o nome é uma string não vazia.

        Args:
            novo_usuario (Dict[str, str]): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se o nome estiver vazio ou não for uma string.
        """

        if not isinstance(novo_usuario["Nome"], str) or len(novo_usuario["Nome"]) == 0:
            raise ValueError("O campo 'Nome' esta vazio!")

    @classmethod
    def validar_id(cls, novo_usuario: Dict) -> None:
        if 'id' not in novo_usuario:
            raise ValueError("O campo 'id' esta vazio!")

    @classmethod
    def validar_username(cls, novo_usuario: Dict) -> None:

        if not isinstance(novo_usuario["Username"], str) or len(novo_usuario["Username"]) == 0:
            raise ValueError("O campo 'username' esta vazio!")

        if (len(novo_usuario['Username']) > 12):
            raise ValueError("O campo 'username' tem mais de 12 caracteres")

    @classmethod
    def validar_email(cls, novo_usuario: Dict) -> None:
        """
        Valida o campo 'Email' do usuário.

        Este método verifica se o email é uma string, não está vazio, não contém números
        e não excede o limite de 12 caracteres.

        Args:
            novo_usuario (Dict[str, str]): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se o email estiver incorreto, contiver números ou exceder o limite
            de 12 caracteres.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if (
            not isinstance(novo_usuario["Email"], str)
            or len(novo_usuario["Email"]) == 0
        ):
            raise ValueError(
                "O campo 'Email' esta vazio"
            )

        if (not re.match(email_regex, novo_usuario['Email'])):
            raise ValueError(
                "O campo 'Email' nao é um email"
            )
    
    @classmethod
    def validar_senha(cls, novo_usuario: Dict) -> None:
        """
        Valida o campo 'Senha' do usuário.

        Este método verifica se a senha atende aos requisitos de comprimento, contém letras
        maiúsculas e minúsculas, números e caracteres especiais, e não é igual ao nome
        ou email.

        Args:
            novo_usuario (Dict[str, str]): Dicionário contendo os dados do novo usuário.

        Raises:
            ValueError: Se a senha não cumprir os requisitos de comprimento, letras maiúsculas,
            minúsculas, números e caracteres especiais.
        """

        senha = novo_usuario["Senha"]
        if len(senha) < 8 or len(senha) > 128:
            raise ValueError(
                "O campo 'Senha' deve ter entre 8 e 128 caracteres!")
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
