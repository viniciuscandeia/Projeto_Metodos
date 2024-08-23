import os

from .constructor.adicionar.adicionar_adm_constructor import adicionar_adm_constructor
from .constructor.adicionar.adicionar_gerente_constructor import (
    adicionar_gerente_constructor,
)
from .constructor.adicionar.adicionar_vendedor_constructor import (
    adicionar_vendedor_constructor,
)
from .constructor.adicionar_processo import adicionar_processo
from .constructor.introducao_processo import introducao_processo
from .constructor.listar.listar_adm_constructor import listar_adm_constructor
from .constructor.listar.listar_gerente_constructor import listar_gerente_constructor
from .constructor.listar.listar_vendedor_constructor import listar_vendedor_constructor
from .constructor.listar_processo import listar_processo


def start() -> None:

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

            case "9":
                exit()
            case _:
                print("Comando invalido!")
