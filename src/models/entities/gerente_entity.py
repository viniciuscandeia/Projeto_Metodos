"""
Este módulo define a classe Gerente, que herda de Vendedor e
representa um gerente associado a uma loja.
"""

from .vendedor_entity import Vendedor


class Gerente(Vendedor):
    """
    Classe que representa um gerente no sistema.

    Herda da classe Vendedor e adiciona o ID da loja ao qual o gerente está associado,
    indicando a responsabilidade do gerente sobre operações específicas de uma loja.
    """
