from models.produto import Produto
from models.favorito import Favorito
from models.compra import Compra
from services.produto_service import ProdutoService
from services.favorito_service import FavoritoService
from services.compra_service import CompraService

class CadastroController:
    def __init__(self, logged_in_user):
        self.logged_in_user = logged_in_user
        self.produto_service = ProdutoService()
        self.favorito_service = FavoritoService()
        self.compra_service = CompraService()

    def cadastro_menu(self):
        while True:
            print("\n1 - Cadastro de Produto")
            print("\n2 - Cadastro de Favorito")
            print("\n3 - Cadastro de Compra")
            print("\n0 - Voltar")
            option = input("\nPor favor digite uma opção: ")

            if option == '1' and self.is_vendedor():
                self.input_produto()
            elif option == '2':
                self.input_favorito()
            elif option == '3':
                self.input_compra()
            elif option == '0':
                break
            else:
                print("Opção inválida ou você não tem permissão para esta ação. Tente novamente.")

    def is_vendedor(self):
        return 'is_vendedor' in self.logged_in_user and self.logged_in_user['is_vendedor']

    def input_produto(self):
        produto = Produto(
            id=input("Insira o ID: "),
            nome=input("Insira o nome: "),
            descricao=input("Insira a descrição: "),
            preco=float(input("Insira o preço: ")),
            quantidade=int(input("Insira a quantidade: ")),
            vendedor_id=self.logged_in_user['id']
        )
        self.produto_service.insert(produto)

    def input_favorito(self):
        favorito = Favorito(
            id=input("Insira o ID: "),
            usuario_id=self.logged_in_user['id'],
            produto_id=input("Insira o ID do produto: ")
        )
        self.favorito_service.insert(favorito)

    def input_compra(self):
        compra = Compra(
            id=input("Insira o ID: "),
            usuario_id=self.logged_in_user['id'],
            produto_id=input("Insira o ID do produto: "),
            data=input("Insira a data (YYYY-MM-DD): "),
            quantidade=int(input("Insira a quantidade: "))
        )
        self.compra_service.insert(compra)
