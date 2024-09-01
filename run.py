"""
Este módulo serve como ponto de entrada para a execução do sistema.

Ele importa e executa a função 'start' do módulo 'process_handle'.
"""
from src.models.entities.usuario_db_entity import UsuarioBD
from src.controllers.editar_controller.editar_adm_controller import EditarAdministradorController
from src.main.process_handle import start
if __name__ == "__main__":
    start()
    # editar_adm_controller = EditarAdministradorController()
    # editar_adm_controller.editar({"id": 2, "Nome": "testizn"})