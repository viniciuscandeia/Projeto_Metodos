"""
Módulo para a visualização de adição de gerentes no sistema.

Este módulo define a classe `AdicionarGerenteView`, que lida com a entrada de dados do usuário
para adicionar novos gerentes e exibe mensagens de sucesso ou falha.
"""

import os
import uuid
from typing import Dict


class AdicionarGerenteView:
    """
    Classe de interface para adicionar gerentes no sistema.

    Esta classe lida com a entrada de dados do usuário e exibe mensagens de sucesso ou falha.
    """

    def adicionar_gerente_view(self) -> Dict:
        """
        Coleta os dados necessários para adicionar um novo gerente e os retorna como um dicionário.

        :return: Dicionário contendo os dados do novo gerente.
        :rtype: Dict
        """

        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo gerente \n")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")
        _id_loja = str(uuid.uuid4().int >> 64)
        # Criando dicionario do adm
        novo_gerente = {
            "Nome": nome,
            "Email": email,
            "Senha": senha,
            "Id_loja": _id_loja,
        }

        return novo_gerente

    def adicionar_gerente_sucesso(self, adm: Dict) -> None:
        """
        Exibe uma mensagem de sucesso ao adicionar um gerente.

        :param adm: Dicionário contendo os dados do gerente recém-adicionado.
        :type adm: Dict
        """

        os.system("cls||clear")

        mensagem_sucesso = f"""
Gerente cadastrado com sucesso!

\tNome: {adm['Nome']}
\tEmail: {adm['Email']}
"""
        print(mensagem_sucesso)

    def adicionar_gerente_falha(self, error: str) -> None:
        """
        Exibe uma mensagem de erro ao falhar na adição de um gerente.

        :param error: Descrição do erro ocorrido.
        :type error: str
        """

        os.system("cls||clear")

        mensagem_falha = f"""
Falha ao cadastrar gerente!

\tErro: {error}
            """
        print(mensagem_falha)
