"""
Módulo que define exceções específicas para operações relacionadas a usuários.

Este módulo contém classes de exceções personalizadas que são usadas para tratar
erros relacionados ao registro e manipulação de usuários no sistema.

Classes:
- UsuarioRegistroError: Exceção base para erros ocorridos durante o registro de um usuário.
- UsuarioIntegridadeError: Exceção para erros de integridade de dados ao registrar um usuário.
- UsuarioErro: Exceção base para erros gerais relacionados a usuários.
- UsuarioNaoEncontrado: Exceção para casos onde um usuário não é encontrado no sistema.
- UsuarioErroInesperado: Exceção para erros inesperados ao lidar com usuários.
"""


class UsuarioRegistroError(Exception):
    """
    Exceção específica para erros ao registrar um usuário.

    Esta exceção é lançada quando ocorre um erro durante o processo de registro
    de um usuário no sistema.
    """


class UsuarioIntegridadeError(UsuarioRegistroError):
    """
    Exceção específica para erros de integridade de dados ao registrar um usuário.

    Esta exceção é lançada quando há problemas relacionados à integridade dos dados,
    como violações de restrições de unicidade ou erros de validação ao registrar um usuário.
    """


class UsuarioErro(Exception):
    """
    Exceção base para erros relacionados ao usuário.

    Esta é a classe base para todas as exceções relacionadas a operações e
    problemas que envolvem usuários no sistema.
    """


class UsuarioNaoEncontrado(UsuarioErro):
    """
    Exceção para quando um usuário não é encontrado.

    Esta exceção é lançada quando uma operação falha devido à ausência de um
    usuário específico no sistema.
    """


class UsuarioErroInesperado(UsuarioErro):
    """
    Exceção para erros inesperados ao lidar com usuários.

    Esta exceção é lançada para capturar e tratar erros inesperados que ocorrem
    durante operações relacionadas a usuários que não se enquadram em categorias
    específicas de erro.
    """
