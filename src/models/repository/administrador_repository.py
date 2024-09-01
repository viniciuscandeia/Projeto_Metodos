"""
Módulo que define o repositório para gerenciar objetos do tipo Administrador.

Este módulo contém a classe `AdministradorRepositorio`, que oferece métodos
para registrar, remover e acessar instâncias de `Administrador`.
"""

from typing import List

from peewee import DoesNotExist, IntegrityError

from ..entities.administrador_entity import Administrador
from ..entities.usuario_db_entity import UsuarioBD
from ..excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)


class AdministradorRepositorio:
    """
    Classe que gerencia o repositório de administradores.

    Esta classe oferece métodos para registrar, remover e acessar administradores
    dentro do sistema.

    Métodos:
    - registrar_administrador: Registra um novo administrador no repositório.
    - remover_administrador: Remove um administrador do repositório com base no ID fornecido.
    - pegar_repositorio: Retorna a lista atual de administradores no repositório.
    """

    def __init__(self) -> None:
        """
        Inicializa um novo repositório de administradores.
        """

    def registrar_administrador(self, administrador: Administrador) -> None:
        """
        Registra um novo administrador no repositório.

        Este método cria uma nova entrada na base de dados para o administrador
        fornecido. Se ocorrer um erro de integridade ou outro erro inesperado,
        uma exceção será lançada.

        Args:
            administrador (Administrador): Objeto do tipo `Administrador` a ser adicionado.

        Levanta:
            Exception: Se ocorrer um erro de integridade ao registrar o administrador
            ou um erro inesperado.
        """

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
        
    def editar_administrador(self, novoAdministrador:dict) -> None:
        try:
                administrador = UsuarioBD.get(UsuarioBD.id == int(novoAdministrador.get('id')))
                update_data = { 
                    'nome': novoAdministrador.get('Nome') if novoAdministrador.get('Nome') else administrador.nome,
                    'email': novoAdministrador.get('Email') if novoAdministrador.get('Email') else administrador.email,
                    'username':novoAdministrador.get('Username') if novoAdministrador.get('Username') else administrador.username,
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
        """
        Remove um administrador do repositório com base no ID fornecido.

        Este método tenta encontrar o administrador pelo ID e, se encontrado,
        remove-o do repositório. Se o administrador não for encontrado ou ocorrer
        um erro inesperado, uma exceção será lançada.

        Args:
            _id (str): ID do administrador a ser removido.

        Levanta:
            Exception: Se o administrador com o ID fornecido não for encontrado
            ou se ocorrer um erro inesperado ao remover o administrador.
        """

        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            raise UsuarioNaoEncontrado(f"Administrador com ID {_id} não encontrado.") from None
        except Exception as e:
            raise UsuarioErroInesperado(f"Erro inesperado ao remover administrador: {str(e)}") from None

    def pegar_repositorio(self) -> List[UsuarioBD]:
        """
        Retorna a lista atual de administradores no repositório.

        Este método consulta o banco de dados e retorna uma lista de objetos `Administrador`
        que representam os administradores armazenados no repositório.

        Returns:
            List[Administrador]: Lista de objetos `Administrador`.

        Levanta:
            Exception: Se ocorrer um erro ao acessar o banco de dados.
        """

        try:
            lista_administradores = UsuarioBD.select().where(UsuarioBD.user_type == "ADMINISTRADOR")
        except Exception as e:
            # Captura qualquer exceção ao acessar o banco de dados
            print(
                f"Erro ao acessar o repositório de administradores: {str(e)}")
            return []
        return lista_administradores


adm_repositorio = AdministradorRepositorio()
