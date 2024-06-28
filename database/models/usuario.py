from database.connection import DatabaseConnection

class Usuario:
    def __init__(self):
        self.collection = DatabaseConnection().get_collection('usuarios')

    def insert(self, usuario):
        self.collection.insert_one(usuario)

    def update(self, usuario_id, updates):
        self.collection.update_one({'id': usuario_id}, {'$set': updates})

    def search(self, query):
        return list(self.collection.find(query))

    def delete(self, usuario_id):
        self.collection.delete_one({'id': usuario_id})
