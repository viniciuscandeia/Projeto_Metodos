from typing import Dict

from src.models.entities.vendedor_entity import Vendedor
from src.models.repository.vendedor_repository import vendedor_repositorio


class AdicionarVendedorController:
    def adicionar(self, novo_vendedor: Dict) -> Dict:
        try:
            self.__validar_campos(novo_vendedor)
            self.__criar_entidade_vendedor(novo_vendedor)
            resposta = self.__formatar_resposta(novo_vendedor)
            return {"Sucesso": True, "Mensagem": resposta}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_vendedor: Dict) -> None:
        if not isinstance(novo_vendedor["Nome"], str):
            raise Exception("Campo Nome Incorreto")

        if len(novo_vendedor["Nome"]) == 0:
            raise Exception("Campo Nome Incorreto")

        if not isinstance(novo_vendedor["Email"], str):
            raise Exception("Campo Email Incorreto")

        if len(novo_vendedor["Email"]) == 0:
            raise Exception("Campo Email Incorreto")

        # Validar senha
        # Precisar validar ID?
        # Validar loja

    def __formatar_resposta(self, novo_vendedor: Dict) -> Dict:
        return {
            "Tipo": "Vendedor",
            "Nome": novo_vendedor["Nome"],
            "Email": novo_vendedor["Email"],
            "Id": novo_vendedor["Id"],
            "Loja": "Null",
        }

    def __criar_entidade_vendedor(self, novo_vendedor: Dict) -> None:
        nome: str = novo_vendedor["Nome"]
        email: str = novo_vendedor["Email"]
        _id: str = novo_vendedor["Id"]
        senha: str = novo_vendedor["Senha"]
        _id_loja: str = novo_vendedor["Id_loja"]

        objeto_vendedor = Vendedor(_id, nome, email, senha, _id_loja)
        vendedor_repositorio.registrar_vendedor(objeto_vendedor)
