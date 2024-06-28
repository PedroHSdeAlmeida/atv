from database.connection import DatabaseConnection

class Favorito:
    def __init__(self):
        self.collection = DatabaseConnection().get_collection('favoritos')

    def insert(self, favorito):
        self.collection.insert_one(favorito)

    def update(self, favorito_id, updates):
        self.collection.update_one({'id': favorito_id}, {'$set': updates})

    def search(self, query):
        return list(self.collection.find(query))

    def delete(self, favorito_id):
        self.collection.delete_one({'id': favorito_id})
