from src.features.users.usuario_controller import UsuarioController
from src.features.users.usuario_services import UsuarioService
from src.features.users.boundaries.gerenciamento_administrador import GerenciamentoAdministradores

class UsuarioModule:
    def __init__(self):
            self.__usuario_service = UsuarioService()
            self.__controle_usuarios = UsuarioController(service=self.__usuario_service)
            self.__gerenciamentoAdministradores = GerenciamentoAdministradores(controller=self.__controle_usuarios)

    def mostrar_menu_gerenciamentoAdministradores(self):
            self.__gerenciamentoAdministradores.exibir_menu()



