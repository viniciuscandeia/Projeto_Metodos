from src.features.users.entities.administrador_entity import Administrador
from src.features.users.usuario_services import UsuarioService

class UsuarioController:
    def __init__(self, service: UsuarioService):
        self.service = service

    def adcionar_administrador(self, novoAdministrador:Administrador):
        #FUTURO: Adcionar verificação se o usuario que tenta acessar esse metodo é um administrador ou nao
        self.service.adcionar_administrador(novoAdministrador)

    def listar_administradores(self):
        return self.service.listar_administradores()
