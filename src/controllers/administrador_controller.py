from src.controllers.relatorios.relatorio_pdf import Relatorio, RelatorioPdf
from .relatorios.relatorio_html import RelatorioHTML
from ..models.excecoes import (
    UsuarioErroInesperado,
    UsuarioIntegridadeError,
    UsuarioNaoEncontrado,
    UsuarioRegistroError,
)

from ..models.entities.administrador_entity import Administrador
from ..models.entities_db.usuario_db_entity import UsuarioBD
from ..lib.validar_inputs import ValidarInputs
from ..factory.persistencia_factory import PersistenciaFactory


class AdministradorController:
    def __init__(self):
        self.adm_repositorio = PersistenciaFactory.criar_persistencia('adm_db')

    def adicionar(self, novo_usuario: dict) -> dict:
        try:
            self.__validar_campos(novo_usuario)
            self._criar_entidade(novo_usuario)
            resposta = self.__formatar_resposta(novo_usuario)

            return {"Sucesso": True, "Mensagem": resposta}
        except ValueError as erro:
            return {"Sucesso": False, "ERROR": str(erro)}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos(self, novo_usuario: dict) -> None:
        try:
            ValidarInputs.validar_nome(novo_usuario)
            ValidarInputs.validar_email(novo_usuario)
            ValidarInputs.validar_senha(novo_usuario)
            ValidarInputs.validar_username(novo_usuario)
        except ValueError as erro:
            raise ValueError(str(erro)) from None

    def __formatar_resposta(self, novo_usuario: dict) -> dict:
        return {
            "Tipo": self.__class__.__name__.replace("Adicionar", "").replace(
                "Controller", ""
            ),
            "Nome": novo_usuario["Nome"],
            "Username": novo_usuario["Username"],
            "Email": novo_usuario["Email"],
        }

    def editar(self, usuario_editado: dict) -> dict:
        try:
            self.__validar_campos_editar(usuario_editado)
            entidade_editada = self._editar_entidade(usuario_editado)
            return {"Sucesso": True, "Mensagem": entidade_editada}
        except ValueError as erro:
            return {"Sucesso": False, "ERROR": str(erro)}
        except Exception as exception:
            return {"Sucesso": False, "ERROR": str(exception)}

    def __validar_campos_editar(self, usuario_editado) -> None:
        try:
            ValidarInputs.validar_id(usuario_editado)

            if ("Nome" in usuario_editado):
                ValidarInputs.validar_nome(usuario_editado)

            if ("Email" in usuario_editado):
                ValidarInputs.validar_email(usuario_editado)

            if ("Username" in usuario_editado):
                ValidarInputs.validar_username(usuario_editado)
        except ValueError as erro:
            raise ValueError(str(erro)) from None

    def _criar_entidade(self, novo_usuario: dict) -> None:
        nome: str = novo_usuario["Nome"]
        email: str = novo_usuario["Email"]
        senha: str = novo_usuario["Senha"]
        username: str = novo_usuario['Username']

        objeto_adm = Administrador(nome, username, email, senha)

        try:
            self.adm_repositorio.registrar_administrador(objeto_adm)
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None

    def _editar_entidade(self, administrador_editado: dict) -> None:
        try:
            self.adm_repositorio.editar_administrador(administrador_editado)
        except (
            UsuarioIntegridadeError,
            UsuarioRegistroError,
            UsuarioErroInesperado,
            UsuarioNaoEncontrado,
        ) as erro:
            raise Exception(str(erro)) from None

    def listar(self) -> bool:
        repositorio: list[UsuarioBD] = self.adm_repositorio.pegar_repositorio()
        if repositorio:
            return True
        return False

    def enviar_relatorio(self):
        try:
            relatorio = RelatorioPdf(adm_repositorio=PersistenciaFactory.criar_persistencia('adm_db'),
                                     gerente_repositorio=PersistenciaFactory.criar_persistencia(
                                         'gerente_db'),
                                     vendedores_repositorio=PersistenciaFactory.criar_persistencia('vendedor_db'))
            relatorio.gerar_relatorio()
        except Exception as e:
            raise e
