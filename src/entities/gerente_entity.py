"""
Este módulo define a classe Manager, que herda de Usuario e
representa um gerente associado a uma loja.
"""

from src.entities.usuario_entity import Usuario


class Manager(Usuario):
    """
    Classe que representa um gerente no sistema.

    Herda da classe Usuario e adiciona o ID da loja ao qual o gerente está associado.
    """

    def __init__(self, id_adm, nome, email, id_loja):
        """
        Inicializa um novo objeto Manager.

        :param id_adm: ID do gerente.
        :param nome: Nome do gerente.
        :param email: Email do gerente.
        :param id_loja: ID da loja associada ao gerente.
        """
        super().__init__(id_adm, nome, email)
        self.id_loja = id_loja
