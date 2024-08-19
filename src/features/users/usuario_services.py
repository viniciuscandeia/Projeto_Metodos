"""
Este módulo define a classe UsuarioService, que gerencia as listas de administradores,
vendedores e gerentes, e fornece métodos para adicionar e listar administradores.
"""

from src.features.users.entities.administrador_entity import Administrador


class UsuarioService:
    """
    Classe que fornece serviços para gerenciar administradores, vendedores e gerentes.

    Mantém listas internas de administradores, vendedores e gerentes e fornece métodos
    para adicionar e listar administradores.
    """

    def __init__(self):
        """
        Inicializa um novo objeto UsuarioService.

        Cria listas vazias para administradores, vendedores e gerentes.
        """
        self.administradores = []
        self.vendedores = []
        self.gerentes = []

    def adicionar_administrador(self, novo_administrador: Administrador):
        """
        Adiciona um novo administrador à lista de administradores.

        :param novo_administrador: Instância de Administrador a ser adicionada à lista.
        """
        self.administradores.append(novo_administrador)

    def listar_administradores(self):
        """
        Lista todos os administradores armazenados no sistema.

        :return: Lista de instâncias de Administrador.
        """
        return self.administradores
