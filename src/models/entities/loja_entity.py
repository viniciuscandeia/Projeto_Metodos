class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    
    def __str__(self)->str:
        return f"Nome: {self.nome}, Endereco: {self.endereco}"
