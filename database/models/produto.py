from database.connection import DatabaseConnection

class Produto:
    def __init__(self):
        self.collection = DatabaseConnection().get_collection('produtos')

    def insert(self, produto):
        self.collection.insert_one(produto)

    def update(self, produto_id, updates):
        self.collection.update_one({'id': produto_id}, {'$set': updates})

    def search(self, query):
        return list(self.collection.find(query))

    def delete(self, produto_id):
        self.collection.delete_one({'id': produto_id})
