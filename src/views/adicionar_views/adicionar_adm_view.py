"""
Módulo para a visualização de adição de administradores no sistema.

Este módulo define a classe `AdicaoAdministradorView`, que lida com a entrada de dados do usuário
para adicionar novos administradores e exibe mensagens de sucesso ou falha.
"""

import os
from typing import Dict


class AdicaoAdministradorView:
    """
    Classe de interface para adicionar administradores no sistema.

    Esta classe lida com a entrada de dados do usuário e exibe mensagens de sucesso ou falha.
    """

    def adicionar_administrador_view(self) -> Dict:
        """
        Coleta os dados necessários para adicionar um novo administrador e
        os retorna como um dicionário.

        :return: Dicionário contendo os dados do novo administrador.
        :rtype: Dict
        """

        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo administrador \n")
        nome = input("Digite o nome: ")
        username = input("Digite o username: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")

        # Criando dicionario do adm
        novo_administrador = {"Nome": nome, "Email": email, "Senha": senha, "Username": username}

        return novo_administrador

    def adicionar_administrador_sucesso(self, adm: Dict) -> None:
        """
        Exibe uma mensagem de sucesso ao adicionar um administrador.

        :param adm: Dicionário contendo os dados do administrador recém-adicionado.
        :type adm: Dict
        """

        os.system("cls||clear")

        mensagem_sucesso = f"""
Administrador cadastrado com sucesso!

\tNome: {adm['Nome']}
\tEmail: {adm['Email']}
"""
        print(mensagem_sucesso)

    def adicionar_administrador_falha(self, error: str) -> None:
        """
        Exibe uma mensagem de erro ao falhar na adição de um administrador.

        :param error: Descrição do erro ocorrido.
        :type error: str
        """

        os.system("cls||clear")

        mensagem_falha = f"""
Falha ao cadastrar administrador!

\tErro: {error}
"""
        print(mensagem_falha)
