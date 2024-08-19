"""
Este módulo define a classe UsuarioController, que gerencia as operações
relacionadas a administradores, utilizando os serviços fornecidos por UsuarioService.
"""

from src.features.users.entities.administrador_entity import Administrador
from src.features.users.usuario_services import UsuarioService

class UsuarioController:
    """
    Classe que controla as operações relacionadas a administradores.

    Utiliza uma instância de UsuarioService para adicionar e listar administradores.
    """

    def __init__(self, service: UsuarioService):
        """
        Inicializa um novo objeto UsuarioController.

        :param service: Instância de UsuarioService utilizada para interagir com a camada
                        de serviços relacionada a administradores.
        """
        self.service = service

    def adicionar_administrador(self, novo_administrador: Administrador):
        """
        Adiciona um novo administrador ao sistema.

        :param novo_administrador: Instância de Administrador a ser adicionada.

        Nota: Futuramente será adicionada uma verificação para garantir que apenas administradores
              possam acessar este método.
        """
        self.service.adicionar_administrador(novo_administrador)

    def listar_administradores(self):
        """
        Lista todos os administradores cadastrados no sistema.

        :return: Lista de instâncias de Administrador.
        """
        return self.service.listar_administradores()
