from database.connection import DatabaseConnection

class Compra:
    def __init__(self):
        self.collection = DatabaseConnection().get_collection('compras')

    def insert(self, compra):
        self.collection.insert_one(compra)

    def update(self, compra_id, updates):
        self.collection.update_one({'id': compra_id}, {'$set': updates})

    def search(self, query):
        return list(self.collection.find(query))

    def delete(self, compra_id):
        self.collection.delete_one({'id': compra_id})
