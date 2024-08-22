from typing import Dict

from src.models.entities.administrador_entity import Administrador
from src.models.repository.administrador_repository import adm_repositorio


class AdicionarAdministradorController:
    def adicionar(self, novo_administrador: Dict) -> Dict:
        try:
            self.__validar_campos(novo_administrador)
            self.__criar_entidade_adm(novo_administrador)
            resposta = self.__formatar_resposta(novo_administrador)
            return {"Sucesso": True, "Mensagem": resposta}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_administrador: Dict) -> None:
        if not isinstance(novo_administrador["Nome"], str):
            raise Exception("Campo Nome Incorreto")

        if len(novo_administrador["Nome"]) == 0:
            raise Exception("Campo Nome Incorreto")

        if not isinstance(novo_administrador["Email"], str):
            raise Exception("Campo Email Incorreto")

        if len(novo_administrador["Email"]) == 0:
            raise Exception("Campo Email Incorreto")

        # Validar senha
        # Precisar validar ID?

    def __formatar_resposta(self, novo_administrador: Dict) -> Dict:
        return {
            "Tipo": "Administrador",
            "Nome": novo_administrador["Nome"],
            "Email": novo_administrador["Email"],
            "Id": novo_administrador["Id"],
        }

    def __criar_entidade_adm(self, novo_administrador: Dict) -> None:
        nome: str = novo_administrador["Nome"]
        email: str = novo_administrador["Email"]
        _id: str = novo_administrador["Id"]
        senha: str = novo_administrador["Senha"]

        novo_adm = Administrador(_id, nome, email, senha)
        adm_repositorio.registrar_administrador(novo_adm)
