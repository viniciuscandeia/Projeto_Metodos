"""
Módulo que controla a adição de novos administradores ao sistema.

Este módulo define a classe `AdicionarAdministradorController`, que é responsável por
validar, criar e registrar novos administradores no sistema.
"""

from typing import Dict

from ...models.entities.administrador_entity import Administrador
from ...models.repository.administrador_repository import adm_repositorio


class AdicionarAdministradorController:
    """
    Controller para adicionar um novo administrador.

    Métodos:
    - adicionar: Adiciona um novo administrador após validar e criar a entidade.
    - __validar_campos: Valida os campos do administrador fornecido.
    - __formatar_resposta: Formata a resposta de confirmação após a adição do administrador.
    - __criar_entidade_adm: Cria uma entidade de administrador e a registra no repositório.
    """

    def adicionar(self, novo_administrador: Dict) -> Dict:
        """
        Adiciona um novo administrador ao sistema.

        Parâmetros:
            novo_administrador (Dict): Um dicionário contendo os dados do novo administrador.

        Retorna:
            Dict: Um dicionário com o status de sucesso ou falha da operação e uma mensagem.
        """
        try:
            self.__validar_campos(novo_administrador)
            self.__criar_entidade_adm(novo_administrador)
            resposta = self.__formatar_resposta(novo_administrador)
            return {"Sucesso": True, "Mensagem": resposta}
        except ValueError as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_administrador: Dict) -> None:
        """
        Valida os campos do dicionário de dados do novo administrador.

        Parâmetros:
            novo_administrador (Dict): Um dicionário contendo os dados do novo administrador.

        Levanta:
            Exception: Se qualquer campo estiver incorreto ou inválido.
        """
        if not isinstance(novo_administrador["Nome"], str):
            raise ValueError("Campo Nome Incorreto")

        if len(novo_administrador["Nome"]) == 0:
            raise ValueError("Campo Nome Incorreto")

        if not isinstance(novo_administrador["Email"], str):
            raise ValueError("Campo Email Incorreto")

        if len(novo_administrador["Email"]) == 0:
            raise ValueError("Campo Email Incorreto")

        # Validar senha
        # Precisar validar ID?

    def __formatar_resposta(self, novo_administrador: Dict) -> Dict:
        """
        Formata a resposta após a adição de um novo administrador.

        Parâmetros:
            novo_administrador (Dict): Um dicionário contendo os dados do novo administrador.

        Retorna:
            Dict: Um dicionário contendo informações formatadas do administrador adicionado.
        """
        return {
            "Tipo": "Administrador",
            "Nome": novo_administrador["Nome"],
            "Email": novo_administrador["Email"],
            "Id": novo_administrador["Id"],
        }

    def __criar_entidade_adm(self, novo_administrador: Dict) -> None:
        """
        Cria uma entidade de administrador e a registra no repositório.

        Parâmetros:
            novo_administrador (Dict): Um dicionário contendo os dados do novo administrador.
        """
        nome: str = novo_administrador["Nome"]
        email: str = novo_administrador["Email"]
        _id: str = novo_administrador["Id"]
        senha: str = novo_administrador["Senha"]

        novo_adm = Administrador(_id, nome, email, senha)
        adm_repositorio.registrar_administrador(novo_adm)
