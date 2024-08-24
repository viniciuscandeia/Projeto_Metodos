"""
Módulo que controla a adição de novos vendedores ao sistema.

Este módulo define a classe `AdicionarVendedorController`, responsável por validar, criar e
registrar novos vendedores no sistema.
"""

from typing import Dict

from ...models.entities.vendedor_entity import Vendedor
from ...models.repository.vendedor_repository import vendedor_repositorio


class AdicionarVendedorController:
    """
    Controller para adicionar um novo vendedor.

    Métodos:
    - adicionar: Adiciona um novo vendedor após validar e criar a entidade.
    - __validar_campos: Valida os campos do vendedor fornecido.
    - __formatar_resposta: Formata a resposta de confirmação após a adição do vendedor.
    - __criar_entidade_vendedor: Cria uma entidade de vendedor e a registra no repositório.
    """

    def adicionar(self, novo_vendedor: Dict) -> Dict:
        """
        Adiciona um novo vendedor ao sistema.

        Parâmetros:
            novo_vendedor (Dict): Um dicionário contendo os dados do novo vendedor.

        Retorna:
            Dict: Um dicionário com o status de sucesso ou falha da operação e uma mensagem.
        """
        try:
            self.__validar_campos(novo_vendedor)
            self.__criar_entidade_vendedor(novo_vendedor)
            resposta = self.__formatar_resposta(novo_vendedor)
            return {"Sucesso": True, "Mensagem": resposta}
        except ValueError as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_vendedor: Dict) -> None:
        """
        Valida os campos do dicionário de dados do novo vendedor.

        Parâmetros:
            novo_vendedor (Dict): Um dicionário contendo os dados do novo vendedor.

        Levanta:
            Exception: Se qualquer campo estiver incorreto ou inválido.
        """
        if not isinstance(novo_vendedor["Nome"], str):
            raise ValueError("Campo Nome Incorreto")

        if len(novo_vendedor["Nome"]) == 0:
            raise ValueError("Campo Nome Incorreto")

        if not isinstance(novo_vendedor["Email"], str):
            raise ValueError("Campo Email Incorreto")

        if len(novo_vendedor["Email"]) == 0:
            raise ValueError("Campo Email Incorreto")

        # Validar senha
        # Precisar validar ID?
        # Validar loja

    def __formatar_resposta(self, novo_vendedor: Dict) -> Dict:
        """
        Formata a resposta após a adição de um novo vendedor.

        Parâmetros:
            novo_vendedor (Dict): Um dicionário contendo os dados do novo vendedor.

        Retorna:
            Dict: Um dicionário contendo informações formatadas do vendedor adicionado.
        """
        return {
            "Tipo": "Vendedor",
            "Nome": novo_vendedor["Nome"],
            "Email": novo_vendedor["Email"],
            "Id": novo_vendedor["Id"],
            "Loja": "Null",
        }

    def __criar_entidade_vendedor(self, novo_vendedor: Dict) -> None:
        """
        Cria uma entidade de vendedor e a registra no repositório.

        Parâmetros:
            novo_vendedor (Dict): Um dicionário contendo os dados do novo vendedor.
        """
        nome: str = novo_vendedor["Nome"]
        email: str = novo_vendedor["Email"]
        _id: str = novo_vendedor["Id"]
        senha: str = novo_vendedor["Senha"]
        _id_loja: str = novo_vendedor["Id_loja"]

        objeto_vendedor = Vendedor(_id, nome, email, senha, _id_loja)
        vendedor_repositorio.registrar_vendedor(objeto_vendedor)
