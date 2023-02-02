from conecMongo import MongoConexion

class interBD:
    def __init__(self):
        self.bd = MongoConexion(None,None,None)

    def conectarABd(self):
        print("Inserte los datos de conexion")
        user = input("Usuario: ")
        contra = input("Contraseña: ")
        clus = input("Cluster: ")
        self.bd = MongoConexion(user,contra,clus)
        op= input("Desea nombrar la bd?(Nombre predeterminado: VentasRamirez): y/n   ")
        if op=="y":
            nomBd=input("Nombre de la bd:")
            self.bd.connect(nomBd)
        else:
            self.bd.connect("VentasRamirez")


    def menuBd(self):
        print("------------------------------------")
        print("1. Conectar a mongo bd")
        print("2. Sin conexion")
        print("3. Actualizar datos a bd")
        print("4. Ver datos de conexion")
        print("5. Regresar")
        print("------------------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion

    def mainBd(self):

        opcion = ""
        while opcion != "5":
            opcion = self.menuBd()
            if opcion == "1":
                self.conectarABd()
                input("Presione Enter para continuar...")
            elif opcion == "2":
                pass
                input("Presione Enter para continuar...")
            elif opcion == "3":
                pass
                input("Presione Enter para continuar...")
            elif opcion == "4":
                pass
                input("Presione Enter para continuar...")
            elif opcion == "5":
                print("Saliendo del sistema...")
                return 1
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")

if __name__ == "__main__":
    interBD().mainBd()