
from ..entities.usuario_entity import Usuario
from abc import ABC, abstractmethod

class UsuarioRepository(ABC):

    @abstractmethod
    def registrar_usuario(self, usuario: Usuario) -> None:
        pass

    @abstractmethod
    def remover_usuario(self, _id: str) -> None:
        pass

    @abstractmethod
    def pegar_repositorio(self) -> list[Usuario]:
        pass

    @abstractmethod
    def get_one_usuario(self, id: int):
        pass
