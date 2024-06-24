from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://pedrohsalmeida2004:senha@ex2.bf67ryk.mongodb.net/?retryWrites=true&w=majority&appName=ex2')
        self.db = self.client['mercado_livre']

    def get_db(self):
        return self.db
