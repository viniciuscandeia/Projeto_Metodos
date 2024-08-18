from src.features.users.entities.administrador_entity import Administrador

class UsuarioService:
    def __init__(self):
        self.administradores = []
        self.vendedores = []
        self.gerentes = []

    def adcionar_administrador(self, novoAdministrador:Administrador):
        self.administradores.append(novoAdministrador)
    
    def listar_administradores(self):
        return self.administradores
    

