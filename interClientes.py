from Cliente import Cliente
from interBD import interBD


class interClientes:
    def __init__(self):
        self.cli = Cliente()

    def agregarCliente(self):
        rfc = input("Ingrese el RFC del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        cliente = Cliente(rfc, nombre, telefono)
        self.cli.agregar(cliente.to_dict())
        print("Cliente creado exitosamente!")

    def actulizarClientes(self):
        print("Que cliente quiere modificar?")
        id, info = self.seleccionar_cliente()
        print(f"Cliente a modificar: #{id + 1}")
        print(f"RFC: {info.rfc}")
        print(f"Nombre: {info.nombre}")
        print(f"Telefono: {info.telefono}")
        rfc = input("Ingrese el RFC del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        cliente = Cliente(rfc, nombre, telefono)
        self.cli.actualizar(id, cliente.to_dict())
        print("Cliente modificado correctamente ")

    def borrarClientes(self):
        print("Que cliente quiere eliminar?")
        id, info = self.seleccionar_cliente()
        print(f"Cliente a eliminar: #{id + 1}")
        print(f"RFC: {info.rfc}")
        print(f"Nombre: {info.nombre}")
        print(f"Telefono: {info.telefono}")
        confirm = input("Confirmacion y/n: ")
        if confirm == "y" | confirm=="Y":
            self.cli.eliminar(id)
            print("Cliente eliminado")
        else:
            return self.mainClientes()

    def verClientes(self):
        clientes_data = self.cli.from_json()
        print("{:<1} {:<20} {:<20} {:<20}".format("#", "RFC", "Nombre", "Telefono"))
        i = 0
        for cliente in clientes_data:
            i=i+1
            print("{:<1} {:<20} {:<20} {:<20}".format(i,cliente.rfc, cliente.nombre, cliente.telefono))
        return len(clientes_data), clientes_data

    def seleccionar_cliente(self):
        tam, clientes_data = self.verClientes()
        seleccion = input("Seleccione un cliente ingresando el número correspondiente: ")
        try:
            seleccion = int(seleccion)
            if seleccion > 0 and seleccion <= tam:
                seleccion = seleccion - 1
                return seleccion, clientes_data[seleccion]
            else:
                print("Opción inválida, intente de nuevo.")
                return interClientes.seleccionar_cliente()
        except ValueError:
            print("Opción inválida, intente de nuevo.")
            return interClientes.seleccionar_cliente()

    def menuClientes(self):
        print("------------------------------------")
        if interBD().checkarConexionEnUso():
            obj, bandera, bool = interBD().checkarConexionEnUso()
            print(f"Datos de conexion: {obj.user}-{obj.cluster}-{obj.bd}------")
            print(f"Estado: {bandera}")
        else:
            print("No hay conexion activa")
        print("------------------------------------")
        print("1. Crear un cliente")
        print("2. Modificar un cliente")
        print("3. Eliminar un cliente")
        print("4. Ver clientes")
        print("5. Regresar")
        print("------------------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion

    def mainClientes(self):
        opcion = ""
        while opcion != "5":
            opcion = self.menuClientes()
            if opcion == "1":
                self.agregarCliente()
                input("Presione Enter para continuar...")
            elif opcion == "2":
                self.actulizarClientes()
                input("Presione Enter para continuar...")
            elif opcion == "3":
                self.borrarClientes()
                input("Presione Enter para continuar...")
            elif opcion == "4":
                self.verClientes()
                input("Presione Enter para continuar...")
            elif opcion == "5":
                print("Saliendo del sistema...")
                return 1
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")


if __name__ == "__main__":
   interClientes().mainClientes()

    # cliente = Cliente(123456789, "Juan Pérez", 555555555)
    # clienteDic = cliente.to_dict()
    # clientes.agregar(clienteDic)
    # print(clientes.buscar(0))
    # print(clientes.mostrar())
    # clientes.actualizar(0, {"rfc": 123456789, "nombre": "Juan Hernandez", "telefono": 2131212})
    # print(clientes.mostrar())
    # clientes.eliminar(0)
    # print(clientes.mostrar())
