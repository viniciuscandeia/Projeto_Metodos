"""
Módulo para a visualização de adição de administradores no sistema.

Este módulo define a classe `AdicionarAdministradorView`, que lida com a entrada de dados do usuário
para adicionar novos administradores e exibe mensagens de sucesso ou falha.
"""

import os
from typing import Dict


class EditarAdmView:
    """
    Classe de interface para adicionar administradores no sistema.

    Esta classe lida com a entrada de dados do usuário e exibe mensagens de sucesso ou falha.
    """

    def editar_administrador_view(self) -> Dict:
        """
        Coleta os dados necessários para adicionar um novo administrador e
        os retorna como um dicionário.

        :return: Dicionário contendo os dados do novo administrador.
        :rtype: Dict
        """

        os.system("cls||clear")

        # Coletando dados
        print("Editar administrador \n")
        print('(Caso nao queira editar um campo, apenas deixe em branco)')
        selectedId = input('Selectione id do usuario para editar: ')
        nome = input("Digite o nome: ")
        username = input("Digite o username: ")
        email = input("Digite o email: ")

        novo_administrador = {
            'id': selectedId,
            'Nome': nome,
            'Username': username,
            'Email': email
        }

        # Filtrando para remover itens onde o valor é vazio
        novo_administrador = {k: v for k, v in novo_administrador.items() if v}

        return novo_administrador

    def editar_administrador_sucesso(self) -> None:
        """
        Exibe uma mensagem de sucesso ao adicionar um administrador.

        :param adm: Dicionário contendo os dados do administrador recém-adicionado.
        :type adm: Dict
        """

        os.system("cls||clear")

        mensagem_sucesso = f"""
Administrador editado com sucesso

"""
        print(mensagem_sucesso)

    def editar_administrador_falha(self, error: str) -> None:
        """
        Exibe uma mensagem de erro ao falhar na adição de um administrador.

        :param error: Descrição do erro ocorrido.
        :type error: str
        """

        # os.system("cls||clear")

        mensagem_falha = f"""
Falha ao editar administrador!

\tErro: {error}
"""
        print(mensagem_falha)
