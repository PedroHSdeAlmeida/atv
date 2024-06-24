from controllers.login_controller import LoginController
from controllers.cadastro_controller import CadastroController
from services.produto_service import ProdutoService
from models.usuario import Usuario
from models.vendedor import Vendedor
from services.usuario_service import UsuarioService
from services.vendedor_service import VendedorService

class MainController:
    def __init__(self):
        self.logged_in_user = None
        self.usuario_service = UsuarioService()
        self.vendedor_service = VendedorService()
        self.produto_service = ProdutoService()

    def main_menu(self):
        while True:
            print("\n1 - Login")
            print("\n2 - Cadastro")
            print("\n3 - Listar Produtos")
            print("\n0 - Sair")
            option = input("\nPor favor digite uma opção: ")

            if option == '1':
                self.login_menu()
            elif option == '2':
                self.cadastro_menu()
            elif option == '3':
                self.listar_produtos()
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def login_menu(self):
        login_controller = LoginController()
        self.logged_in_user = login_controller.login()
        if self.logged_in_user:
            print(f"Bem-vindo, {self.logged_in_user['nome']}!")
            self.cadastro_menu_logado()

    def cadastro_menu(self):
        print("\n1 - Cadastro de Usuário")
        print("\n2 - Cadastro de Vendedor")
        print("\n0 - Voltar")
        option = input("\nPor favor digite uma opção: ")

        if option == '1':
            self.input_usuario()
        elif option == '2':
            self.input_vendedor()
        elif option == '0':
            return
        else:
            print("Opção inválida. Tente novamente.")

    def cadastro_menu_logado(self):
        while True:
            print("\n1 - Cadastro de Produto")
            print("\n2 - Cadastro de Favorito")
            print("\n3 - Cadastro de Compra")
            print("\n0 - Voltar")
            option = input("\nPor favor digite uma opção: ")

            if option == '1' and self.is_vendedor():
                self.cadastro_controller.input_produto()
            elif option == '2':
                self.cadastro_controller.input_favorito()
            elif option == '3':
                self.cadastro_controller.input_compra()
            elif option == '0':
                break
            else:
                print("Opção inválida ou você não tem permissão para esta ação. Tente novamente.")

    def is_vendedor(self):
        return 'is_vendedor' in self.logged_in_user and self.logged_in_user['is_vendedor']

    def input_usuario(self):
        usuario = Usuario(
            id=input("Insira o ID: "),
            nome=input("Insira o nome: "),
            email=input("Insira o email: "),
            senha=input("Insira a senha: "),
            endereco=input("Insira o endereço: ")
        )
        self.usuario_service.insert(usuario)

    def input_vendedor(self):
        vendedor = Vendedor(
            id=input("Insira o ID: "),
            nome=input("Insira o nome: "),
            email=input("Insira o email: "),
            senha=input("Insira a senha: "),
            endereco=input("Insira o endereço: ")
        )
        self.vendedor_service.insert(vendedor)

    def listar_produtos(self):
        produtos = self.produto_service.listar_todos()
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

if __name__ == '__main__':
    main_controller = MainController()
    main_controller.main_menu()
