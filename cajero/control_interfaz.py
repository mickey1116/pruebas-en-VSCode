import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


class Usuario():
    def __init__(self, nombre, edad, documento, clave):
        self.nombre = nombre
        self.edad = edad
        self.documento = documento
        self.clave = clave

        import json
        ruta="cajero/datosUsuarios.json"
        with open(ruta,"r") as file:
            data=json.load(file)
        self.data=data

class cajero():
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("cajero UN")
        
        frame=LabelFrame(self.ventana, text="ingreso")
        frame.grid(row=0,column=1, columnspan=3, pady=20)

        Label(frame, text="documento: ").grid(row=1,column=0)
        self.usuario= Entry(frame)
        self.usuario.focus()
        self.usuario.grid(row=1, column=1)

        Label(frame, text="clave: ").grid(row=2,column=0)
        self.contraseña= Entry(frame)
        self.contraseña.grid(row=2, column=1)

        ttk.Button(frame,text="ingresar",command= self.ingresar).grid(row=3,column=2, sticky= W + E)

        frame1=LabelFrame(self.ventana, text="")
        frame1.grid(row=3,column=0, columnspan=3, pady=20)

        ttk.Button(frame1,text="crear usuario",command= self.datosNewUsuario).grid(row=4,column=2, sticky= W + E)



    
    def ingresar(self):

        import json
        ruta = "cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)
        self.datos=data


        self.documento=int(self.usuario.get())
        self.clave=int(self.contraseña.get())

        ingreso=False
        i=-1
        while ingreso==False:
            for usuario in self.datos:
                i=i+1
                if usuario["documento"]== self.documento:
                    print("vengaaaaa")
                    if usuario["clave"]==self.clave:
                        print("bienvenido")
                        self.abrirventana2()
                        ingreso=True
                        break
                    else: messagebox.showwarning("cuidado", "usuario o contraseña incorrectas")
                    break
            break


    def abrirventana2(self):
        ventana.withdraw()

        import json
        ruta="cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data=json.load(file)

        for usuario in data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                valor=usuario["salario"]
                nombre=usuario["nombre"]
                edad=usuario["edad"]
                documento=usuario["documento"]
                clave=usuario["clave"]
                break

        self.perfil=tkinter.Toplevel()
        self.perfil.title("perfil usuario")

        frame3=LabelFrame(self.perfil,text="datos")
        frame3.grid(row=0,column=1, columnspan=3, pady=20)

        Label(frame3, text="nombres: "+ usuario["nombre"]).grid(row=1,column=0)
        Label(frame3, text="edad: "+ str(usuario["edad"])).grid(row=2,column=0)
        Label(frame3, text="documento: "+ str(usuario["documento"])).grid(row=3,column=0)
        Label(frame3, text="clave: "+ str(usuario["clave"])).grid(row=4,column=0)
        ttk.Button(frame3,text="actualizar datos",command= self.actualizarDatos).grid(row=1,column=1)


        frame4=LabelFrame(self.perfil,text="")
        frame4.grid(row=5,column=1, columnspan=3, pady=20)

        Label(frame4, text="salario disponible: "+ str(usuario["salario"])).grid(row=6,column=0)

        ttk.Button(frame4,text="consignar",command= self.consignacion).grid(row=7,column=0)
        ttk.Button(frame4,text="retirar",command= self.retiro).grid(row=7,column=1)

        frame6=LabelFrame(self.perfil,text="")
        frame6.grid(row=8,column=1, columnspan=3,sticky=W+E, pady=20)
        
        ttk.Button(frame6,text="actualizar",command= self.actualizar).grid(row=8,column=2, sticky= W + E)
        ttk.Button(frame6,text="cerrar sesion",command= self.perfil.withdraw).grid(row=9,column=2, sticky= W + E)
        ttk.Button(frame6,text="borrar cuenta",command= self.borrarUsuario).grid(row=10,column=2, sticky= W + E)


        
    def consignacion(self):
        self.transferir=tkinter.Toplevel()
        self.transferir.title("transeferencia")

        frame5=LabelFrame(self.transferir, text="")
        frame5.grid(row=0,column=1, columnspan=3, pady=20)

        Label(frame5, text="valor a consignar: ").grid(row=1,column=0)
        self.salario= Entry(frame5)
        self.salario.focus()
        self.salario.grid(row=1, column=1)
        self.salario.get()
        ttk.Button(frame5,text="consignar",command= self.salarioupdating).grid(row=2,column=0)

    def retiro(self):
        self.transferir=tkinter.Toplevel()
        self.transferir.title("transeferencia")

        frame5=LabelFrame(self.transferir, text="")
        frame5.grid(row=0,column=1, columnspan=3, pady=20)

        Label(frame5, text="valor a retirar: ").grid(row=1,column=0)
        self.salario= Entry(frame5)
        self.salario.focus()
        self.salario.grid(row=1, column=1)
        self.salario.get()
        ttk.Button(frame5,text="retirar",command= self.retiroupdating).grid(row=2,column=0)

    def retiroupdating(self):
        import json
        ruta="cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data=json.load(file)

        for usuario in data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                valor=usuario["salario"]
                retiro=self.salario.get()
                del usuario["salario"]
                while int(valor)>=int(retiro):
                    usuario["salario"]=valor - int(retiro)
                    print("saldo actual: ", usuario["salario"])

                    import json
                    ruta="cajero/datosUsuarios.json"
                    with open(ruta,"w") as file:
                        json.dump(data,file)

                    
                    self.transferir.withdraw()

                    break
                else: messagebox.showwarning("cuidado", "saldo insuficiente")
        


    def salarioupdating(self):
        import json
        ruta = "cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)

        for usuario in data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                valor=usuario["salario"]
                consignacion=self.salario.get()
                del usuario["salario"]
                usuario["salario"]=valor + int(consignacion)
                print("saldo actual: ", usuario["salario"])

                import json
                ruta="cajero/datosUsuarios.json"
                with open(ruta,"w") as file:
                    json.dump(data,file)
                
                self.transferir.withdraw()
                break
 
    def actualizar(self):
        import json
        ruta = "cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)

        self.perfil.withdraw()
        self.abrirventana2()

    def actualizarDatos(self):
        import json
        ruta="cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data=json.load(file)

        for usuario in data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                valor=usuario["salario"]
                nombre=usuario["nombre"]
                edad=usuario["edad"]
                documento=usuario["documento"]
                clave=usuario["clave"]
                break

        self.actualizacion=tkinter.Toplevel()
        self.actualizacion.title("actualizacion de datos")

        frame7=LabelFrame(self.actualizacion, text="actualizaciones")
        frame7.grid(row=0,column=1, columnspan=3, pady=20)
        
        Label(frame7, text="nombres: "+ usuario["nombre"]).grid(row=1,column=0)
        Label(frame7, text="nombres actualizados: ").grid(row=1,column=1)
        self.nomb= Entry(frame7)
        self.nomb.focus()
        self.nomb.grid(row=1, column=2)
        Label(frame7, text="edad: "+ str(usuario["edad"])).grid(row=2,column=0)
        Label(frame7, text="edad actualizada: ").grid(row=2,column=1)
        self.ed= Entry(frame7)
        self.ed.grid(row=2, column=2)
        Label(frame7, text="documento: "+ str(usuario["documento"])).grid(row=3,column=0)
        Label(frame7, text="documento actualizado: ").grid(row=3,column=1)
        self.doc= Entry(frame7)
        self.doc.grid(row=3, column=2)
        Label(frame7, text="clave: "+ str(usuario["clave"])).grid(row=4,column=0)
        Label(frame7, text="clave actualizada: ").grid(row=4,column=1)
        self.cla= Entry(frame7)
        self.cla.grid(row=4, column=2)

        frame8=LabelFrame(self.actualizacion,text="")
        frame8.grid(row=5,column=0, columnspan=3, pady=20)
        ttk.Button(frame8,text="actualizar datos",command= self.datosA).grid(row=6,column=0)



    def datosA(self):
        import json
        ruta = "cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)

        print("siuuuu")

        for usuario in data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                n=self.nomb.get()
                del usuario["nombre"]
                usuario["nombre"]= n
                e=self.ed.get()
                del usuario["edad"]
                usuario["edad"]=int(e)
                d=self.doc.get()
                del usuario["documento"]
                usuario["documento"]=int(d)
                c=self.cla.get()
                del usuario["clave"]
                usuario["clave"]=int(c)


                import json
                ruta="cajero/datosUsuarios.json"
                with open(ruta,"w") as file:
                    json.dump(data,file)
                
                self.actualizacion.withdraw()
                break
        
    def borrarUsuario(self):

        self.deleteUser=tkinter.Toplevel()
        self.deleteUser.title("borrar cuenta")

        frame9=LabelFrame(self.deleteUser,text="confirmacion")
        frame9.grid(row=0,column=0)

        Label(frame9,text="escriba su clave: ").grid(row=1,column=0)
        self.confi=Entry(frame9)
        self.confi.grid(row=1,column=2)
        ttk.Button(frame9,text="confirmar",command= self.confirmacion).grid(row=2,column=0)

        
    def confirmacion(self):
        print("a")
        import json
        ruta = "cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)
        i=0
        for usuario in data:
            if usuario["documento"]== self.documento:
                print("vengaaaaa")
                if usuario["clave"]==int(self.confi.get()):
                    print("bienvenido")
                    data.pop(i)
                    import json
                    ruta="cajero/datosUsuarios.json"
                    with open(ruta,"w") as file:
                        json.dump(data,file)
                    print("usuario eliminado")
                    self.deleteUser.withdraw()
                    self.perfil.withdraw()
                    break
                else: print("contraseña incorrecta")
            else: i=i+1
            print(i)
 

    def datosNewUsuario(self):
        import json
        ruta = "cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)
        self.datos=data

        self.cuenta=tkinter.Toplevel()
        self.cuenta.title("crear cuenta")

        frame2=LabelFrame(self.cuenta,text="datos")
        frame2.grid(row=0,column=1, columnspan=3, pady=20)

        
        Label(frame2, text="nombres: ").grid(row=1,column=0)
        self.nombre= Entry(frame2)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)

        Label(frame2, text="edad: ").grid(row=2,column=0)
        self.edad= Entry(frame2)
        self.edad.grid(row=2, column=1)

        Label(frame2, text="clave: ").grid(row=3,column=0)
        self.contraseña= Entry(frame2)
        self.contraseña.grid(row=3, column=1)

        Label(frame2, text="documento: ").grid(row=4,column=0)
        self.id= Entry(frame2)
        self.id.grid(row=4, column=1)

        ttk.Button(frame2,text="crear",command= self.dataupdating).grid(row=5,column=2, sticky= W + E)




    def dataupdating(self):
        
        import json
        ruta = "cajero/datosUsuarios.json"
        with open(ruta, "r") as file:
            data = json.load(file)
        
        
        self.salario=0
        user={"nombre":self.nombre.get(),"edad":int(self.edad.get()),"documento":int(self.id.get()),"clave":int(self.contraseña.get()), "salario":int(self.salario)}
        data.append(user)
        self.data=data
        
        
        import json
        ruta="cajero/datosUsuarios.json"
        with open(ruta,"w") as file:
            json.dump(data,file)


        self.cuenta.withdraw()


    







         


if __name__ == "__main__":
    ventana=tkinter.Tk()
    usuario=cajero(ventana)
    ventana.mainloop()
