
from abc import ABC, abstractmethod
from typing import Dict
from ...lib.validar_inputs import ValidarInputs

class EditarUsuarioController(ABC):
    def editar(self, usuarioEditado:Dict) -> Dict:
        try:
            self.__validar_campos(usuarioEditado)
            entidade_editada = self._editar_entidade(usuarioEditado)

            return {"Sucesso": True, "Mensagem": entidade_editada}
        except ValueError as erro:
            return {"Sucesso": False, "ERROR": str(erro)}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, usuarioEditado) -> None:
        try:
            ValidarInputs.validar_id(usuarioEditado)

            if("Nome" in usuarioEditado):
                ValidarInputs.validar_nome(usuarioEditado)
            
            if("Email" in usuarioEditado):
                 ValidarInputs.validar_email(usuarioEditado)
            
            if("Username" in  usuarioEditado):
                ValidarInputs.validar_username(usuarioEditado)
        except ValueError as erro:
            raise ValueError(str(erro)) from None
    

    @abstractmethod 
    def _editar_entidade(self, id:int, usuarioEditado:Dict) -> None:
       """"""