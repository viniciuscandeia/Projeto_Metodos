
# * main

from src.features.users.user_controller import ControleUsuarios
from src.features.users.user_services import InterfaceUsuarios

controle_usuarios = ControleUsuarios()
interface_usuarios = InterfaceUsuarios(controle_usuarios)

interface_usuarios.exibir_menu()
