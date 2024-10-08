"""
Este módulo define a classe Administrador, que herda de Usuario e
representa um administrador no sistema.
"""

from .usuario_entity import Usuario


class Administrador(Usuario):
    """
    Classe que representa um administrador no sistema.

    Herda da classe Usuario e define permissões e comportamentos específicos
    para administradores, como acesso a funcionalidades de gerenciamento avançadas.
    """
