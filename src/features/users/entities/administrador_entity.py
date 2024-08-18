from src.features.users.entities.usuario_entity import Usuario

class Administrador(Usuario):
    def __init__(self, id_adm, name, email):
        super().__init__(id_adm, name, email)


    def __str__(self):
        return super().__str__()