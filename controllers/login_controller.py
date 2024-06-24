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
            return user[0]
        elif vendedor:
            return vendedor[0]
        else:
            print("Email ou senha incorretos.")
            return None
