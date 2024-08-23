import os
import uuid
from typing import Dict


class AdicionarGerenteView:
    def adicionar_gerente_view(self) -> Dict:
        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo gerente \n")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")
        _id = str(uuid.uuid4().int >> 64)
        _id_loja = str(uuid.uuid4().int >> 64)
        # Criando dicionario do adm
        novo_gerente = {
            "Nome": nome,
            "Email": email,
            "Id": _id,
            "Senha": senha,
            "Id_loja": _id_loja,
        }

        return novo_gerente

    def adicionar_gerente_sucesso(self, adm: Dict) -> None:
        os.system("cls||clear")

        mensagem_sucesso = f"""
Gerente cadastrado com sucesso!

\tID: {adm["Id"]}
\tNome: {adm['Nome']}
\tEmail: {adm['Email']}
"""
        print(mensagem_sucesso)

    def adicionar_gerente_falha(self, error: str) -> None:
        os.system("cls||clear")

        mensagem_falha = f"""
Falha ao cadastrar gerente!

\tErro: {error}
            """
        print(mensagem_falha)
