import os
from src.models.entities_db.loja_db_entity import LojaDB


class ListarLojasView:
    def listar(self, lista: list[LojaDB]):
        if len(lista) > 0:
            self.__lista_preenchida(lista=lista)
            return

        self.__lista_vazia()
        return

    def __lista_vazia(self) -> None:
        os.system('cls||clear')
        mensagem = """
Lista vazia de Lojas.
"""
        print(mensagem)

        return

    def __lista_preenchida(self, lista: list[LojaDB]) -> None:
        mensagem = """
Lista de Lojas

"""
        lista_lojas = '\n'.join(
            [f"\t - [{loja.id}] {loja.nome} | Endereço: {loja.endereco}" for loja in list])

        print(mensagem + lista_lojas)

        return
