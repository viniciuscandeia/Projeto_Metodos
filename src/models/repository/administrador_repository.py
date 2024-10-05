from typing import List

from peewee import DoesNotExist, IntegrityError

from ..entities.administrador_entity import Administrador
from ..entities_db.usuario_db_entity import UsuarioBD
from ..excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)


class AdministradorRepositorio:
    def __init__(self) -> None:
        pass

    def registrar_administrador(self, administrador: Administrador) -> None:
        try:
            UsuarioBD.create(
                nome=administrador.nome,
                email=administrador.email,
                senha=administrador.senha,
                username=administrador.username,
                user_type="ADMINISTRADOR",
            )
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise UsuarioIntegridadeError(f'Erro ao registrar administrador: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise UsuarioRegistroError(f"Erro inesperado ao registrar administrador: { str(e)}") from None

    def editar_administrador(self, novo_administrador:dict) -> None:
        try:
            administrador = UsuarioBD.get(UsuarioBD.id == int(novo_administrador.get('id')))
            update_data = {
                'nome': novo_administrador.get('Nome') if novo_administrador.get('Nome') else administrador.nome,
                'email': novo_administrador.get('Email') if novo_administrador.get('Email') else administrador.email,
                'username':novo_administrador.get('Username') if novo_administrador.get('Username') else administrador.username,
            }

        # Remover chaves com valor None (ou não fornecidas)
            update_data = {k: v for k, v in update_data.items() if v is not None}
            UsuarioBD.update(**update_data).where(UsuarioBD.id == administrador.id).execute()
            return update_data
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise UsuarioIntegridadeError(f'Erro ao editar administrador: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise UsuarioRegistroError(f"Erro inesperado ao editar administrador: { str(e)}") from None

    def remover_administrador(self, _id: str) -> None:
        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            raise UsuarioNaoEncontrado(f"Administrador com ID {_id} não encontrado.") from None
        except Exception as e:
            raise UsuarioErroInesperado(f"Erro inesperado ao remover administrador: {str(e)}") from None

    def pegar_repositorio(self) -> List[UsuarioBD]:
        try:
            lista_administradores = UsuarioBD.select().where(UsuarioBD.user_type == "ADMINISTRADOR")
        except Exception as e:
            # Captura qualquer exceção ao acessar o banco de dados
            print(f"Erro ao acessar o repositório de administradores: {str(e)}")
            return []
        return lista_administradores

    def get_one_administrador(self, _id:int) -> UsuarioBD:
        try:
            administrador = UsuarioBD.get(UsuarioBD.id == _id,
                                                             UsuarioBD.user_type == "ADMINISTRADOR",)
        except UsuarioBD.DoesNotExist:
            print(f"Administrador com ID {_id} não encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao acessar o repositório de administradores: {str(e)}")
            return None
        return administrador


adm_repositorio = AdministradorRepositorio()
