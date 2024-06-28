from database.models.produto import Produto
from database.models.vendedor import Vendedor

class SellerMenu:
    def __init__(self, seller):
        self.seller = seller

    def display(self):
        while True:
            print("\n1 - Produtos")
            print("\n2 - Atualizar Vendedor")
            print("\n0 - Voltar")
            option = input("\nPor favor digite uma opção: ")

            if option == '1':
                self.produto_menu()
            elif option == '2':
                self.atualizar_vendedor()
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
                
    def atualizar_vendedor(self):
        usuario_model = Vendedor()
        usuario_id = self.seller["id"]
        updates = {
            "nome": input("Insira o novo nome: "),
            "email": input("Insira o novo email: "),
            "senha": input("Insira a nova senha: "),
            "endereco": input("Insira o novo endereço: ")
        }
        usuario_model.update(usuario_id, updates)
        print("Vendedor atualizado com sucesso!")

    def produto_menu(self):
        produto_model = Produto()
        while True:
            print("\n1 - Adicionar Produto")
            print("\n2 - Atualizar Produto")
            print("\n3 - Remover Produto")
            print("\n4 - Listar Produtos")
            print("\n0 - Voltar")
            option = input("\nPor favor digite uma opção: ")

            if option == '1':
                produto = {
                    "id": input("Insira o ID do produto: "),
                    "nome": input("Insira o nome do produto: "),
                    "descrição": input("Insira a descrição do produto: "),
                    "preço": float(input("Insira o preço do produto: ")),
                    "quantidade": int(input("Insira a quantidade do produto: ")),
                    "vendedor_id": self.seller["id"]
                }
                produto_model.insert(produto)
            elif option == '2':
                produto_id = input("Insira o ID do produto: ")
                updates = {
                    "nome": input("Insira o novo nome: "),
                    "descrição": input("Insira a nova descrição: "),
                    "preço": float(input("Insira o novo preço: ")),
                    "quantidade": int(input("Insira a nova quantidade: "))
                }
                produto_model.update(produto_id, updates)
            elif option == '3':
                produto_id = input("Insira o ID do produto: ")
                produto_model.delete(produto_id)
            elif option == '4':
                produtos = produto_model.search({"vendedor_id": self.seller["id"]})
                print("\n Meus produtos:")
                for produto in produtos:
                    print(f"\n Id do produto: {produto['id']} \n Nome do produto: {produto['nome']}\n Descrição: {produto['descrição']}\n Preço: R${produto['preço']:,.2f}\n Quantidade: {produto['quantidade']}")
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")
