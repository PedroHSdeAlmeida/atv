from db.connection import MongoDBConnection

class FavoritoService:
    def __init__(self):
        self.db = MongoDBConnection().get_db()

    def insert(self, favorito):
        self.db.favoritos.insert_one(favorito.__dict__)

    def update(self, favorito_id, updates):
        self.db.favoritos.update_one({'id': favorito_id}, {'$set': updates})

    def search(self, query):
        return list(self.db.favoritos.find(query))

    def delete(self, favorito_id):
        self.db.favoritos.delete_one({'id': favorito_id})
