"""
Módulo para gerenciamento do fluxo principal do sistema.

Este módulo contém a função `start` que gerencia o fluxo principal do programa.
A função exibe a tela inicial, captura comandos do usuário e redireciona para as
funções de adicionar e listar itens com base nas entradas fornecidas. O loop
principal continua até que o usuário escolha sair do programa.

Funções:
- start: Inicializa o sistema e gerencia o fluxo principal do programa.
"""

import sys

from .facade.adicionar_processo import adicionar_processo
from .facade.introducao_processo import introducao_processo
from .facade.loja_facade import loja_facade
import os
from .facade.listar_processo import listar_processo, ListarProcessoLoja
from .facade.editar_processo import editar_processo, EditarProcessoLoja
from ..controllers.relatorios.relatorio import Relatorio
from ..controllers.relatorios.relatorio_html import RelatorioHTML
from ..controllers.relatorios.relatorio_pdf import RelatorioPdf
from ..models.inicializar_db import inicializar_database
from .facade.listar_processo import ListarProcessoLoja
from .facade.process_helpers import processo_helpers
from .facade.excluir_processo import ExcluirProcessoLoja
from src.models.entities_db.loja_db_entity import LojaDB
from src.lib.notificator_api import NotificatorApi
from src.adapters.database_adapter_notificator_api import database_adapter_notificator_api
from src.adapters.firebase_adapter_notificator_api import firebase_adapter_notificator_api
from ..models.repository.administrador_repository import AdministradorRepositorio
from ..models.repository.gerente_repository import GerenteRepositorio
from ..models.repository.vendedor_repository import VendedorRepositorio

from .facade.usuarios_facade import UsuariosFacade

USAR_MEMORIA = False


def start() -> None:
    """
    Inicializa o sistema e gerencia o fluxo principal do programa.

    Esta função é responsável por exibir a tela inicial, capturar comandos do usuário e
    redirecionar para as funcionalidades de adicionar e listar itens com base nas entradas
    fornecidas. O loop principal continua até que o usuário escolha sair do programa.

    - Limpa a tela.
    - Mostra a tela inicial e captura o comando do usuário.
    - Navega para as funções de adicionar ou listar conforme o comando.
    - Gerencia a saída do programa.

    :return: None
    """
    inicializar_database(USAR_MEMORIA)
    os.system("cls||clear")

    usuario_facade = UsuariosFacade()

    while True:
        comando = introducao_processo()

        match comando:
            case "1":  # Cadastrar

                while True:
                    retorno = adicionar_processo()
                    match retorno:
                        case "1":
                            usuario_facade.adicionar_administrador()
                        case "2":
                            usuario_facade.adicionar_gerente()
                        case "3":
                            usuario_facade.adicionar_vendedor()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")

            case "2":

                while True:
                    retorno = listar_processo()
                    match retorno:
                        case "1":
                            usuario_facade.listar_administrador()
                        case "2":
                            usuario_facade.listar_gerente()
                        case "3":
                            usuario_facade.listar_vendedor()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")
            case "3":
                while True:
                    retorno = editar_processo()
                    match retorno:
                        case "1":
                            usuario_facade.editar_administrador()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")

            case "4":
                while True:
                    id_administrador = processo_helpers.getIdUsuario()

                    if id_administrador is None:
                        break

                    nova_loja = processo_helpers.getDataToCreateLoja()

                    if nova_loja is None:
                        break

                    if nova_loja:
                        loja_facade.registrar_loja(
                            id_admnistrador=id_administrador, loja=nova_loja)
                        break
            case "5":
                while True:
                    retorno = ListarProcessoLoja.executar()
                    match retorno:
                        case "1":
                            id_adm = processo_helpers.getIdUsuario()

                            if (id_adm):
                                loja_facade.listar_adm(id_adm=id_adm)
                        case "2":
                            id_adm = processo_helpers.getIdUsuario()

                            if id_adm is None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja is None:
                                break

                            loja_facade.get_loja_adm(
                                id_adm=id_adm, id_loja=id_loja)
                        case "3":
                            id_gerente = processo_helpers.getIdUsuario()

                            if id_gerente is None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja is None:
                                break

                            loja_facade.get_loja_gerente(
                                id_gerente=id_gerente, id_loja=id_loja)

                        case _:
                            break
            case "6":
                while True:
                    retorno = EditarProcessoLoja.executar()

                    match retorno:
                        case "1":
                            id_loja = processo_helpers.getIdLoja()

                            if id_loja is None:
                                break

                            id_adm = processo_helpers.getIdUsuario()

                            if id_adm is None:
                                break

                            loja = loja_facade.get_loja_adm(
                                id_adm=id_adm, id_loja=id_loja)

                            if loja:
                                nova_loja = processo_helpers.getDataToEditLoja()

                                loja_facade.editar_loja_adm(
                                    id_adm=id_adm, id_loja=id_loja, nova_loja=nova_loja)

                        case "2":
                            id_loja = processo_helpers.getIdLoja()

                            if id_loja is None:
                                break

                            id_gerente = processo_helpers.getIdUsuario()

                            if id_gerente is None:
                                break

                            loja = loja_facade.get_loja_gerente(
                                id_gerente=id_gerente, id_loja=id_loja)

                            if loja:
                                nova_loja = processo_helpers.getDataToEditLoja()

                                loja_facade.editar_loja_gerente(
                                    id_gerente=id_gerente, id_loja=id_loja, nova_loja=nova_loja)
                        case _:
                            print('Comando Invalido')
                            break

            case "7":
                while True:
                    comando = ExcluirProcessoLoja.executar()

                    match comando:
                        case "1":
                            id_adm = processo_helpers.getIdUsuario()

                            if id_adm is None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja is None:
                                break

                            loja_facade.excluir_loja(
                                id_administrador=id_adm, id_loja=id_loja)
                        case "9":
                            break
            case "9":
                sys.exit()
                break
            case _:
                print("Comando invalido!")
