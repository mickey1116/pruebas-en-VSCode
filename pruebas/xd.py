import tkinter
import pruebas

def abrirventana3():
    actualizaciones=tkinter.Toplevel()
    actualizaciones.geometry("500x300")
    actualizardatos1=tkinter.Button(actualizaciones,text="actualizar nombre", command= abrirventanaNombre)
    actualizardatos1.pack()
    actualizardatos2=tkinter.Button(actualizaciones,text="actualizar edad", command= abrirventanaEdad)
    actualizardatos2.pack()
    actualizardatos3=tkinter.Button(actualizaciones,text="actualizar clave", command= abrirventanaCodigo)
    actualizardatos3.pack()
    actualizardatos4=tkinter.Button(actualizaciones,text="actualizar documento", command= abrirventanaDocumento)
    actualizardatos4.pack()


def abrirventanaNombre():
    documento=int(float(doc.get()))
    clave=int(float(passw.get()))
    usuario=pruebas.cajero(documento,clave)
    actualizacion=tkinter.Toplevel()
    actualizacion.geometry("300x100")
    Enombre=tkinter.Label(actualizacion,text="nombre")
    Enombre.pack()
    nombre=tkinter.Entry(actualizacion)
    nombre.pack()
    guardar=tkinter.Button(actualizacion,text="guardar cambio",command=lambda: usuario.actualizarDatos())
    guardar.pack()
def abrirventanaEdad():
    actualizacion=tkinter.Toplevel()
    actualizacion.geometry("300x100")
    Eedad=tkinter.Label(actualizacion,text="edad")
    Eedad.pack()
    edad=tkinter.Entry(actualizacion)
    edad.pack()
def abrirventanaCodigo():
    actualizacion=tkinter.Toplevel()
    actualizacion.geometry("300x100")
    Ecodigo=tkinter.Label(actualizacion,text="codigo")
    Ecodigo.pack()
    codigo=tkinter.Entry(actualizacion)
    codigo.pack()
def abrirventanaDocumento():
    actualizacion=tkinter.Toplevel()
    actualizacion.geometry("300x100")
    Edocumento=tkinter.Label(actualizacion,text="documento")
    Edocumento.pack()
    documento=tkinter.Entry(actualizacion)
    documento.pack()
