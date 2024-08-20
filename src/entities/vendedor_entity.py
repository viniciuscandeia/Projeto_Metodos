"""
Este módulo define a classe Vendedor, que herda de Usuario e
representa um vendedor associado a uma loja.
"""

from src.entities.usuario_entity import Usuario

class Vendedor(Usuario):
    """
    Classe que representa um vendedor no sistema.

    Herda da classe Usuario e adiciona o ID da loja ao qual o vendedor está associado.
    """

    def __init__(self, id_seller, name, email, id_store):
        """
        Inicializa um novo objeto Vendedor.

        :param id_seller: ID do vendedor.
        :param name: Nome do vendedor.
        :param email: Email do vendedor.
        :param id_store: ID da loja associada ao vendedor.
        """
        super().__init__(id_seller, name, email)
        self.id_store = id_store
