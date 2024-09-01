"""
Este módulo serve como ponto de entrada para a execução do sistema.

Ele importa e executa a função 'start' do módulo 'process_handle'.
"""
from src.models.entities.usuario_db_entity import UsuarioBD

from src.main.process_handle import start
if __name__ == "__main__":
    start()
    # items:list[UsuarioBD] = UsuarioBD.select()

    # # Iterate through the results and print the ID and other fields
    # for item in items:
    #     print(item.nome)
    #     print(f'ID: {item.id}')