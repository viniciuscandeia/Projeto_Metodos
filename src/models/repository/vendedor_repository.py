"""
Módulo que define o repositório para gerenciar objetos do tipo Vendedor.

Este módulo contém a classe `VendedorRepositorio`, que oferece métodos
para registrar, remover e acessar instâncias de `Vendedor`.
"""

from typing import List

from peewee import DoesNotExist, IntegrityError

from ..entities.usuario_db_entity import UsuarioBD
from ..entities.vendedor_entity import Vendedor
from ..excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)


class VendedorRepositorio:
    """
    Classe que gerencia o repositório de vendedores.

    Esta classe oferece métodos para registrar, remover e acessar vendedores
    dentro do sistema.

    Métodos:
    - registrar_vendedor: Registra um novo vendedor no repositório.
    - remover_vendedor: Remove um vendedor do repositório com base no ID fornecido.
    - pegar_repositorio: Retorna a lista atual de vendedores no repositório.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório de vendedores como uma lista vazia.
        """

    def registrar_vendedor(self, vendedor: Vendedor) -> None:
        """
        Registra um novo vendedor no repositório.

        Este método cria uma nova entrada na base de dados para o vendedor
        fornecido.

        Args:
            vendedor (Vendedor): Objeto do tipo `Vendedor` a ser adicionado.

        Levanta:
            Exception: Se ocorrer um erro ao registrar o vendedor.
        """

        try:
            UsuarioBD.create(
                nome=vendedor.nome,
                email=vendedor.email,
                senha=vendedor.senha,
                username=vendedor.username,
                user_type="VENDEDOR",
            )
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise UsuarioIntegridadeError(f"Erro ao registrar vendedor: {str(e)}") from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise UsuarioRegistroError(f"Erro inesperado ao registrar vendedor: {str(e)}") from None


    def remover_vendedor(self, _id: str) -> None:
        """
        Remove um vendedor do repositório com base no ID fornecido.

        Este método tenta encontrar o vendedor pelo ID e, se encontrado,
        remove-o do repositório. Se o vendedor não for encontrado ou ocorrer
        um erro inesperado, uma exceção será lançada.

        Args:
            _id (str): ID do vendedor a ser removido.

        Levanta:
            Exception: Se o vendedor com o ID fornecido não for encontrado
            ou se ocorrer um erro inesperado ao remover o vendedor.
        """

        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            raise UsuarioNaoEncontrado(f"Vendedor com ID {_id} não encontrado.") from None
        except Exception as e:
            raise UsuarioErroInesperado(f"Erro inesperado ao remover vendedor: {str(e)}") from None


    def pegar_repositorio(self) -> List[Vendedor]:
        """
        Retorna a lista atual de vendedores no repositório.

        Este método consulta o banco de dados e retorna uma lista de objetos `Vendedor`
        que representam os vendedores armazenados no repositório.

        Returns:
            List[Vendedor]: Lista de objetos `Vendedor`.

        Levanta:
            Exception: Se ocorrer um erro ao acessar o banco de dados.
        """

        try:
            lista_vendedores = UsuarioBD.select().where(UsuarioBD.user_type == "VENDEDOR")
        except Exception as e:
            # Captura qualquer exceção ao acessar o banco de dados
            print(
                f"Erro ao acessar o repositório de vendedores: {str(e)}")
            return []
        return lista_vendedores


vendedor_repositorio = VendedorRepositorio()
