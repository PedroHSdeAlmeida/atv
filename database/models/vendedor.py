from database.connection import DatabaseConnection

class Vendedor:
    def __init__(self):
        self.collection = DatabaseConnection().get_collection('vendedores')

    def insert(self, vendedor):
        self.collection.insert_one(vendedor)

    def update(self, vendedor_id, updates):
        self.collection.update_one({'id': vendedor_id}, {'$set': updates})

    def search(self, query):
        return list(self.collection.find(query))

    def delete(self, vendedor_id):
        self.collection.delete_one({'id': vendedor_id})
