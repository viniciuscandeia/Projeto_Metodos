class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def __str__(self):
        return f'ID: {self.id_usuario}, Nome: {self.nome}, Email: {self.email}'
