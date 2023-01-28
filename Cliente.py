from Lista import Lista
import os


class Cliente(Lista):
    def __init__(self, rfc="", nombre="", telefono=""):
        super().__init__("Clientes.json")
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.rfc},{self.nombre},{self.telefono}"

    def to_dict(self):
        listaDicc = []
        if type(self) == list:
            for item in self:
                if type(item) == dict:
                    listaDicc.append(item)
                else:
                    listaDicc.append(item.to_dict())
            return listaDicc
        elif type(self) == dict:
            listaDicc.append(self.listas)
        else:
            diccionario = {"rfc": self.rfc, "nombre": self.nombre, "telefono": self.telefono}

            listaDicc.append(diccionario)
            return diccionario

    def from_json(self):
        clientes_json = self.json.leer_de_json()
        clientes_obj = []
        for cliente in clientes_json:
            cli = Cliente(cliente["rfc"], cliente["nombre"], cliente["telefono"])
            clientes_obj.append(cli)
        return clientes_obj


if __name__ == "__main__":
    clientes = Cliente().from_json()

    print(clientes[0])


