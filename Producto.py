from Lista import Lista


class Productos(Lista):
    def __init__(self, codigo="", nombre="", descripcion="", precio="", stat=""):
        super().__init__("Productos.json")
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stat=stat

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.descripcion},{self.precio},{self.stat}"

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
            diccionario = {"codigo": self.codigo, "nombre": self.nombre, "descripcion": self.descripcion, "precio": self.precio,"stat":self.stat}
            listaDicc.append(diccionario)
            return diccionario



    def from_json(self):
        productos_json = self.json.leer_de_json()
        productos_obj = []
        for prod in productos_json:
            cli = Productos(prod["codigo"], prod["nombre"], prod["descripcion"], prod["precio"],prod["stat"])
            productos_obj.append(cli)
        return productos_obj


if __name__ == "__main__":
    prduc = Productos().from_json()
    print(prduc[1])
    for cliente in prduc:
        print(cliente.nombre)
