"""
Este módulo define a classe Manager, que herda de Vendedor e
representa um gerente associado a uma loja.
"""

from src.models.entities.vendedor_entity import Vendedor


class Gerente(Vendedor):
    """
    Classe que representa um gerente no sistema.

    Herda da classe Vendedor e adiciona o ID da loja ao qual o gerente está associado.
    """

    def __init__(self, id_manager, nome, email, senha, id_loja):
        """
        Inicializa um novo objeto Manager.

        :param id_manager: ID do gerente.
        :param nome: Nome do gerente.
        :param email: Email do gerente.
        :param id_loja: ID da loja associada ao gerente.
        """
        super().__init__(id_manager, nome, email, senha, id_loja)
