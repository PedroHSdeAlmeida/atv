from db.connection import MongoDBConnection

class VendedorService:
    def __init__(self):
        self.db = MongoDBConnection().get_db()

    def insert(self, vendedor):
        self.db.vendedores.insert_one(vendedor.__dict__)

    def update(self, vendedor_id, updates):
        self.db.vendedores.update_one({'id': vendedor_id}, {'$set': updates})

    def search(self, query):
        return list(self.db.vendedores.find(query))

    def delete(self, vendedor_id):
        self.db.vendedores.delete_one({'id': vendedor_id})
