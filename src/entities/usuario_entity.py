"""
Este módulo define a classe Usuario, que representa um usuário com ID, nome e email.
"""

class Usuario:
    """
    Classe que representa um usuário do sistema.
    """

    def __init__(self, id_usuario, nome, email):
        """
        Inicializa um novo objeto Usuario.

        :param id_usuario: ID do usuário.
        :param nome: Nome do usuário.
        :param email: Email do usuário.
        """
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def __str__(self):
        """
        Retorna uma string representando o objeto Usuario.

        :return: String formatada com ID, nome e email.
        """
        return f'ID: {self.id_usuario}, Nome: {self.nome}, Email: {self.email}'
