"""
Módulo que define o repositório para gerenciar objetos do tipo Gerente.

Este módulo contém a classe `GerenteRepositorio`, que oferece métodos
para registrar, remover e acessar instâncias de `Gerente`.
"""

from typing import List

from peewee import DoesNotExist, IntegrityError

from ..entities.gerente_entity import Gerente
from ..entities.usuario_db_entity import UsuarioBD
from ..exceptions import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)


class GerenteRepositorio:
    """
    Classe que gerencia o repositório de gerentes.

    Esta classe oferece métodos para registrar, remover e acessar gerentes
    dentro do sistema.

    Métodos:
    - registrar_gerente: Registra um novo gerente no repositório.
    - remover_gerente: Remove um gerente do repositório com base no ID fornecido.
    - pegar_repositorio: Retorna a lista atual de gerentes no repositório.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório de gerentes como uma lista vazia.
        """

    def registrar_gerente(self, gerente: Gerente) -> None:
        """
        Registra um novo gerente no repositório.

        Este método cria uma nova entrada na base de dados para o gerente
        fornecido. Se ocorrer um erro de integridade ou outro erro inesperado,
        uma exceção será lançada.

        Args:
            gerente (Gerente): Objeto do tipo `Gerente` a ser adicionado.

        Levanta:
            Exception: Se ocorrer um erro de integridade ao registrar o gerente
            ou um erro inesperado.
        """

        try:
            UsuarioBD.create(
                nome=gerente.nome,
                email=gerente.email,
                senha=gerente.senha,
                user_type="GERENTE",
            )
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise UsuarioIntegridadeError(f"Erro ao registrar gerente: {
                str(e)}") from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise UsuarioRegistroError(f"Erro inesperado ao registrar gerente: {
                str(e)}") from None


    def remover_gerente(self, _id: str) -> None:
        """
        Remove um gerente do repositório com base no ID fornecido.

        Este método tenta encontrar o gerente pelo ID e, se encontrado,
        remove-o do repositório. Se o gerente não for encontrado ou ocorrer
        um erro inesperado, uma exceção será lançada.

        Args:
            _id (str): ID do gerente a ser removido.

        Levanta:
            Exception: Se o gerente com o ID fornecido não for encontrado
            ou se ocorrer um erro inesperado ao remover o gerente.
        """
        try:
            usuario = UsuarioBD.get_by_id(_id)
            usuario.delete_instance()
        except DoesNotExist:
            raise UsuarioNaoEncontrado(f"Gerente com ID {
                _id} não encontrado.") from None
        except Exception as e:
            raise UsuarioErroInesperado(f"Erro inesperado ao remover gerente: {
                str(e)}") from None


    def pegar_repositorio(self) -> List[Gerente]:
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
            lista_gerentes = [
                Gerente(
                    nome=gerente.nome, email=gerente.email, senha=gerente.senha, id_store=0
                )
                for gerente in UsuarioBD.select().where(UsuarioBD.user_type == "GERENTE")
            ]
        except Exception as e:
            # Captura qualquer exceção ao acessar o banco de dados
            print(
                f"Erro ao acessar o repositório de gerentes: {str(e)}")
            return []
        return lista_gerentes


gerente_repositorio = GerenteRepositorio()
