from menus.user_menu import UserMenu
from menus.seller_menu import SellerMenu
from database.models.usuario import Usuario
from database.models.vendedor import Vendedor

class MainMenu:
    def display(self):
        while True:
            print("\n1 - Login")
            print("\n2 - Cadastro")
            print("\n0 - Sair")
            option = input("\nPor favor digite uma opção: ")

            if option == '1':
                self.login_menu()
            elif option == '2':
                self.cadastro_menu()
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def login_menu(self):
        email = input("Insira o email: ")
        senha = input("Insira a senha: ")

        usuario_model = Usuario()
        user = usuario_model.search({"email": email, "senha": senha})

        vendedor_model = Vendedor()
        seller = vendedor_model.search({"email": email, "senha": senha})

        if user:
            print(f"Bem-vindo, {user[0]['nome']}!")
            user_menu = UserMenu(user[0])
            user_menu.display()
        elif seller:
            print(f"Bem-vindo, {seller[0]['nome']}!")
            seller_menu = SellerMenu(seller[0])
            seller_menu.display()
        else:
            print("Email ou senha incorretos.")

    def cadastro_menu(self):
        print("\n1 - Cadastro de Usuário")
        print("\n2 - Cadastro de Vendedor")
        option = input("\nPor favor digite uma opção: ")

        if option == '1':
            self.input_usuario()
        elif option == '2':
            self.input_vendedor()
        else:
            print("Opção inválida. Tente novamente.")

    def input_usuario(self):
        usuario_model = Usuario()
        usuario = {
            "id": input("Insira o ID: "),
            "nome": input("Insira o nome: "),
            "email": input("Insira o email: "),
            "senha": input("Insira a senha: "),
            "endereço": input("Insira o endereço: ")
        }
        usuario_model.insert(usuario)

    def input_vendedor(self):
        vendedor_model = Vendedor()
        vendedor = {
            "id": input("Insira o ID: "),
            "nome": input("Insira o nome: "),
            "email": input("Insira o email: "),
            "senha": input("Insira a senha: "),
            "endereço": input("Insira o endereço: ")
        }
        vendedor_model.insert(vendedor)
