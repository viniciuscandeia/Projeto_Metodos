"""
Este módulo define a classe Usuario, que representa um usuário com ID, nome, email e senha.
"""


class Usuario:
    """
    Classe que representa um usuário do sistema.

    Esta classe serve como base para diferentes tipos de usuários no sistema, armazenando
    informações comuns como ID, nome, email e senha.
    """

    def __init__(self, id_usuario, nome, email, senha):
        """
        Inicializa um novo objeto Usuario.

        :param id_usuario: ID do usuário.
        :type id_usuario: str
        :param nome: Nome do usuário.
        :type nome: str
        :param email: Email do usuário.
        :type email: str
        :param senha: Senha do usuário.
        :type senha: str
        """
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self) -> str:
        """
        Retorna uma string representando o objeto Usuario.

        :return: String formatada com ID, nome e email.
        :rtype: str
        """
        return f"ID: {self.id_usuario}, Nome: {self.nome}, Email: {self.email}"
