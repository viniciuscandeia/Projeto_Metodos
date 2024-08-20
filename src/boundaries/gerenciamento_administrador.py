import uuid
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from src.entities.administrador_entity import Administrador
from src.business.usuario_controller import UsuarioController


class GerenciamentoAdministradores:
    def __init__(self, controller: UsuarioController):
        self.console = Console()
        self.controller = controller

    def exibir_menu(self):
        while True:
            self.console.print(
                Panel("MENU PRINCIPAL", style="bold cyan", expand=False))

            table = Table(show_header=True, header_style="bold")
            table.add_column("Opção", style="bold green", width=6)
            table.add_column("Descrição")

            table.add_row("1", "Adicionar Administrador")
            table.add_row("2", "Listar todos os Administradores")
            table.add_row("[bold red]3[/bold red]", "Sair")
            self.console.print(table)

            opcao = Prompt.ask(
                "[bold yellow]Escolha uma opção[/bold yellow]",
                choices=["1", "2", "3"], show_choices=False)

            match opcao:
                case "1":
                    self.adicionar_administrador()
                case "2":
                    self.listar_administradores()
                case "3":
                    self.console.print(
                        "[bold red]Encerrando o programa...[/bold red]")
                    break
                case _:
                    self.console.print(
                        "[bold red]Opção inválida. Tente novamente.[/bold red]")

    def adicionar_administrador(self):
        self.console.print(
            Panel("ADICIONAR Administrador", style="bold cyan", expand=False))

        nome = Prompt.ask(
            "[bold yellow]Digite o nome do Administrador[/bold yellow]")
        email = Prompt.ask(
            "[bold yellow]Digite o email do Administrador[/bold yellow]")

        adm_id = str(uuid.uuid4().int >> 64)

        novo_administrador = Administrador(adm_id, nome, email)
        self.controller.adicionar_administrador(
            novo_administrador=novo_administrador)
        self.console.print(
            "[bold green]Administrador adicionado com sucesso![/bold green]")

    def listar_administradores(self):
        self.console.print(
            Panel("LISTA DE ADMINISTRADORES", style="bold cyan", expand=False))
        administradores: list[Administrador] = self.controller.listar_administradores(
        )

        if administradores:
            table = Table(show_header=True, header_style="bold")
            table.add_column("ID", style="dim")
            table.add_column("Nome")
            table.add_column("Email")

            for admin in administradores:
                table.add_row(admin.id_usuario, admin.nome, admin.email)

            self.console.print(table)
        else:
            self.console.print(
                "[bold red]Nenhum Administrador cadastrado.[/bold red]")
