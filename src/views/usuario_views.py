import os
import uuid

from ..models.entities.usuario_entity import Usuario
from ..models.repository.usuario_repository import UsuarioRepository


class UsuarioViews:

    def tela_inicial():
        """
        Exibe a tela inicial do sistema cadastral e retorna o comando selecionado pelo usuário.

        :return: Comando digitado pelo usuário.
        :rtype: str
        """

        mensagem = """
    Sistema Cadastral

    1 - Cadastrar Usuario
    2 - Listar Usuario
    3 - Editar Usuario
    4 - Adcionar Loja
    5 - Listar Lojas
    6 - Editar Lojas
    7 - Excluir Lojas
    * Sair - 9
        """

        print(mensagem)
        comando = input("Comando: ")

        return comando

    def adicionar_administrador_view(self) -> dict:
        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo administrador \n")
        nome = input("Digite o nome: ")
        username = input("Digite o username: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")

        # Criando dicionario do adm
        novo_administrador = {
            "Nome": nome,
            "Email": email,
            "Senha": senha,
            "Username": username,
        }

        return novo_administrador

    def adicionar_usuario_sucesso(self, usuario: dict, tipo: str) -> None:
        os.system("cls||clear")

        mensagem_sucesso = f"""
{tipo} cadastrado com sucesso!

\tNome: {usuario['Nome']}
\tEmail: {usuario['Email']}
"""
        print(mensagem_sucesso)

    def adicionar_usuario_falha(self, error: str, tipo: str) -> None:
        os.system("cls||clear")

        mensagem_falha = f"""
Falha ao cadastrar {tipo}!

\tErro: {error}
"""
        print(mensagem_falha)

    def adicionar_gerente_view(self) -> dict:
        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo gerente \n")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        username = input("Digite o username: ")
        senha = input("Digite a senha: ")
        _id_loja = str(uuid.uuid4().int >> 64)
        # Criando dicionario do adm
        novo_gerente = {
            "Nome": nome,
            "Email": email,
            "Senha": senha,
            "Username": username,
            "Id_loja": _id_loja,
        }

        return novo_gerente

    def adicionar_vendedor_view(self) -> dict:
        os.system("cls||clear")

        # Coletando dados
        print("Adicionar novo vendedor \n")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")
        username = input("Digite o username: ")
        _id_loja = str(uuid.uuid4().int >> 64)

        novo_vendedor = {
            "Nome": nome,
            "Email": email,
            "Senha": senha,
            "Id_loja": _id_loja,
            "Username": username,
        }

        return novo_vendedor

    def escolher_usuario_adicionar_view():

        mensagem = """
    Cadastrar Usuario

    * Cadastrar Administrador - 1
    * Cadastrar Gerente - 2
    * Cadastrar Vendedor - 3
    * Voltar - 9
        """

        print(mensagem)
        comando = input("Comando: ")

        return comando

    def editar_administrador_view(self) -> dict:

        os.system("cls||clear")

        # Coletando dados
        print("Editar administrador \n")
        print("(Caso nao queira editar um campo, apenas deixe em branco)")
        id_usuario = input("Digite o id do usuario para editar: ")
        nome = input("Digite o nome: ")
        username = input("Digite o username: ")
        email = input("Digite o email: ")

        novo_administrador = {
            "id": id_usuario,
            "Nome": nome,
            "Username": username,
            "Email": email,
        }

        # Filtrando para remover itens onde o valor é vazio
        novo_administrador = {k: v for k, v in novo_administrador.items() if v}

        return novo_administrador

    def editar_administrador_sucesso(self) -> None:
        os.system("cls||clear")

        mensagem_sucesso = """
Administrador editado com sucesso!

"""
        print(mensagem_sucesso)

    def editar_administrador_falha(self, error: str) -> None:
        # os.system("cls||clear")

        mensagem_falha = f"""
Falha ao editar administrador!

\tErro: {error}
"""
        print(mensagem_falha)

    def selecionar_usuario_editar_usuario_view():
        mensagem = """
    Editar Usuario

    * Editar Administradores - 1
    * Editar Gerentes - 2
    * Editar Vendedores - 3
    * Voltar - 9
        """

        print(mensagem)
        comando = input("Comando: ")

        return comando

    def listar_usuarios_escolher_view():
        """
        Exibe o menu de opções para listar usuários e retorna o comando selecionado pelo usuário.

        :return: Comando digitado pelo usuário.
        :rtype: str
        """

        mensagem = """
    Listar Usuario

    * Listar Administradores - 1
    * Listar Gerentes - 2
    * Listar Vendedores - 3
    * Voltar - 9
        """

        print(mensagem)
        comando = input("Comando: ")

        return comando

    def lista_preenchida(self, repositorio: UsuarioRepository, tipo: str) -> None:
        """
        Exibe a lista de usuários quando a mesma não está vazia.

        A lista de usuários é obtida do repositório que é passado como argumento
        e exibida no formato de nome e email.
        """

        os.system("cls||clear")

        repositorio_usuario: list[Usuario] = repositorio.pegar_repositorio()

        mensagem = f"""
Lista de {tipo}

"""

        # Usando join para eficiência na criação da string
        lista: str = "\n".join(
            [
                f"\t- {usuario.id} {usuario.nome}: {usuario.email}"
                for usuario in repositorio_usuario
            ]
        )

        print(mensagem + lista)

    def lista_vazia(self, tipo: str) -> None:
        """
        Exibe uma mensagem informando que a lista de usuários está vazia.
        """

        os.system("cls||clear")

        mensagem = f"""
Lista vazia de {tipo}.
"""
        print(mensagem)

    def selecionar_usuario_edicao_loja_view():
        mensagem = """
        Editar Loja

        * 1 - Editar Lojas como adm
        * 2 - Editar uma loja como gerente
        * 3 - Buscar uma loja como gerente
        * Voltar - 9
            """

        print(mensagem)
        comando = input("Comando: ")

        return comando

    def selecionar_usuario_excluir_loja_view():
        mensagem = """
        Excluir Loja

        * Excluir Loja como administrador - 1
        * Voltar - 9 """

        print(mensagem)

        comando = input('Comando: ')
        return comando

    def selecionar_usuario_listar_loja_view():
        mensagem = """
        Listar Lojas

        * 1 - Listar Lojas como adm
        * 2 - Buscar uma loja como adm
        * 3 - Bucar uma loja como gerente
        * Voltar - 9
            """

        print(mensagem)
        comando = input("Comando: ")

        return comando
