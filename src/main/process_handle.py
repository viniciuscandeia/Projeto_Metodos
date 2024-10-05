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

from .facade.introducao_processo import introducao_processo
from .facade.loja_facade import loja_facade
import os
from ..models.inicializar_db import inicializar_database
from .facade.process_helpers import processo_helpers

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
                    retorno = usuario_facade.escolher_usuario_adicionar_usuario()
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
                    retorno = usuario_facade.selecionar_usuario_listar_loja()
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
                    retorno = usuario_facade.selecionar_usuario_edicao_usuario()
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
                    retorno = usuario_facade.selecionar_usuario_edicao_loja
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
                    retorno = usuario_facade.selecionar_usuario_edicao_loja()

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
                    comando = usuario_facade.selecionar_usuario_excluir_loja

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
