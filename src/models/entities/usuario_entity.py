"""
Este módulo define a classe Usuario, que representa um usuário com nome, email e senha.
"""


class Usuario:
    """
    Classe que representa um usuário do sistema.

    Esta classe serve como base para diferentes tipos de usuários no sistema, armazenando
    informações comuns como nome, email e senha.
    """

    def __init__(self, nome, username, email, senha,):
        """
        Inicializa um novo objeto Usuario.

        :param nome: Nome do usuário.
        :type nome: str
        :param email: Email do usuário.
        :type email: str
        :param senha: Senha do usuário.
        :type senha: str
        """
        self.nome = nome
        self.email = email
        self.senha = senha
        self.username = username

    def __str__(self) -> str:
        """
        Retorna uma string representando o objeto Usuario.

        :return: String formatada com nome e email.
        :rtype: str
        """
        return f"Nome: {self.nome}, Email: {self.email}"
