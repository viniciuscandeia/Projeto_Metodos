from src.features.users.user_entities import Usuario

from colorama import Fore, Style, init

# Inicializa a colorama para garantir que funcione em todos os terminais
init(autoreset=True)


class InterfaceUsuarios:
    def __init__(self, controle):
        self.controle = controle

    def exibir_menu(self):
        while True:
            print(Fore.CYAN + "\n========================")
            print("    MENU PRINCIPAL    ")
            print(Fore.CYAN + "========================" + Style.RESET_ALL)
            print(Fore.GREEN + "1 - Adicionar Usuário")
            print(Fore.GREEN + "2 - Listar Todos os Usuários")
            print(Fore.RED + "3 - Sair")
            print(Fore.CYAN + "========================" + Style.RESET_ALL)
            opcao = input(
                Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL)

            match opcao:
                case "1":
                    self.adicionar_usuario()
                case "2":
                    self.listar_usuarios()
                case "3":
                    print(Fore.RED + "Encerrando o programa..." + Style.RESET_ALL)
                    break
                case _:
                    print(
                        Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)

    def adicionar_usuario(self):
        print(Fore.CYAN + "\n========================")
        print("   ADICIONAR USUÁRIO   ")
        print(Fore.CYAN + "========================" + Style.RESET_ALL)
        id_usuario = input(
            Fore.YELLOW + "Digite o ID do usuário: " + Style.RESET_ALL)
        nome = input(
            Fore.YELLOW + "Digite o nome do usuário: " + Style.RESET_ALL)
        email = input(
            Fore.YELLOW + "Digite o email do usuário: " + Style.RESET_ALL)

        usuario = Usuario(id_usuario, nome, email)
        self.controle.adicionar_usuario(usuario)
        print(Fore.GREEN + "Usuário adicionado com sucesso!" + Style.RESET_ALL)

    def listar_usuarios(self):
        print(Fore.CYAN + "\n========================")
        print("  LISTA DE USUÁRIOS   ")
        print(Fore.CYAN + "========================" + Style.RESET_ALL)
        usuarios = self.controle.listar_usuarios()
        if usuarios:
            print(Fore.GREEN + "Usuários cadastrados:" + Style.RESET_ALL)
            for usuario in usuarios:
                print(Fore.YELLOW + str(usuario) + Style.RESET_ALL)
        else:
            print(Fore.RED + "Nenhum usuário cadastrado." + Style.RESET_ALL)
