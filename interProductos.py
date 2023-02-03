from Producto import Productos as Producto
from interBD import interBD




class interProductos:
    def __init__(self):
        self.prod = Producto()

    def agregarProducto(self):
        print("------------------------------------")
        if interBD().checkarConexionEnUso():
            obj, bandera, bool = interBD().checkarConexionEnUso()
            print(f"Datos de conexion: {obj.user}-{obj.cluster}-{obj.bd}------")
            print(f"Estado: {bandera}")
        else:
            print("No hay conexion activa")
        print("------------------------------------")
        codigo = input("Ingese el codigo del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese una breve descripcion del producto: ")
        precio = int(input("Ingrese el precio unitario del producto: "))
        if interBD().checkarConexionEnUso():#si da
            stat=2
            producto = Producto(codigo, nombre, descripcion, precio, stat)
            self.prod.agregar(producto.to_dict())
            list, id = self.prod.filter("stat", 2)
            obj.conect()
            for item in list:
                producS = item
                print(f"Guardando en BD: {item['nombre']}")
                coleccion = "Productos"
                producS["stat"] = 1
                self.prod.actualizar(id, producS)
                obj.insert_one(coleccion, item)
        else:
            stat=2
            producto = Producto(codigo, nombre, descripcion, precio, stat)
            self.prod.agregar(producto.to_dict())


        print("Producto creado exitosamente!")

    def actulizarProductos(self):
        print("Que producto quiere modificar?")
        id, info = self.seleccionar_producto()
        print(f"Producto a modificar: #{id + 1}")
        print(f"Codigo: {info.codigo}")
        print(f"Nombre: {info.nombre}")
        print(f"Descripcion: {info.descripcion}")
        print(f"Precio: ${info.precio}")
        print("Ingrese los datos nuevos")
        codigo = input("Ingrese el codigo del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        precio = input("Ingrese el precio del producto: ")
        producto = Producto(codigo, nombre, descripcion, precio)
        self.prod.actualizar(id, producto.to_dict())
        print("Producto modificado correctamente ")

    def borrarProductos(self):
        print("Que producto quiere eliminar? ")
        id, info = self.seleccionar_producto()
        print(f"Producto a eliminar: #{id+1}")
        print(f"Codigo: {info.codigo}")
        print(f"Nombre: {info.nombre}")
        print(f"Descripcion: {info.descripcion}")
        print(f"Precio: ${info.precio}")
        confirm = input("Confirmacion y/n: ")
        if confirm == "y" | confirm=="Y":
            self.prod.eliminar(id)
            print("Cliente eliminado")
        else:
            return self.mainProducto()

    def verProducto(self): #lista de productos
        productos_data = self.prod.from_json()
        print("{:<1} {:<20} {:<20} {:<20} {:<20}".format("#", "Codigo", "Nombre", "Descripcion", "Precio"))
        i=0
        for producto in productos_data:
            i=i+1
            print("{:<1} {:<20} {:<20} {:<20} ${:<20}".format(i, producto.codigo,producto.nombre, producto.descripcion, producto.precio))
        return len(productos_data), productos_data

    def seleccionar_producto(self): #devuelve id y objeto
        tam, data=self.verProducto()
        seleccion = input("Seleccione un producto ingresando el número correspondiente: ")
        try:
            seleccion = int(seleccion)
            if seleccion > 0 and seleccion <= tam:
                seleccion = seleccion - 1
                return seleccion, data[seleccion]
            else:
                print("Opción inválida, intente de nuevo.")
                return interProductos.seleccionar_producto()
        except ValueError:
            print("Opción inválida, intente de nuevo.")
            return interProductos.seleccionar_producto()

    def seleccionar_productos_varios(self):#devuelve los objetos
        tam, productos_data=self.verProducto()
        seleccion = input("Seleccione uno o más productos ingresando los números correspondientes separados por coma: ")
        try:
            seleccion = seleccion.split(",")
            seleccion = [int(x) for x in seleccion]
            seleccion = [productos_data[x - 1] for x in seleccion if x > 0 and x <= tam]
            if len(seleccion) > 0:
                return seleccion
            else:
                print("Opción inválida, intente de nuevo.")
                return interProductos.seleccionar_productos()
        except ValueError:
            print("Opción inválida, intente de nuevo.")
            return interProductos.seleccionar_productos()

    def menuProducto(self):
        print("------------------------------------")
        if interBD().checkarConexionEnUso():
            obj, bandera, bool = interBD().checkarConexionEnUso()
            print(f"Datos de conexion: {obj.user}-{obj.cluster}-{obj.bd}------")
            print(f"Estado: {bandera}")
        else:
            print("No hay conexion activa")
        print("------------------------------------")
        print("1. Crear un producto")
        print("2. Modificar un producto")
        print("3. Eliminar un producto")
        print("4. Ver productos")
        print("5. Regresar")
        print("------------------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion

    def mainProducto(self):

        opcion = ""
        while opcion != "5":
            opcion = self.menuProducto()
            if opcion == "1":
                self.agregarProducto()
                input("Presione Enter para continuar...")
            elif opcion == "2":
                self.actulizarProductos()
                input("Presione Enter para continuar...")
            elif opcion == "3":
                self.borrarProductos()
                input("Presione Enter para continuar...")
            elif opcion == "4":
                self.verProducto()
                input("Presione Enter para continuar...")
            elif opcion == "5":
                print("Saliendo del sistema...")
                return 1
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")


if __name__ == "__main__":
    # print(interProductos().seleccionar_productos_varios())
    interProductos().mainProducto()
