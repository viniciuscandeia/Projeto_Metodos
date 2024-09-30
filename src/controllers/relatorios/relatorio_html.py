from abc import ABC

from src.controllers.relatorios.relatorio import Relatorio
from src.models.repository.administrador_repository import AdministradorRepositorio
from src.models.repository.gerente_repository import GerenteRepositorio
from src.models.repository.vendedor_repository import VendedorRepositorio
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class RelatorioHTML(Relatorio, ABC):
    def __init__(self, adm_repositorio:AdministradorRepositorio,
                 gerente_repositorio:GerenteRepositorio,
                 vendedores_repositorio:VendedorRepositorio):
        super().__init__(adm_repositorio,
                         gerente_repositorio,
                         vendedores_repositorio)

    def formatar_relatorio(self, data: dict):
            nome_arquivo = f'{self.gerar_nome_arquivo()}.html'

            html_conteudo = f"""
            <html>
                <head>
                    <title>Relatório de Usuários (HTML)</title>
                    <style>
                        body {{ font-family: Helvetica, Arial, sans-serif; }}
                        h1 {{ color: #333; }}
                        p {{ font-size: 14px; }}
                    </style>
                </head>
                <body>
                    <h1>Relatório de Usuários(HTML)</h1>
                    <p><strong>Total:</strong> {data['total']}</p>
                    <p><strong>Porcentagem de Vendedores:</strong> {data['percentageVendedores']}%</p>
                    <p><strong>Porcentagem de Administradores:</strong> {data['percentageAdm']}%</p>
                    <p><strong>Porcentagem de Gerentes:</strong> {data['percentageGerente']}%</p>
                </body>
            </html>
            """

            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(html_conteudo)

            print(f"Relatório HTML gerado: {nome_arquivo}")
