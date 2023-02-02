from Mongo import Mongo
class interBD:
    def __init__(self):
        self.mong=Mongo()
    def conectarABd(self):
        print("------Conexion a MongoDB------")
        print("1. Ingresar por url")
        print("2. Ingresar por datos")
        opci=input("Seleccione una opcion: ")
        if opci =="2":
            print("Inserte los datos de conexion")
            user = input("Usuario: ")
            contra = input("Contraseña: ")
            clus = input("Cluster: ")
            token = input("Toke: ")
            op = input("Desea nombrar la bd?(Nombre predeterminado: VentasRamirez): y/n   ")
            if op == "y":
                nomBd = input("Nombre de la bd:")
                bd = nomBd
            else:
                bd = "VentasRamirez"
            mongoBD = Mongo(user=user, contra=contra, cluster=clus, token=token, bd=bd)
        elif opci=="1":
            print("Inserte la url de conexion")
            url = input("Url: ")
            op = input("Desea nombrar la bd?(Nombre predeterminado: VentasRamirez): y/n   ")
            if op == "y":
                nomBd = input("Nombre de la bd:")
                bd = nomBd
            else:
                bd = "VentasRamirez"
            mongoBD = Mongo(url=url,
                           bd=bd)
        self.mong.agregar(mongoBD.to_dict())


    def mostrarConexiones(self):
        conexiones_data = self.mong.from_json()
        print("{:<1} {:<20} {:<20} {:<20} {:<20}".format("#", "User", "Cluster", "BD", "Status"))
        i = 0
        for conexion in conexiones_data:
            i = i + 1
            print("{:<1} {:<20} {:<20} {:<20} {:<20}".format(i, conexion.user, conexion.cluster, conexion.bd,conexion.getStatus()))
        return len(conexiones_data), conexiones_data


    def menuBd(self):
        print("------------------------------------")
        print("1. Conectar a mongo bd")
        print("2. Sin conexion")
        print("3. Actualizar datos a bd")
        print("4. Ver datos de conexion")
        print("5. Regresar")
        print("------------------------------------")
        opcion = input("Selection una opción: ")
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
                input("Presione Enter para continuar...")
            elif opcion == "4":
                self.mostrarConexiones()
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

    #mongodb+srv://admin:root@cluster0.hcy4jnm.mongodb.net/?retryWrites=true&w=majority
    #mongodb+srv://pablo:1010@cluster0.qfgfj6v.mongodb.net/?retryWrites=true&w=majority

    #mongodb+srv://pablaao:1010@cluster0.qfgfj6v.mongodb.net/?retryWrites=true&w=majority