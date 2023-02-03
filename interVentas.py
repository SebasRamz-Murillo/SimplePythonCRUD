from interClientes import interClientes
from interProductos import interProductos
from Venta import Venta
import os
import datetime
from Producto import Productos as Producto
from Cliente import Cliente
from interBD import interBD


class interVentas:
    def __init__(self):
        self.vent = Venta()
        self.fecha = datetime.datetime.now().strftime("%d-%m-%Y")#dia, mes, año

    def agregarVenta(self):
        print("Agregar venta            " + self.fecha)
        idCli, infoCli = interClientes().seleccionar_cliente()
        print(f"Cliente de venta: {infoCli.nombre}")
        prodList = interProductos().seleccionar_productos_varios()
        print("-----------------Informacion de venta-----------------")
        print(f"Cliente de venta: {infoCli.nombre}")
        print("Productos en venta:")
        total = 0
        i=0
        print("{:<2} {:<20} ${:<20}".format("#", "Nombre", "Precio"))
        for producto in prodList:
            i=i+1
            print("{:<2} {:<20} {:<20}".format(i, producto.nombre, producto.precio))
            total = total + float(producto.precio)
        print("Total de venta: $" + str(total))
        print("Aceptar:   1")
        print("Modificar: 2")
        print("Cancelar:  3")
        opcion = input("Opcion:")
        while opcion != "3":
            if opcion == "2":
                print("Modificar: ")
                print("Cliente:   1")
                print("Productos: 2")
                opcion2 = input("Opcion:")
                if (opcion2 == "2"):  # modificar Productos
                    total = 0
                    prodList = interProductos().seleccionar_productos_varios()

                else:
                    idCli, infoCli = interClientes().seleccionar_cliente()
                print("-----------------Informacion de venta-----------------")
                print(f"Cliente de venta: {infoCli.nombre}")
                print("Productos en venta:")
                total = 0
                i = 0
                print("{:<2} {:<20} {:<20}".format("#", "Nombre", "Precio"))
                for producto in prodList:
                    i = i + 1
                    print("{:<2} {:<20} ${:<20}".format(i, producto.nombre, producto.precio))
                    total = total + float(producto.precio)
                print("Total de venta: $" + str(total))
                print("Aceptar: 1")
                print("Modificar: 2")
                opcion = input("Opcion:")
            else:
                productoFinal=[]
                for prod in prodList:
                    productoFinal.append(prod.to_dict())
                ventaFinal = Venta(infoCli.to_dict(), productoFinal, self.fecha, total, stat)
                self.vent.agregar(ventaFinal.to_dict())
                print("Venta creado exitosamente!")
                break

    def modificarVenta(self):
        print("Que venta quiere eliminar?")
        info, dir = self.seleccionarVenta()
        cliente = info.cliente
        productos = info.detalle_producto
        productos_str = ', '.join([product['nombre'] for product in productos])
        print("Venta a eliminar: ")
        print(f"Fecha: {info.fecha}")
        print(f"Cliente: {cliente.get('nombre')} RFC:{cliente.get('rfc')}")
        print(f"Productos: {productos_str}")
        print(f"Total: ${info.total}")
        print("-----------------ActualizarVenta-----------------")
        fechaNueva= "-".join(input("Inserte fecha modificada en formato d/m/a").split("/"))
        idCli, infoCli = interClientes().seleccionar_cliente()
        print(f"Cliente de venta: {infoCli.nombre}")
        prodList = interProductos().seleccionar_productos_varios()
        print("-----------------Informacion de venta-----------------")
        print(f"Cliente de venta: {infoCli.nombre}")
        print("Productos en venta:")
        total = 0
        i = 0
        print("{:<2} {:<20} {:<20}".format("#", "Nombre", "Precio"))
        for producto in prodList:
            i = i + 1
            print("{:<2} {:<20} ${:<20}".format(i, producto.nombre, producto.precio))
            total = total + float(producto.precio)
        print("Total de venta: $" + str(total))
        print("Aceptar:   1")
        print("Cancelar:   2")
        confirm = input("Confirmacion:  ")
        if confirm == "1":
            productoFinalActualizado = []
            for prod in prodList:
                productoFinalActualizado.append(prod.to_dict())
            ventaFinal = Venta(infoCli.to_dict(), productoFinalActualizado, fechaNueva, total)
            self.vent.actualizar(dir,ventaFinal.to_dict())
            print("Venta actualizada")
        else:
            return self.mainVentas()

    def borrarVenta(self):
        print("Que venta quiere eliminar?")
        info, dir = self.seleccionarVenta()
        cliente = info.cliente
        productos = info.detalle_producto
        productos_str = ', '.join([product['nombre'] for product in productos])
        print("Venta a eliminar: ")
        print(f"Fecha: {info.fecha}")
        print(f"Cliente: {cliente.get('nombre')} RFC:{cliente.get('rfc')}")
        print(f"Productos: {productos_str}")
        print(f"Total: ${info.total}")
        confirm = input("Confirmacion y/n: ")
        if confirm == "y" | confirm=="Y":
            print(dir)
            print(info)
            self.vent.eliminar(dir)
            print("Venta eliminada")
        else:
            return self.mainVentas()

    def seleccionarVenta(self):#data, direccion
        ubi,ventas_data = self.verVentas()
        seleccion = input("Seleccione una venta ingresando el número correspondiente: ")
        try:
            seleccion = int(seleccion)
            if seleccion > 0 and seleccion <= ubi:
                seleccion = seleccion - 1
                return ventas_data[seleccion], seleccion
            else:
                print("Opción inválida, intente de nuevo.")
                return interProductos.seleccionar_cliente()
        except ValueError:
            print("Opción inválida, intente de nuevo.")
            return interProductos.seleccionar_cliente()
        input("Presione Enter para continuar...")

    def verVentas(self):
        ventas_data = self.vent.from_json()
        print("{:<1} {:<10} {:<20} {:<30} {:<20} {:<20}".format("#", "RFC","Cliente", "Productos", "Fecha", "Total"))
        i=0
        for venta in ventas_data:
            i=i+1
            clienteInfo= venta.cliente
            prodListInfo=venta.detalle_producto
            productos_str = ', '.join([product['nombre'] for product in prodListInfo])
            print("{:<1} {:<10} {:<20} {:<30} {:<20} ${:<20}".format(i,clienteInfo.get("rfc"), clienteInfo.get("nombre"), productos_str, venta.fecha, venta.total))
        return len(ventas_data), ventas_data

    def menuVentas(self):
        print("------------------------------------")
        if interBD().checkarConexionEnUso():
            obj, bandera, bool = interBD().checkarConexionEnUso()
            print(f"Datos de conexion: {obj.user}-{obj.cluster}-{obj.bd}------")
            print(f"Estado: {bandera}")
        else:
            print("No hay conexion activa")
        print("------------------------------------")
        print("1. Crear una venta")
        print("2. Modificar una venta")
        print("3. Eliminar una venta")
        print("4. Ver ventas")
        print("5. Regresar")
        print("------------------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion

    def mainVentas(self):
        opcion = ""
        while opcion != "5":
            opcion = self.menuVentas()
            if opcion == "1":
                self.agregarVenta()
                input("Presione Enter para continuar...")

            elif opcion == "2":
                self.modificarVenta()
                input("Presione Enter para continuar...")

            elif opcion == "3":
                self.borrarVenta()
                input("Presione Enter para continuar...")

            elif opcion == "4":
                self.verVentas()
                input("Presione Enter para continuar...")

            elif opcion == "5":
                print("Saliendo del sistema...")
                return 1
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")


if __name__ == "__main__":
    interVentas().mainVentas()
