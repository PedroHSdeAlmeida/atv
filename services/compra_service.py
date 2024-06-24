from db.connection import MongoDBConnection

class CompraService:
    def __init__(self):
        self.db = MongoDBConnection().get_db()

    def insert(self, compra):
        self.db.compras.insert_one(compra.__dict__)

    def update(self, compra_id, updates):
        self.db.compras.update_one({'id': compra_id}, {'$set': updates})

    def search(self, query):
        return list(self.db.compras.find(query))

    def delete(self, compra_id):
        self.db.compras.delete_one({'id': compra_id})
