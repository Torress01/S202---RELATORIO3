import pymongo

from dataset.pokemon_dataset import dataset


class Database:
    def __init__(self, database, collection):
        self.collection = None
        self.db = None
        self.clusterConnection = None
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection_string = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def reset_database(self):
        try:
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)