import pymongo
from pymongo.server_api import ServerApi


class MongoConexion:
    def __init__(self, url, dbname, cluster):
        self.url = url
        self.dbname = dbname
        self.cluster=cluster
        self.client=None
        self.db=None
    def conect(self):
        self.client = pymongo.MongoClient(self.url, server_api=ServerApi('1'))
        try:
            self.client.server_info()
        except Exception as e:
            print("Error en datos")
        else:
            print(f"Conectado al cliente MongoDB {self.cluster}")
            print(f"Buscando bd {self.dbname}....")
            if self.dbname in self.client.list_database_names():
                self.db = self.client[self.dbname]
                print(f"Conectado a {self.dbname}")
            else:
                print(f"Base de datos no encontrada")
                print(f"Creando base de datos {self.dbname} ")
                self.db = self.client[self.dbname]
                print(f"{self.dbname} creada y conectada")

    def insert_one(self, collection, data):
        coll = self.db[collection]
        coll.insert_one(data)
        if self.find_one(collection,data):
            print("Objeto insertado")
        else:
            print("Error")

    def find_one(self, collection, query={}):
        coll = self.db[collection]
        return coll.find_one(query)

    def find_many(self, collection, query={}):
        coll = self.db[collection]
        return coll.find(query)

    def update_one(self, collection, query, new_values):
        coll = self.db[collection]
        coll.update_one(query, {"$set": new_values})

    def delete_one(self, collection, query):
        coll = self.db[collection]
        coll.delete_one(query)

    def delete_many(self, collection, query):
        coll = self.db[collection]
        coll.delete_many(query)


if __name__ == "__main__":
    mongo_object = MongoConexion("mongodb+srv://pablo:1010@cluster0.qfgfj6v.mongodb.net/?retryWrites=true&w=majority")
    if (mongo_object.conecDB("mydba")):
        pass
    else:
        print("No hay bd")

    mongo_object.conecCollec("Clientes")
    data = {'nombre': "Sebastian"}
    mongo_object.insert(data)
