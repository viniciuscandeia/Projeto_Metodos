from ..entities.usuario_entity import Usuario
from ..entities.entities_db.usuario_db_entity import UsuarioBD
from ..entities.administrador_entity import Administrador
from ..entities.gerente_entity import Gerente
from ..entities.entities_db.loja_db_entity import LojaDB
from ..entities.loja_entity import Loja
from ..excecoes import LojaIntegridadeError, LojaRegistroError, LojaExclusaoError, UsuarioNaoAdministrador
from peewee import IntegrityError
from ..repository.administrador_repository import AdministradorRepositorio
from ..repository.gerente_repository import GerenteRepositorio

class LojaRepository:
    def __init__(self, adm_repositorio:AdministradorRepositorio, gerente_repositorio: GerenteRepositorio) -> None:
        self.adm_repositorio = adm_repositorio
        self.gerente_repositorio = gerente_repositorio

    def get_loja_adm(self, id_adm: int, id_loja: int):
        try:
            usuario = self.adm_repositorio.get_one_administrador(id_adm)

            if usuario: 
                loja = LojaDB.get(LojaDB.id == id_loja)
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise LojaIntegridadeError(f'Erro ao retornar loja: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise LojaRegistroError(f"Erro inesperado ao retornar loja: { str(e)}") from None
        
        return loja
    
    def get_loja_gerente(self, id_gerente: int, id_loja: int)->Loja:
        try:
            loja = LojaDB.get(LojaDB.id==id_loja)
            gerente = self.gerente_repositorio.get_one_gerente(id_gerente)
            #verificar id da loja se é igual ao id do usuario e assim retornar a loja, se nao, retorna erro
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise LojaIntegridadeError(f'Erro ao retornar loja: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise LojaRegistroError(f"Erro inesperado ao retornar loja: { str(e)}") from None
        
        return loja         


    def registrar_loja(self, id_administrador:int, loja: Loja)->LojaDB:
        try:
            usuario = self.adm_repositorio.get_one_administrador(id_administrador)

            if usuario: 
                LojaDB.create(
                    nome = loja['Nome'],
                    endereco=loja['Endereco'],
                )

        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise LojaIntegridadeError(f'Erro ao registrar loja: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise LojaRegistroError(f"Erro inesperado ao registrar loja: { str(e)}") from None
        
        return loja
        
    
    def listar_lojas_adm(self,id_adm:int):
        try:
            usuario = self.adm_repositorio.get_one_administrador(id_adm)

            if usuario: 
                lista_lojas = LojaDB.select()
                return lista_lojas
            
            raise UsuarioNaoAdministrador(f'Usuario de id {id_adm} não é um vendedor')
        except Exception as e:
            # Captura qualquer exceção ao acessar o banco de dados
            print(f"Erro ao acessar o repositório de lojas: {str(e)}")
            return []
        
    
    def editar_loja_administrador(self, id_adm:int, id_loja:int, nova_loja:dict):
        try:
            usuario = self.adm_repositorio.get_one_administrador(id_adm)

            if usuario: 
                loja = self.get_loja_adm(id_adm==id_adm, id_loja=id_loja)
                nova_loja_data = {
                    'nome': nova_loja.get('Nome') if nova_loja.get('Nome') else loja.nome,
                    'endereco': nova_loja.get('Endereco') if nova_loja.get('Endereco') else loja.endereco
                }

                nova_loja_data = {k: v for k, v in nova_loja_data.items() if v is not None}
                LojaDB.update(**nova_loja_data).where(LojaDB.id == id_loja).execute()
                return LojaDB.get(LojaDB.id == id_loja)
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise LojaIntegridadeError(f'Erro ao editar loja: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise LojaRegistroError(f"Erro inesperado ao editar loja: { str(e)}") from None
        
    def editar_loja_gerente(self, id_gerente:int, id_loja:int, nova_loja:dict):
        try:
            usuario = self.gerente_repositorio.get_one_gerente(id_gerente)
            loja = self.get_loja_gerente(id_gerente=id_gerente, id_loja=id_loja)

            #TODO:VERIFICAR SE A LOJA PERTERNCE AO USUARIO

            if usuario: 
                nova_loja_data = {
                    'nome': nova_loja.get('Nome') if nova_loja.get('Nome') else loja.nome,
                    'endereco': nova_loja.get('Endereco') if nova_loja.get('Endereco') else loja.endereco
                }

                nova_loja_data = {k: v for k, v in nova_loja_data.items() if v is not None}
                UsuarioBD.update(**nova_loja_data).where(LojaDB.id == id_loja).execute()
                return LojaDB.get(LojaDB.id == id_loja)
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise LojaIntegridadeError(f'Erro ao editar loja: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise LojaRegistroError(f"Erro inesperado ao editar loja: { str(e)}") from None
        
    def excluir_loja(self, id_loja:int, id_adm):
        try:
            loja = self.get_loja_adm(id_loja=id_loja,id_adm=id_adm)

            if(loja):
                loja.delete_instance()

                return loja
        except IntegrityError as e:
            # Mensagem de erro mais específica para integridade dos dados
            raise LojaExclusaoError(f'Erro ao excluir loja: { str(e)}') from None
        except Exception as e:
            # Captura qualquer outra exceção não esperada
            raise LojaRegistroError(f"Erro inesperado ao excluir loja: { str(e)}") from None