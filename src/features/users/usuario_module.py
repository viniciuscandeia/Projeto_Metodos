"""
Este módulo define a classe UsuarioModule, que integra os componentes relacionados
à gestão de usuários, incluindo serviços, controladores e interfaces de gerenciamento
de administradores.
"""

from src.features.users.usuario_controller import UsuarioController
from src.features.users.usuario_services import UsuarioService
from src.features.users.boundaries.gerenciamento_administrador import GerenciamentoAdministradores


class UsuarioModule:
    """
    Classe que encapsula os componentes do módulo de usuários.

    Esta classe cria instâncias dos serviços, controladores e interfaces necessárias para
    gerenciar usuários e administradores no sistema.
    """

    def __init__(self):
        """
        Inicializa um novo objeto UsuarioModule.

        Cria instâncias de UsuarioService, UsuarioController, e GerenciamentoAdministradores,
        integrando-os para o gerenciamento de usuários e administradores.
        """
        self.__usuario_service = UsuarioService()
        self.__controle_usuarios = UsuarioController(
            service=self.__usuario_service)
        self.__gerenciamento_administradores = GerenciamentoAdministradores(
            controller=self.__controle_usuarios)

    def mostrar_menu_gerenciamento_administradores(self):
        """
        Exibe o menu de gerenciamento de administradores.

        Utiliza a instância de GerenciamentoAdministradores para exibir o menu relacionado ao
        gerenciamento de administradores.
        """
        self.__gerenciamento_administradores.exibir_menu()
