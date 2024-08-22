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
        adm_id = str(uuid.uuid4().int >> 64)

        # Criando dicionario do adm
        novo_administrador = {"nome": nome, "email": email, "adm_id": adm_id}

        return novo_administrador

    def adicionar_administrador_sucesso(self, adm: Dict) -> None:
        os.system("cls||clear")

        mensagem_sucesso = f"""
            Administrador cadastrado com sucesso!

                ADM_ID: {adm['adm_id']}
                Nome: {adm['nome']}
                Email: {adm['email']}
            """
        print(mensagem_sucesso)

    def adicionar_administrador_falha(self, error: str) -> None:
        os.system("cls||clear")

        mensagem_falha = f"""
            Falha ao cadastrar administrador!

                Erro: {error}
            """
        print(mensagem_falha)
