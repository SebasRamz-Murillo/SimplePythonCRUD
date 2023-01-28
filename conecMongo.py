import pymongo
from pymongo.server_api import ServerApi


class MongoConexion:
    def __init__(self, url):
        self.client = pymongo.MongoClient(url, server_api=ServerApi('1'))

    def check_connection(self):
        try:
            self.client.server_info()
        except Exception:
            return False
        else:
            return True

    def conecDB(self,bd):
        if self.check_connection():
            if bd in self.client.list_database_names():
                self.db = self.client[bd]
                print(f"Conectado a {bd}")
            else:
                self.db = self.client[bd]
                print(f"{bd} creada y conectada")
        else:
            print("No hay conexion")

if __name__ == "__main_<_":
    MongoConexion("aa").conecDB("a")