from typing import Dict

from src.models.entities.gerente_entity import Gerente
from src.models.repository.gerente_repository import gerente_repositorio


class AdicionarGerenteController:
    def adicionar(self, novo_gerente: Dict) -> Dict:
        try:
            self.__validar_campos(novo_gerente)
            self.__criar_entidade_gerente(novo_gerente)
            resposta = self.__formatar_resposta(novo_gerente)
            return {"Sucesso": True, "Mensagem": resposta}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_gerente: Dict) -> None:
        if not isinstance(novo_gerente["Nome"], str):
            raise Exception("Campo Nome Incorreto")

        if len(novo_gerente["Nome"]) == 0:
            raise Exception("Campo Nome Incorreto")

        if not isinstance(novo_gerente["Email"], str):
            raise Exception("Campo Email Incorreto")

        if len(novo_gerente["Email"]) == 0:
            raise Exception("Campo Email Incorreto")

        # Validar senha
        # Precisar validar ID?
        # Validar loja

    def __formatar_resposta(self, novo_gerente: Dict) -> Dict:
        return {
            "Tipo": "Gerente",
            "Nome": novo_gerente["Nome"],
            "Email": novo_gerente["Email"],
            "Id": novo_gerente["Id"],
            "Loja": "Null",
        }

    def __criar_entidade_gerente(self, novo_gerente: Dict) -> None:
        nome: str = novo_gerente["Nome"]
        email: str = novo_gerente["Email"]
        _id: str = novo_gerente["Id"]
        senha: str = novo_gerente["Senha"]
        _id_loja: str = novo_gerente["Id_loja"]

        objeto_gerente = Gerente(_id, nome, email, senha, _id_loja)
        gerente_repositorio.registrar_gerente(objeto_gerente)
