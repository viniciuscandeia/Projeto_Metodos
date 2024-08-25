"""
Este módulo define a classe Vendedor, que herda de Usuario e
representa um vendedor associado a uma loja.
"""

<<<<<<<< HEAD:src/entities/vendedor_entity.py
from src.entities.usuario_entity import Usuario
========
from .usuario_entity import Usuario

>>>>>>>> validar_campos:src/models/entities/vendedor_entity.py

class Vendedor(Usuario):
    """
    Classe que representa um vendedor no sistema.

    Herda da classe Usuario e adiciona o ID da loja ao qual o vendedor está associado,
    indicando que o vendedor é responsável por operações dentro de uma loja específica.
    """

<<<<<<<< HEAD:src/entities/vendedor_entity.py
    def __init__(self, id_seller, name, email, id_loja):
========
    def __init__(self, id_seller, name, email, senha, id_store):
>>>>>>>> validar_campos:src/models/entities/vendedor_entity.py
        """
        Inicializa um novo objeto Vendedor.

        :param id_seller: ID do vendedor.
        :type id_seller: str
        :param name: Nome do vendedor.
        :type name: str
        :param email: Email do vendedor.
<<<<<<<< HEAD:src/entities/vendedor_entity.py
        :param id_loja: ID da loja associada ao vendedor.
        """
        super().__init__(id_seller, name, email)
        self.id_loja = id_loja
========
        :type email: str
        :param senha: Senha do vendedor.
        :type senha: str
        :param id_store: ID da loja associada ao vendedor.
        :type id_store: str
        """
        super().__init__(id_seller, name, email, senha)
        self.id_store = id_store
>>>>>>>> validar_campos:src/models/entities/vendedor_entity.py
