from ..views.usuario_views import UsuarioViews


class UsuarioProcessosFacade:

    def __init__(self):
        self.usuario_views = UsuarioViews()

    def tela_inicial(self):
        comando = self.usuario_views.tela_inicial()
        return comando

    def escolher_usuario_adicionar(self):
        comando = self.usuario_views.escolher_usuario_adicionar_view()
        return comando

    def adicionar_administrador(self):


    def editar_processo(self):
        comando = self.usuario_views.editar_view()
        return comando
