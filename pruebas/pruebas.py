
class Usuario():
    def __init__(self, nombre, edad, documento, clave):
        self.nombre = nombre
        self.edad = edad
        self.documento = documento
        self.clave = clave

        import json
        ruta="pruebas/datosUsuarios.json"
        with open(ruta,"r") as file:
            data=json.load(file)
        self.data=data

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
        for usuario in self.data:
            if usuario["documento"]==self.documento:
                print("entramos")
                consignacion=input("valor a consignar:")
                salario=usuario["salario"]
                salario=salario+int(consignacion)
            else: salario ="no se pudo consignar"
            print("usuario incorrecto")
        return salario




class cajero():
    def __init__(self,documento, clave):
        self.documento = documento
        self.clave = clave

         
        import json
        ruta = "pruebas/datosUsuarios.json"
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

        import json
        ruta = "pruebas/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)
        self.data=data

        ingreso=False
        while ingreso==False:
            for usuario in self.data:
                if usuario["documento"]== self.documento:
                    print("vengaaaaa")
                    if usuario["clave"]==self.clave:
                        print("bienvenido")
                        ingreso=True
                        break
                    else: print("contraseña incorrecta")
                    break
                else:ingreso=False
            if ingreso==False:
                print("usuario invalido")
            break
        return ingreso

    def borrarUsuario(self):
        x=input("digite 1 si quiere borrar su cuenta, 0 sino quiere borrarla ")
        if x=="1":
            contraseña=input("ingrese su clave: ")
            if int(contraseña)==self.clave:
                despedida="usuario a sido eliminado"

                import json
                ruta = "pruebas/datosUsuarios.json"
                with open(ruta, "r") as file:
                    data = json.load(file)
                self.data=data
                i=0
                for usuario in self.data:
                    if usuario["documento"]== self.documento:
                        print("vengaaaaa")
                        if usuario["clave"]==self.clave:
                            print("bienvenido")
                            self.data.pop(i)
                            import json
                            ruta="pruebas/datosUsuarios.json"
                            with open(ruta,"w") as file:
                                json.dump(self.data,file)

                            print(despedida)
                        else: print("contraseña incorrecta")
                        break
                    else: i=i+1
                    print(i)
                    print("usuario incorrecto")
            else: print("no se borro la cuenta")
            despedida=False
        else: print("accion abortada")
        despedida=False
        return despedida

    def actualizarDatos(self):

        import json
        ruta = "pruebas/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)
            self.data=data
        for usuario in self.data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                if usuario["clave"]==self.clave:
                    datoActualizar=input("ingrese el dato que quiere actualizar: ")
                    del usuario[datoActualizar]
                    if datoActualizar == "nombre":
                        datoActualizado=input("ingrese el dato actualizado: ")
                        usuario[datoActualizar]=datoActualizado
                    elif datoActualizar !="nombre":
                        datoActualizado=input("ingrese el dato actualizado: ")
                        usuario[datoActualizar]=int(datoActualizado)

                    import json
                    ruta="pruebas/datosUsuarios.json"
                    with open(ruta,"w") as file:
                        json.dump(self.data,file)

                    actualizacion="actualizacion exitosa"

                    break

                else: print("contraseña incorrecta")
                actualizacion=False
                break
            else: print("usuario incorrecto")
            actualizacion=False
            break
        return actualizacion

    def consignacion(self):

        import json
        ruta="pruebas/datosUsuarios.json"
        with open(ruta, "r") as file:
            data=json.load(file)
        self.data=data

        for usuario in self.data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                valor=usuario["salario"]
                consignacion=input("ingrese valor a consignar: ")
                del usuario["salario"]
                usuario["salario"]=valor + int(consignacion)
                print("saldo actual: ", usuario["salario"])
                consi="consignacion exitosa"

                import json
                ruta="pruebas/datosUsuarios.json"
                with open(ruta,"w") as file:
                    json.dump(self.data,file)
                
                break

            else: print("usuario incorrecto")
            consi="algo salio mal"
        return consi

    def retiro(self):

        import json
        ruta="pruebas/datosUsuarios.json"
        with open(ruta, "r") as file:
            data=json.load(file)
        self.data=data

        for usuario in self.data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                valor=usuario["salario"]
                retiro=input("ingrese valor a retirar: ")
                del usuario["salario"]
                usuario["salario"]=valor - int(retiro)
                print("saldo actual: ", usuario["salario"])
                ret="retiro exitoso"


                import json
                ruta="pruebas/datosUsuarios.json"
                with open(ruta,"w") as file:
                    json.dump(self.data,file)
                
                break

            else: print("usuario incorrecto")
            ret="algo salio mal"
        return ret




def crearUsuario():

    import json
    ruta = "pruebas/datosUsuarios.json"
    with open(ruta, "r") as file:
        data = json.load(file)


    nombre=input("ingrese su nombre completo: ")
    edad=input("ingrese su edad: ")
    documento=input("ingrese su documento: ")
    clave1=input("ingrese su clave: ")
    clave2=input("por favor confirme su clave:")
    salario=0
    while clave1!=clave2:
        clave1=input("contraseña incorrecta, vuelva a intentarlo")
        clave2=input("confirme la clave:")
    else: clave=clave1
    user={"nombre":nombre,"edad":int(edad),"documento":int(documento),"clave":int(clave), "salario":int(salario)}
    data.append(user)


    import json
    ruta="pruebas/datosUsuarios.json"
    with open(ruta,"w") as file:
        json.dump(data,file)

    bienvenida="su usuario a sido creado con exito"

    return bienvenida


    









if __name__ == "__main__":
    curso1 = cajero(10026,114)
    print("ingreso=>", curso1.ingresar())
