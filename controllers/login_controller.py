from services.usuario_service import UsuarioService
from services.vendedor_service import VendedorService

class LoginController:
    def __init__(self):
        self.usuario_service = UsuarioService()
        self.vendedor_service = VendedorService()

    def login(self):
        email = input("Insira o email: ")
        senha = input("Insira a senha: ")
        user = self.usuario_service.search({"email": email, "senha": senha})
        vendedor = self.vendedor_service.search({"email": email, "senha": senha})
        if user:
            user_info = user[0]  # Supondo que user[0] é um dicionário com as informações do usuário
            user_info['is_vendedor'] = False  # Adiciona a chave is_vendedor com valor False
            print("usu normal")
            return user_info
        elif vendedor:
            vendedor_info = vendedor[0]  # Supondo que vendedor[0] é um dicionário com as informações do vendedor
            vendedor_info['is_vendedor'] = True  # Adiciona a chave is_vendedor com valor True
            print( 'vendedor')
            return vendedor_info
        else:
            print("Email ou senha incorretos.")
            return None
