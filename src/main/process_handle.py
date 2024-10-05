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

from .facade.adicionar_facade.adicionar_adm_facade import adicionar_adm_facade
from .facade.adicionar_facade.adicionar_gerente_facade import adicionar_gerente_facade
from .facade.adicionar_facade.adicionar_vendedor_facade import adicionar_vendedor_facade
from .facade.administrador_facade import adm_facade

from .facade.editar_facade.editar_adm_facade import editar_adm_facade
from .facade.adicionar_processo import adicionar_processo
from .facade.gerente_facade import gerente_facade
from .facade.introducao_processo import introducao_processo
from .facade.listar_facade.listar_adm_facade import listar_adm_facade
from .facade.listar_facade.listar_gerente_facade import listar_gerente_facade
from .facade.listar_facade.listar_vendedor_facade import listar_vendedor_facade
from .facade.loja_facade import loja_facade
import os
from .facade.listar_processo import listar_processo, ListarProcessoLoja
from .facade.editar_processo import editar_processo, EditarProcessoLoja
from .facade.notification_processo import ListarNotifications
from ..controllers.relatorios.relatorio import Relatorio
from ..controllers.relatorios.relatorio_html import RelatorioHTML
from ..controllers.relatorios.relatorio_pdf import RelatorioPdf
from ..models.inicializar_db import inicializar_database
from .facade.listar_processo import ListarProcessoLoja
from .facade.process_helpers import processo_helpers
from .facade.excluir_processo import ExcluirProcessoLoja
from src.models.entities_db.loja_db_entity import LojaDB
from src.lib.notificator_api import NotificatorApi
from src.adapters.firebase_adapter_notificator_api import firebase_adapter_notificator_api
from ..models.repository.administrador_repository import AdministradorRepositorio
from ..models.repository.gerente_repository import GerenteRepositorio
from ..models.repository.vendedor_repository import VendedorRepositorio
from ..singletons.adm_repository_singleton import AdmRepositorySingleton
from ..singletons.gerente_repository_singleton import GerenteRepositorySingleton
from ..singletons.vendedor_repository_singleton import VendedorRepositorySingleton

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

    #
    # #TEMPLATE METHOD
    # relatorio = RelatorioPdf(adm_repositorio=AdmRepositorySingleton().getInstance(),
    #                          gerente_repositorio=GerenteRepositorySingleton().getInstance(),
    #                          vendedores_repositorio=VendedorRepositorySingleton().getInstance(),)
    # relatoriohtml = RelatorioHTML(adm_repositorio=AdmRepositorySingleton().getInstance(),
    #                          gerente_repositorio=GerenteRepositorySingleton().getInstance(),
    #                          vendedores_repositorio=VendedorRepositorySingleton().getInstance())
    #
    # relatoriohtml.gerar_relatorio()

    # LOJA FACADE TEST
    # registrarLojaController = RegistrarLojaController()
    # # registrarLojaController.registrarLoja(id_usuario=2, loja=Loja(endereco='Rua mauricio', nome='maganize'))
    # listarLojaController = ListarLojaController()
    # editarLojaController = EditarLojaController()
    # editarLojaController.editar_loja_adm(id_adm=2, id_loja=4, nova_loja={'Endereco': 'Rua gama filho'})
    # excluirLojaController = ExcluirLojaController()
    # excluirLojaController.excluir_loja(id_adm=2,id_loja=9)

    # print(listarLojaController.list_lojas_adm(id_usuario=2))

    #ADAPTER
    # class Controller():
    #     def __init__(self, notificator_api:NotificatorApi) -> None:
    #         self.notificator_api = notificator_api
    #
    #     def basic_controller(self, id_loja:int, id_adm:int):
    #         #...
    #         self.notificator_api.send(id_loja=id_loja, id_adm=id_adm, mensagem='Essa é uma notificacao')
    #         #...
    #
    #     def basic_receive(self, id_usuario:int, id_loja:int):
    #         return self.notificator_api.receive(id_usuario=id_usuario, id_loja=id_loja)
    #
    # controller_use = Controller(notificator_api=database_adapter_notificator_api)
    # controller_use = Controller(notificator_api=firebase_adapter_notificator_api)
    # controller_use.basic_controller(2, 2)
    # controller_use.basic_controller(1, 2)
    # list = controller_use.basic_receive(id_usuario=1, id_loja=2)
    #
    # print('Recebendo notificacao')
    # for item in list:
    #     print(item)
    #
    # list = controller_use.basic_receive(id_usuario=4, id_loja=1)
    #
    # print('Recebendo notificacao')
    # for item in list:
    #     print(item)

    #SINGLETON
    # singleton = AdmRepositorySingleton('test')
    # singleton2 = AdmRepositorySingleton('test32')
    #
    # if(id(singleton2) == id(singleton)):
    #     print('sucesso')
    #     singleton2.setValue('value changed1')
    #     print(singleton.getValue())
    #     print(singleton2.getValue())
    # else:
    #     print('falha')

    while True:
        comando = introducao_processo()

        match comando:
            case "1":  # Cadastrar

                while True:
                    retorno = adicionar_processo()
                    match retorno:
                        case "1":
                            adicionar_adm_facade()
                        case "2":
                            adicionar_gerente_facade()
                        case "3":
                            adicionar_vendedor_facade()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")

            case "2":

                while True:
                    retorno = listar_processo()
                    match retorno:
                        case "1":
                            listar_adm_facade()
                        case "2":
                            listar_gerente_facade()
                        case "3":
                            listar_vendedor_facade()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")
            case "3":
                while True:
                    retorno = editar_processo()
                    match retorno:
                        case "1":
                            editar_adm_facade()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")

            case "4":
                while True:
                    id_administrador = processo_helpers.getIdUsuario()

                    if id_administrador == None:
                        break

                    nova_loja = processo_helpers.getDataToCreateLoja()

                    if nova_loja == None:
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

                            if id_adm == None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
                                break

                            loja_facade.get_loja_adm(
                                id_adm=id_adm, id_loja=id_loja)
                        case "3":
                            id_gerente = processo_helpers.getIdUsuario()

                            if id_gerente == None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
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

                            if id_loja == None:
                                break

                            id_adm = processo_helpers.getIdUsuario()

                            if id_adm == None:
                                break

                            loja = loja_facade.get_loja_adm(
                                id_adm=id_adm, id_loja=id_loja)

                            if loja:
                                nova_loja = processo_helpers.getDataToEditLoja()

                                loja_facade.editar_loja_adm(
                                    id_adm=id_adm, id_loja=id_loja, nova_loja=nova_loja)

                        case "2":
                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
                                break

                            id_gerente = processo_helpers.getIdUsuario()

                            if id_gerente == None:
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

                            if id_adm == None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
                                break

                            loja_facade.excluir_loja(
                                id_administrador=id_adm, id_loja=id_loja)
                        case "9":
                            break
            case "8":
                while True:
                    comando = ListarNotifications.executar()

                    match comando:
                        case "1":
                            id_gerente = processo_helpers.getIdUsuario()

                            if id_gerente == None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
                                break

                            gerente_facade.get_notifications(id_loja=id_loja, id_gerente=id_gerente)
                        case "9":
                            break
            case '9':
                adm_facade.gerar_relatorio()

            case "10":
                sys.exit()
            case _:
                print("Comando invalido!")
