import datetime
from src.controllers.relatorios.relatorio import Relatorio
from src.models.repository.administrador_repository import AdministradorRepositorio
from src.models.repository.gerente_repository import GerenteRepositorio
from src.models.repository.vendedor_repository import VendedorRepositorio
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class RelatorioPdf(Relatorio):
    def __init__(self, adm_repositorio:AdministradorRepositorio,
                 gerente_repositorio:GerenteRepositorio,
                 vendedores_repositorio:VendedorRepositorio):
        super().__init__(adm_repositorio,
                         gerente_repositorio,
                         vendedores_repositorio)


    def formatar_relatorio(self, data: dict):
        nome_arquivo = self.gerar_nome_arquivo() + '.pdf'

        c = canvas.Canvas(nome_arquivo, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Relatório de Usuarios (PDF)")
        c.drawString(100, 720, f"Total: {data['total']}")
        c.drawString(100, 700, f"Porcentagem de Vendedores: {data['percentageVendedores']}%")
        c.drawString(100, 680, f"Porcentagem de Administradores: {data['percentageAdm']}%")
        c.drawString(100, 660, f"Porcentagem de Gerentes: {data['percentageGerente']}%")
        c.save()

        print('Relatorio Salvo em PDF')