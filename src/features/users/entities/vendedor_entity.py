from src.features.users.entities.usuario_entity import Usuario

class Vendedor(Usuario):
    def __init__(self, id_seller, name, email, id_store):
        super().__init__(id_seller, name, email)

        self.id_store = id_store

    
    def __str__(self):
        return super().__str__()