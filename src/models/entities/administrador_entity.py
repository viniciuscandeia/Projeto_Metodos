"""
Este módulo define a classe Administrador, que herda de Usuario e
representa um administrador no sistema.
"""

<<<<<<<< HEAD:src/entities/administrador_entity.py
from src.entities.usuario_entity import Usuario
========
from .usuario_entity import Usuario
>>>>>>>> validar_campos:src/models/entities/administrador_entity.py


class Administrador(Usuario):
    """
    Classe que representa um administrador no sistema.

    Herda da classe Usuario e define permissões e comportamentos específicos
    para administradores, como acesso a funcionalidades de gerenciamento avançadas.
    """
