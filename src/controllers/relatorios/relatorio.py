import datetime
import os
from abc import abstractmethod
from src.models.repository.administrador_repository import AdministradorRepositorio
from src.models.repository.vendedor_repository import VendedorRepositorio
from src.models.repository.gerente_repository import  GerenteRepositorio

class Relatorio:
    def __init__(self, adm_repositorio:AdministradorRepositorio,
                 gerente_repositorio:GerenteRepositorio,
                 vendedores_repositorio:VendedorRepositorio):
        self.adm_repositorio = adm_repositorio
        self.gerente_repositorio = gerente_repositorio
        self.vendedores_repositorio = vendedores_repositorio
        self.total = 0

    def get_total_usuarios(self):
        lista_adms = self.adm_repositorio.pegar_repositorio()
        lista_gerentes = self.gerente_repositorio.pegar_repositorio()
        lista_vendedores = self.vendedores_repositorio.pegar_repositorio()

        quantity_adms = len(lista_adms)
        quantity_gerentes = len(lista_gerentes)
        quantity_vendedores = len(lista_vendedores)

        total = quantity_adms + quantity_gerentes + quantity_vendedores
        self.total = total
        return total

    def get_percentagem_adms(self) -> float:
        lista_adms = self.adm_repositorio.pegar_repositorio()
        return len(lista_adms)/self.total*100

    def get_percentage_gerentes(self) -> float:
        lista_gerente = self.gerente_repositorio.pegar_repositorio()
        return len(lista_gerente)/self.total*100

    def get_percentage_vendedores(self) -> float:
        lista_vendedores = self.vendedores_repositorio.pegar_repositorio()
        return len(lista_vendedores) / self.total * 100


    def gerar_nome_arquivo(self):
        data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        return data_atual

    @abstractmethod
    def formatar_relatorio(self, data: dict):
        pass

    #template method
    def gerar_relatorio(self):
        total = self.get_total_usuarios()
        percentage_adms = self.get_percentagem_adms()
        percentage_gerentes = self.get_percentage_gerentes()
        percentage_vendedores = self.get_percentage_vendedores()


        data_relatorio = {'total': total,
                'percentageVendedores': percentage_vendedores,
                'percentageAdm': percentage_adms,
                'percentageGerente': percentage_gerentes}

        self.formatar_relatorio(data=data_relatorio)