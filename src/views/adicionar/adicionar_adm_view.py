import os
import uuid
from typing import Dict


class AdicionarAdministradorView:
    def adicionar_administrador_view(self) -> Dict:
        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo administrador \n")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input('Digite a senha: ')
        _id = str(uuid.uuid4().int >> 64)

        # Criando dicionario do adm
        novo_administrador = {"Nome": nome,
                              "Email": email, "Id": _id, "Senha": senha}

        return novo_administrador

    def adicionar_administrador_sucesso(self, adm: Dict) -> None:
        os.system("cls||clear")

        mensagem_sucesso = f"""
Administrador cadastrado com sucesso!

\tID: {adm["Id"]}
\tNome: {adm['Nome']}
\tEmail: {adm['Email']}
            """
        print(mensagem_sucesso)

    def adicionar_administrador_falha(self, error: str) -> None:
        os.system("cls||clear")

        mensagem_falha = f"""
Falha ao cadastrar administrador!

\tErro: {error}
            """
        print(mensagem_falha)
