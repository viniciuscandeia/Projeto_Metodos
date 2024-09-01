from .database import database_memoria
from .entities.usuario_db_entity import UsuarioBD

def inicializar_database(usar_memoria:bool):
    if(usar_memoria):
        UsuarioBD._meta.database = database_memoria

    UsuarioBD._meta.database.connect()
    UsuarioBD._meta.database.create_tables([UsuarioBD])