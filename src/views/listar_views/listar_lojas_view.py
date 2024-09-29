import os
from .listar_view_interface import AbstractListView
from src.controllers.listar_controller.listar_loja_controller import LojasListController
from src.models.entities.entities_db.loja_db_entity import LojaDB
from typing import List

class LojasListagemView(AbstractListView): 
    def listar(self, list:List[LojaDB]):
        if len(list) > 0:
            self._lista_preenchida(list=list)
            return
        
        self._lista_vazia()
        return
    
    def _lista_vazia(self) -> None:
        os.system('cls||clear')
        mensagem = """
Lista vazia de Lojas.
"""
        print(mensagem)

        return

    def _lista_preenchida(self, list: List[LojaDB]) -> None:
        mensagem = """
Lista de Lojas

"""
        lista_lojas = '\n'.join([f"\t - [{loja.id}] {loja.nome} | Endereço: {loja.endereco}" for loja in list])

        print(mensagem + lista_lojas)

        return
