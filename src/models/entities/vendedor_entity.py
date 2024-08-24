"""
Este módulo define a classe Vendedor, que herda de Usuario e
representa um vendedor associado a uma loja.
"""

from .usuario_entity import Usuario


class Vendedor(Usuario):
    """
    Classe que representa um vendedor no sistema.

    Herda da classe Usuario e adiciona o ID da loja ao qual o vendedor está associado,
    indicando que o vendedor é responsável por operações dentro de uma loja específica.
    """

    def __init__(self, id_seller, name, email, senha, id_store):
        """
        Inicializa um novo objeto Vendedor.

        :param id_seller: ID do vendedor.
        :type id_seller: str
        :param name: Nome do vendedor.
        :type name: str
        :param email: Email do vendedor.
        :type email: str
        :param senha: Senha do vendedor.
        :type senha: str
        :param id_store: ID da loja associada ao vendedor.
        :type id_store: str
        """
        super().__init__(id_seller, name, email, senha)
        self.id_store = id_store
