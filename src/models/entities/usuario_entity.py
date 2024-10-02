"""
Este módulo define a classe Usuario, que representa um usuário com nome, username, email e senha.
"""


class Usuario:

    def __init__(self, nome, username, email, senha):
        """
        Inicializa um novo objeto Usuario.

        :param nome: Nome do usuário.
        :type nome: str
        :param username: Username do usuário.
        :type username: str
        :param email: Email do usuário.
        :type email: str
        :param senha: Senha do usuário.
        :type senha: str
        """
        self.nome = nome
        self.username = username
        self.email = email
        self.senha = senha

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Email: {self.email}"
