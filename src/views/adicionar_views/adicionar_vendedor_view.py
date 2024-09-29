"""
Módulo para a visualização de adição de vendedores no sistema.

Este módulo define a classe `AdicaoVendedorView`, que lida com a entrada de dados do usuário
para adicionar novos vendedores e exibe mensagens de sucesso ou falha.
"""

import os
import uuid
from typing import Dict


class AdicaoVendedorView:
    """
    Classe de interface para adicionar vendedores no sistema.

    Esta classe lida com a entrada de dados do usuário e exibe mensagens de sucesso ou falha.
    """

    def adicionar_vendedor_view(self) -> Dict:
        """
        Coleta os dados necessários para adicionar um novo vendedor e os retorna como um dicionário.

        :return: Dicionário contendo os dados do novo vendedor.
        :rtype: Dict
        """

        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo vendedor \n")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")
        username = input('Digite o username: ')
        _id_loja = str(uuid.uuid4().int >> 64)

        novo_vendedor = {
            "Nome": nome,
            "Email": email,
            "Senha": senha,
            "Id_loja": _id_loja,
            "Username": username,
        }

        return novo_vendedor

    def adicionar_vendedor_sucesso(self, adm: Dict) -> None:
        """
        Exibe uma mensagem de sucesso ao adicionar um vendedor.

        :param adm: Dicionário contendo os dados do vendedor recém-adicionado.
        :type adm: Dict
        """

        os.system("cls||clear")

        mensagem_sucesso = f"""
Vendedor cadastrado com sucesso!

\tNome: {adm['Nome']}
\tEmail: {adm['Email']}
            """
        print(mensagem_sucesso)

    def adicionar_vendedor_falha(self, error: str) -> None:
        """
        Exibe uma mensagem de erro ao falhar na adição de um vendedor.

        :param error: Descrição do erro ocorrido.
        :type error: str
        """
        os.system("cls||clear")

        mensagem_falha = f"""
Falha ao cadastrar vendedor!

\tErro: {error}
            """
        print(mensagem_falha)
