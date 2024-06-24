from db.connection import MongoDBConnection

class ProdutoService:
    def __init__(self):
        self.db = MongoDBConnection().get_db()

    def insert(self, produto):
        self.db.produtos.insert_one(produto.__dict__)
        
    def listar_todos(self):
        return list(self.db.produtos.find())

    def update(self, produto_id, updates):
        self.db.produtos.update_one({'id': produto_id}, {'$set': updates})

    def search(self, query):
        return list(self.db.produtos.find(query))

    def delete(self, produto_id):
        self.db.produtos.delete_one({'id': produto_id})
