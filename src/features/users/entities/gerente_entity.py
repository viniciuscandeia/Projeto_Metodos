from src.features.users.entities.usuario_entity import Usuario

class Manager(Usuario):
    def __init__(self, id_adm, nome, email, id_loja):
        super().__init__(id_adm, nome, email)

        self.id_loja = id_loja

    def __str__(self):
        return super().__str__()