from Lista import Lista


class Venta(Lista):
    def __init__(self,cliente={},detalle_producto=[],fecha="",total=0):
        super().__init__("Ventas.json")
        self.cliente = cliente
        self.detalle_producto = detalle_producto
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"{self.cliente},{self.detalle_producto},{self.fecha},{self.total}"

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
            diccionario = {"cliente": self.cliente, "detalle_producto": self.detalle_producto, "fecha": self.fecha,
                           "total": self.total}

            listaDicc.append(diccionario)
            return diccionario

    def from_json(self):
        venta_json = self.json.leer_de_json()
        venta_obj = []
        for venta in venta_json:
            cli = Venta(venta["cliente"], venta["detalle_producto"], venta["fecha"], venta["total"])
            venta_obj.append(cli)
        return venta_obj





if __name__ == "__main__":
    cli = Venta().from_json()
    print(cli[0])

