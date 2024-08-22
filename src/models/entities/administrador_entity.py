"""
Este módulo define a classe Administrador, que herda de Gerente e
representa um administrador no sistema.
"""

from src.models.entities.usuario_entity import Usuario


class Administrador(Usuario):
    """
    Classe que representa um administrador no sistema.

    Herda da classe Gerente.
    """
