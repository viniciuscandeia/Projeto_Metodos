import os
import uuid
from typing import Dict


class AdicionarVendedorView:
    def adicionar_vendedor_view(self) -> Dict:
        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo vendedor \n")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input('Digite a senha: ')
        _id = str(uuid.uuid4().int >> 64)
        _id_loja = str(uuid.uuid4().int >> 64)

        novo_vendedor = {"Nome": nome, "Email": email,
                         "Id": _id, "Senha": senha, "Id_loja": _id_loja}

        return novo_vendedor

    def adicionar_vendedor_sucesso(self, adm: Dict) -> None:
        os.system("cls||clear")

        mensagem_sucesso = f"""
Vendedor cadastrado com sucesso!

\tID: {adm["Id"]}
\tNome: {adm['Nome']}
\tEmail: {adm['Email']}
            """
        print(mensagem_sucesso)

    def adicionar_vendedor_falha(self, error: str) -> None:
        os.system("cls||clear")

        mensagem_falha = f"""
Falha ao cadastrar vendedor!

\tErro: {error}
            """
        print(mensagem_falha)
