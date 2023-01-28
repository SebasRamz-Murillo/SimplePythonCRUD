from interProductos import interProductos
from interClientes import interClientes
from interVentas import interVentas
from JSON_Handle import JSON_Handle

import os
import datetime


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menuGeneral():
    clear()
    print("Sistema de gestión de clientes, productos y ventas          "+datetime.datetime.now().strftime("%d-%m-%Y"))
    print("1. Clientes")
    print("2. Productos")
    print("3. Ventas")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def main():
    opcion = ""

    while opcion != "0":
        opcion = menuGeneral()
        if opcion == "1":
            interClientes().mainClientes()

        elif opcion == "2":
            interProductos().mainProducto()

        elif opcion == "3":
            interVentas().mainVentas()
        elif opcion == "p":
            contra=input("Contra:")
            if contra=="1234":
                JSON_Handle.clear_all_files()
            else:
                return main()
        elif opcion == "0":
            # Salir
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
            input("Presione Enter para continuar...")





if __name__ == "__main__":
    main()
