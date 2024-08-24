"""
Módulo para controle de adição de novos gerentes ao sistema.

Este módulo contém a classe AdicionarGerenteController, responsável por validar
os dados de um novo gerente, criar a entidade gerente e registrá-la no repositório.
"""


from typing import Dict

from ...models.entities.gerente_entity import Gerente
from ...models.repository.gerente_repository import gerente_repositorio


class AdicionarGerenteController:
    """
    Controller para adicionar um novo gerente.

    Métodos:
    - adicionar: Adiciona um novo gerente após validar e criar a entidade.
    - __validar_campos: Valida os campos do gerente fornecido.
    - __formatar_resposta: Formata a resposta de confirmação após a adição do gerente.
    - __criar_entidade_gerente: Cria uma entidade de gerente e a registra no repositório.
    """

    def adicionar(self, novo_gerente: Dict) -> Dict:
        """
        Adiciona um novo gerente ao sistema.

        Parâmetros:
            novo_gerente (Dict): Um dicionário contendo os dados do novo gerente.

        Retorna:
            Dict: Um dicionário com o status de sucesso ou falha da operação e uma mensagem.
        """
        try:
            self.__validar_campos(novo_gerente)
            self.__criar_entidade_gerente(novo_gerente)
            resposta = self.__formatar_resposta(novo_gerente)
            return {"Sucesso": True, "Mensagem": resposta}
        except ValueError as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_gerente: Dict) -> None:
        """
        Valida os campos do dicionário de dados do novo gerente.

        Parâmetros:
            novo_gerente (Dict): Um dicionário contendo os dados do novo gerente.

        Levanta:
            Exception: Se qualquer campo estiver incorreto ou inválido.
        """
        if not isinstance(novo_gerente["Nome"], str):
            raise ValueError("Campo Nome Incorreto")

        if len(novo_gerente["Nome"]) == 0:
            raise ValueError("Campo Nome Incorreto")

        if not isinstance(novo_gerente["Email"], str):
            raise ValueError("Campo Email Incorreto")

        if len(novo_gerente["Email"]) == 0:
            raise ValueError("Campo Email Incorreto")

        # Validar senha
        # Precisar validar ID?
        # Validar loja

    def __formatar_resposta(self, novo_gerente: Dict) -> Dict:
        """
        Formata a resposta após a adição de um novo gerente.

        Parâmetros:
            novo_gerente (Dict): Um dicionário contendo os dados do novo gerente.

        Retorna:
            Dict: Um dicionário contendo informações formatadas do gerente adicionado.
        """
        return {
            "Tipo": "Gerente",
            "Nome": novo_gerente["Nome"],
            "Email": novo_gerente["Email"],
            "Id": novo_gerente["Id"],
            "Loja": "Null",
        }

    def __criar_entidade_gerente(self, novo_gerente: Dict) -> None:
        """
        Cria uma entidade de gerente e a registra no repositório.

        Parâmetros:
            novo_gerente (Dict): Um dicionário contendo os dados do novo gerente.
        """
        nome: str = novo_gerente["Nome"]
        email: str = novo_gerente["Email"]
        _id: str = novo_gerente["Id"]
        senha: str = novo_gerente["Senha"]
        _id_loja: str = novo_gerente["Id_loja"]

        objeto_gerente = Gerente(_id, nome, email, senha, _id_loja)
        gerente_repositorio.registrar_gerente(objeto_gerente)
