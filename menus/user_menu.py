from database.models.favorito import Favorito
from database.models.compra import Compra
from database.models.produto import Produto
from database.models.usuario import Usuario

class UserMenu:
    def __init__(self, user):
        self.user = user

    def display(self):
        while True:
            print("\n1 - Favoritos")
            print("\n2 - Produtos")
            print("\n4 - Atualizar usuario")
            print("\n0 - Voltar")
            option = input("\nPor favor digite uma opção: ")

            if option == '1':
                self.favorito_menu()
            elif option == '2':
                self.produto_menu()
            elif option == '4':
                self.atualizar_usuario()
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def produto_menu(self):
        while True:
            print("\n1 - Comprar Produto")
            print("\n2 - Listar Produtos")
            print("\n0 - Voltar")
            option = input("\nPor favor digite uma opção: ")

            if option == '1':
                self.comprar_produto()
            elif option == '2':
                self.listar_produtos()
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def atualizar_usuario(self):
        usuario_model = Usuario()
        usuario_id = self.user["id"]
        updates = {
            "nome": input("Insira o novo nome: "),
            "email": input("Insira o novo email: "),
            "senha": input("Insira a nova senha: "),
            "endereco": input("Insira o novo endereço: ")
        }
        usuario_model.update(usuario_id, updates)
        print("Usuário atualizado com sucesso!")

    def favorito_menu(self):
        favorito_model = Favorito()
        while True:
            print("\n1 - Adicionar Favorito")
            print("\n2 - Remover Favorito")
            print("\n3 - Listar Favoritos")
            print("\n0 - Voltar")
            option = input("\nPor favor digite uma opção: ")

            if option == '1':
                favorito = {
                    "id": input("Insira o ID: "),
                    "usuario_id": self.user["id"],
                    "produto_id": input("Insira o ID do produto: ")
                }
                favorito_model.insert(favorito)
            elif option == '2':
                favorito_id = input("Insira o ID do favorito: ")
                favorito_model.delete(favorito_id)
            elif option == '3':
                favoritos = favorito_model.search({"usuario_id": self.user["id"]})
                for fav in favoritos:
                    print(fav)
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def comprar_produto(self):
        compra_model = Compra()
        compra = {
            "id": input("Insira o ID da compra: "),
            "usuario_id": self.user["id"],
            "produto_id": input("Insira o ID do produto: "),
            "data": input("Insira a data (YYYY-MM-DD): "),
            "quantidade": int(input("Insira a quantidade: "))
        }
        compra_model.insert(compra)

    def listar_produtos(self):
        produto_model = Produto()
        produtos = produto_model.search({})
        print("\n Listagem de produtos:")
        for produto in produtos:
            print(f"\n Id do produto: {produto['id']} \n Nome do produto: {produto['nome']}\n Descrição: {produto['descrição']}\n Preço: R${produto['preço']:,.2f}\n Quantidade: {produto['quantidade']}")