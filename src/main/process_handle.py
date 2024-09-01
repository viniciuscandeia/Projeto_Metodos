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
from .constructor.listar_processo import listar_processo
from ..models.inicializar_db import inicializar_database

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

            case "9":
                sys.exit()
            case _:
                print("Comando invalido!")
