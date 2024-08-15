from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from src.features.users.user_entities import Usuario

class InterfaceUsuarios:
    def __init__(self, controle):
        self.controle = controle
        self.console = Console()

    def exibir_menu(self):
        while True:
            self.console.print(
                Panel("MENU PRINCIPAL", style="bold cyan", expand=False))

            table = Table(show_header=True, header_style="bold")
            table.add_column("Opção", style="bold green", width=6)
            table.add_column("Descrição")

            table.add_row("1", "Adicionar usuário")
            table.add_row("2", "Listar todos os usuários")
            table.add_row("[bold red]3[/bold red]", "Sair")
            self.console.print(table)

            opcao = Prompt.ask(
                "[bold yellow]Escolha uma opção[/bold yellow]", choices=["1", "2", "3"], show_choices=False)

            match opcao:
                case "1":
                    self.adicionar_usuario()
                case "2":
                    self.listar_usuarios()
                case "3":
                    self.console.print(
                        "[bold red]Encerrando o programa...[/bold red]")
                    break
                case _:
                    self.console.print(
                        "[bold red]Opção inválida. Tente novamente.[/bold red]")

    def adicionar_usuario(self):
        self.console.print(
            Panel("ADICIONAR USUÁRIO", style="bold cyan", expand=False))
        id_usuario = Prompt.ask(
            "[bold yellow]Digite o ID do usuário[/bold yellow]")
        nome = Prompt.ask(
            "[bold yellow]Digite o nome do usuário[/bold yellow]")
        email = Prompt.ask(
            "[bold yellow]Digite o email do usuário[/bold yellow]")

        usuario = Usuario(id_usuario, nome, email)
        self.controle.adicionar_usuario(usuario)
        self.console.print(
            "[bold green]Usuário adicionado com sucesso![/bold green]")

    def listar_usuarios(self):
        self.console.print(
            Panel("LISTA DE USUÁRIOS", style="bold cyan", expand=False))
        usuarios = self.controle.listar_usuarios()
        if usuarios:
            table = Table(show_header=True, header_style="bold")
            table.add_column("ID", style="dim")
            table.add_column("Nome")
            table.add_column("Email")

            for usuario in usuarios:
                table.add_row(usuario.id_usuario, usuario.nome, usuario.email)

            self.console.print(table)
        else:
            self.console.print(
                "[bold red]Nenhum usuário cadastrado.[/bold red]")
