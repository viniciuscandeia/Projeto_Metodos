"""
Módulo que define o repositório para gerenciar objetos do tipo Gerente.

Este módulo contém a classe `GerenteRepositorio`, que oferece métodos
para registrar, remover e acessar instâncias de `Gerente`.
"""

from peewee import DoesNotExist, IntegrityError

from ..entities.usuario_entity import Usuario
from ..entities_db.usuario_db_entity import UsuarioBD
from ..excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)
from .usuario_repository import UsuarioRepository


class GerenteRepositorio(UsuarioRepository):
    def registrar_usuario(self, usuario: Usuario) -> None:
        try:
            UsuarioBD.create(
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                user_type="GERENTE",
                username=usuario.username,
            )
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise UsuarioIntegridadeError(
                f"Erro ao registrar usuario: {str(e)}") from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise UsuarioRegistroError(
                f"Erro inesperado ao registrar gerente: {str(e)}") from None

    def remover_usuario(self, _id: str) -> None:
        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            raise UsuarioNaoEncontrado(
                f"Gerente com ID {_id} não encontrado.") from None
        except Exception as e:
            raise UsuarioErroInesperado(
                f"Erro inesperado ao remover gerente: {str(e)}") from None

    def pegar_repositorio(self) -> list[Usuario]:
        """
        Retorna a lista atual de gerentes no repositório.

        Este método consulta o banco de dados e retorna uma lista de objetos `Gerente`
        que representam os gerentes armazenados no repositório.

        Returns:
            List[Gerente]: Lista de objetos `Gerente`.

        Levanta:
            Exception: Se ocorrer um erro ao acessar o banco de dados.
        """

        try:
            lista_gerentes = UsuarioBD.select().where(UsuarioBD.user_type == "GERENTE")
        except Exception as e:
            # Captura qualquer exceção ao acessar o banco de dados
            print(f"Erro ao acessar o repositório de gerentes: {str(e)}")
            return []
        return lista_gerentes

    def get_one_usuario(self, _id: int):
        try:
            usuario = UsuarioBD.get(UsuarioBD.id == _id,
                                    UsuarioBD.user_type == "GERENTE",)
        except UsuarioBD.DoesNotExist:
            print(f"Gerente com ID {_id} não encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao acessar o repositório de Gerentes: {str(e)}")
            return None
        return usuario

gerente_repositorio = GerenteRepositorio()
