import uuid
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from src.entities.administrador_entity import Administrador
from src.entities.gerente_entity import Manager
from src.entities.vendedor_entity import Vendedor
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
            table.add_row("3", "Adicionar Gerente")
            table.add_row("4", "Listar todos os Gerentes")
            table.add_row("5", "Adicionar Vendedor")
            table.add_row("6", "Listar todos os Vendedores")
            table.add_row("[bold red]7[/bold red]", "Sair")
            self.console.print(table)

            opcao = Prompt.ask(
                "[bold yellow]Escolha uma opção[/bold yellow]",
                choices=["1", "2", "3", "4", "5", "6", "7"], show_choices=False)

            match opcao:
                case "1":
                    self.adicionar_administrador()
                case "2":
                    self.listar_administradores()
                case "3":
                    self.adicionar_gerente()
                case"4":
                    self.listar_gerentes()
                case"5":
                    self.adicionar_vendedor()
                case "6":
                    self.listar_vendedores()
                case "7":
                    self.console.print(
                        "[bold red]Encerrando o programa...[/bold red]")
                    break
                case _:
                    self.console.print(
                        "[bold red]Opção inválida. Tente novamente.[/bold red]")#TODO Ao invés dessa saída recebemos: "Please select one of the available options"

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
        administradores: list[Administrador] = self.controller.listar_administradores()

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

    def adicionar_gerente(self):
        self.console.print(
            Panel("ADICIONAR Gerente", style="bold cyan", expand=False))
        
        nome = Prompt.ask(
            "[bold yellow]Digite o nome do Gerente[/bold yellow]")
        email = Prompt.ask(
            "[bold yellow]Digite o email do Gerente[/bold yellow]")
        id_loja = Prompt.ask(
            "[bold yellow]Insira o id da loja[/bold yellow]")
        
        id_gerente = str(uuid.uuid4().int >> 64)

        novo_gerente = Manager(id_gerente, nome, email, id_loja)

        self.controller.adicionar_gerente(
            novo_gerente=novo_gerente)
   
        self.console.print(
            "[bold green]Gerente adicionado com sucesso![/bold green]")
            

    def listar_gerentes(self):
        self.console.print(
            Panel("LISTA DE GERENTES", style="bold cyan", expand=False))
        gerentes: list[Manager] = self.controller.listar_gerentes()

        if gerentes:
            table = Table(show_header=True, header_style="bold")
            table.add_column("ID", style="dim")
            table.add_column("Nome")
            table.add_column("Email")
            table.add_column("ID da loja")

            for gerente in gerentes:
                table.add_row(gerente.id_usuario, gerente.nome, gerente.email, gerente.id_loja)

            self.console.print(table)
        else:
            self.console.print(
                "[bold red]Nenhum Gerente cadastrado.[/bold red]")


    def adicionar_vendedor(self):
        self.console.print(
            Panel("ADICIONAR Vendedor", style="bold cyan", expand=False))
        
        nome = Prompt.ask(
            "[bold yellow]Digite o nome do Vendedor[/bold yellow]")
        email = Prompt.ask(
            "[bold yellow]Digite o email do Vendedor[/bold yellow]")
        id_loja = Prompt.ask(
            "[bold yellow]Insira o id da loja[/bold yellow]")
        
        id_vendedor = str(uuid.uuid4().int >> 64)

        novo_vendedor = Vendedor(id_vendedor, nome, email, id_loja)

        self.controller.adicionar_vendedor(
            novo_vendedor=novo_vendedor)
   
        self.console.print(
            "[bold green]Vendedor adicionado com sucesso![/bold green]")
        

    def listar_vendedores(self):
        self.console.print(
            Panel("LISTA DE VENDEDORES", style="bold cyan", expand=False))
        vendedores: list[Vendedor] = self.controller.listar_vendedores()

        if vendedores:
            table = Table(show_header=True, header_style="bold")
            table.add_column("ID", style="dim")
            table.add_column("Nome")
            table.add_column("Email")
            table.add_column("ID da loja")

            for vendedor in vendedores:
                table.add_row(vendedor.id_usuario, vendedor.nome, vendedor.email, vendedor.id_loja)

            self.console.print(table)
        else:
            self.console.print(
                "[bold red]Nenhum Vendedor cadastrado.[/bold red]")