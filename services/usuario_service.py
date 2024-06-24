from db.connection import MongoDBConnection

class UsuarioService:
    def __init__(self):
        self.db = MongoDBConnection().get_db()

    def insert(self, usuario):
        self.db.usuarios.insert_one(usuario.__dict__)

    def update(self, usuario_id, updates):
        self.db.usuarios.update_one({'id': usuario_id}, {'$set': updates})

    def search(self, query):
        return list(self.db.usuarios.find(query))

    def delete(self, usuario_id):
        self.db.usuarios.delete_one({'id': usuario_id})
