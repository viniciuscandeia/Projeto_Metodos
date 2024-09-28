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

from .constructor.adicionar_constructor.adicionar_adm_constructor import (
    adicionar_adm_constructor,
)
from .constructor.adicionar_constructor.adicionar_gerente_constructor import (
    adicionar_gerente_constructor,
)
from .constructor.adicionar_constructor.adicionar_vendedor_constructor import (
    adicionar_vendedor_constructor,
)
from .constructor.editar_constructor.editar_adm_constructor import (
    editar_adm_constructor,
)
from .constructor.adicionar_processo import adicionar_processo
from .constructor.introducao_processo import introducao_processo
from .constructor.listar_constructor.listar_adm_constructor import (
    listar_adm_constructor,
)
from .constructor.listar_constructor.listar_gerente_constructor import (
    listar_gerente_constructor,
)
from .constructor.listar_constructor.listar_vendedor_constructor import (
    listar_vendedor_constructor,
)
from .constructor.loja_constructor import (
    loja_constructor,
)
from .constructor.listar_processo import listar_processo, ListarProcessoLoja
from .constructor.editar_processo import editar_processo, EditarProcessoLoja
from ..models.inicializar_db import inicializar_database
from .constructor.listar_processo import ListarProcessoLoja
from .constructor.process_helpers import processo_helpers
from .constructor.excluir_processo import ExcluirProcessoLoja
import os 

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

    # registrarLojaController = RegistrarLojaController()
    # # registrarLojaController.registrarLoja(id_usuario=2, loja=Loja(endereco='Rua mauricio', nome='maganize'))
    # listarLojaController = ListarLojaController()
    # editarLojaController = EditarLojaController()
    # editarLojaController.editar_loja_adm(id_adm=2, id_loja=4, nova_loja={'Endereco': 'Rua gama filho'})
    # excluirLojaController = ExcluirLojaController()
    # excluirLojaController.excluir_loja(id_adm=2,id_loja=9)

    # print(listarLojaController.list_lojas_adm(id_usuario=2))
 
    

    os.system("cls||clear")


    while True:
        comando = introducao_processo()

        match comando:
            case "1":  # Cadastrar

                while True:
                    retorno = adicionar_processo()
                    match retorno:
                        case "1":
                            adicionar_adm_constructor()
                        case "2":
                            adicionar_gerente_constructor()
                        case "3":
                            adicionar_vendedor_constructor()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")

            case "2":

                while True:
                    retorno = listar_processo()
                    match retorno:
                        case "1":
                            listar_adm_constructor()
                        case "2":
                            listar_gerente_constructor()
                        case "3":
                            listar_vendedor_constructor()
                        case "9":
                            break
                        case _:
                            print("Comando invalido!")
            case "3":
                while True:
                    retorno = editar_processo()
                    match retorno:
                        case "1":
                            editar_adm_constructor()
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
                       loja_constructor.registrar_loja(id_admnistrador=id_administrador, loja=nova_loja)
                       break
            case "5":
                while True:
                    retorno = ListarProcessoLoja.executar()
                    match retorno:
                        case "1":
                            id_adm = processo_helpers.getIdUsuario()

                            if(id_adm):
                                loja_constructor.listar_adm(id_adm=id_adm)
                        case "2":
                            id_adm = processo_helpers.getIdUsuario()

                            if id_adm == None:
                                break

                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
                                break


                            loja_constructor.get_loja_adm(id_adm=id_adm, id_loja=id_loja)
                        case "3":
                            id_gerente = processo_helpers.getIdUsuario()

                            if id_gerente == None:
                                break
                            
                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
                                break

                            loja_constructor.get_loja_gerente(id_gerente=id_gerente, id_loja=id_loja)
                        
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


                            loja = loja_constructor.get_loja_adm(id_adm=id_adm, id_loja=id_loja)

                            if loja:
                                nova_loja = processo_helpers.getDataToEditLoja()
                                    
                                loja_constructor.editar_loja_adm(id_adm=id_adm, id_loja=id_loja, nova_loja=nova_loja)

                        case "2":
                            id_loja = processo_helpers.getIdLoja()

                            if id_loja == None:
                                break
                            
                            id_gerente = processo_helpers.getIdUsuario()
                            
                            if id_gerente == None:
                                break


                            loja = loja_constructor.get_loja_gerente(id_gerente=id_gerente, id_loja=id_loja)
                            
                            if loja:
                                nova_loja = processo_helpers.getDataToEditLoja()

                                loja_constructor.editar_loja_gerente(id_gerente=id_gerente, id_loja=id_loja, nova_loja=nova_loja)
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

                            loja_constructor.excluir_loja(id_administrador=id_adm, id_loja=id_loja)
                        case "9":
                            break
            case "9":
                sys.exit()
                break
            case _:
                print("Comando invalido!")
