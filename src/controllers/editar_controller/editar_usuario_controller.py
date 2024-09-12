
from abc import ABC, abstractmethod
from typing import Dict
from ...lib.validar_inputs import ValidarInputs

class EditarUsuarioController(ABC):
    def editar(self, usuario_editado:Dict) -> Dict:
        try:
            self.__validar_campos(usuario_editado)
            entidade_editada = self._editar_entidade(usuario_editado)

            return {"Sucesso": True, "Mensagem": entidade_editada}
        except ValueError as erro:
            return {"Sucesso": False, "ERROR": str(erro)}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, usuario_editado) -> None:
        try:
            ValidarInputs.validar_id(usuario_editado)

            if("Nome" in usuario_editado):
                ValidarInputs.validar_nome(usuario_editado)

            if("Email" in usuario_editado):
                 ValidarInputs.validar_email(usuario_editado)

            if("Username" in  usuario_editado):
                ValidarInputs.validar_username(usuario_editado)
        except ValueError as erro:
            raise ValueError(str(erro)) from None


    @abstractmethod
    def _editar_entidade(self, id:int, usuario_editado:Dict) -> None:
       """"""