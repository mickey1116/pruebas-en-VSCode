salario=0
class Usuario():
    def __init__(self, nombre, edad, documento, clave):
        self.nombre = nombre
        self.edad = edad
        self.documento = documento
        self.clave = clave

    def retirar(self):
        contraseña=input("ingrese su clave: ")
        while contraseña!= self.clave:
            contraseña=input("clave incorrecta, vuelva a intentar:")
        else:print("salario disponible: ", salario)
        retiro=input("valor a retirar: ")
        while retiro>salario:
            retiro=input("saldo insuficiente pruebe otro valor: ")
        else: salario=salario-retiro
        return salario

    def consignar(self):
        consignacion=input("valro a consignar:")
        salario=salario+consignacion
        return salario

    def info(self):
        documento=self.documento
        clave=self.clave
        lista=[documento,clave]
        return lista




class cajero():
    def __init__(self,documento, clave):
        self.documento = documento
        self.clave = clave

         
        import json
        ruta = "cajero/dataUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)
        print("lectura de datos=>", data)
        self.data=data

        listaUsuarios = []
        for diccionarioUsuarios in data:
            nombre = diccionarioUsuarios["nombre"]
            edad = diccionarioUsuarios["edad"]
            documento = diccionarioUsuarios["documento"]
            clave = diccionarioUsuarios["clave"]
            objetoEstudiante = Usuario(nombre,edad,documento,clave)
            listaUsuarios.append(objetoEstudiante)

        self.usuarios = listaUsuarios

    def ingresar(self):
        for usuario in self.data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                if usuario["clave"]==self.clave:
                    print("bienvenido")
                    ingreso=True
                else: print("contraseña incorrecta")

            else: print("usuario incorrecto")
        return ingreso

    def crearUsuario(self):
        nombre=input("ingrese su nombre completo: ")
        edad=input("ingrese su edad: ")
        documento=input("ingrese su documento: ")
        clave1=input("ingrese su clave: ")
        clave2=input("por favor confirme su clave:")
        while clave1!=clave2:
            clave1=input("contraseña incorrecta, vuelva a intentarlo: ")
            clave2=input("confirme la clave:")
        else: clave=clave1
        objetoUsuario=Usuario(nombre,edad,documento,clave)






if __name__ == "__main__":
    curso1 = cajero(142,123)

    print("ingreso=>", curso1.ingresar())