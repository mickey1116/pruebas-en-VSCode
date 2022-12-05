import tkinter
import pruebas
from tkinter import messagebox

def DOCU():
    documento=int(float(doc.get()))
    clave=int(float(passw.get()))
    usuario=pruebas.cajero(documento,clave)
    usuario.ingresar()
    if usuario.ingresar()==True:
        etiqueta=tkinter.Label(ventana, text="Bienvenido")
        etiqueta.grid(row=0,column=5)
        abrirventana2()
    else:messagebox.showwarning("cuidado", "usuario invalido")

def actualizar():
    documento=int(float(doc.get()))
    clave=int(float(passw.get()))
    usuario=pruebas.cajero(documento,clave)
    usuario.actualizarDatos()

def abrirventana2():
    documento=int(float(doc.get()))
    clave=int(float(passw.get()))
    usuario=pruebas.cajero(documento,clave)

    ventana.withdraw()
    cuenta=tkinter.Toplevel()
    cuenta.geometry("300x300")
    bienvenida=tkinter.Label(cuenta,text="bienvenido")
    bienvenida.grid(row=0,column=4)
    actualizardatos=tkinter.Button(cuenta,text="actualizar datos", command= lambda: usuario.actualizarDatos())
    actualizardatos.grid(row=7,column=0)
    
    borrarcuenta=tkinter.Button(cuenta, text="borrar cuenta", command= lambda: usuario.borrarUsuario())
    borrarcuenta.grid(row=8,column=0)

    consignar=tkinter.Button(cuenta, text="consignar", command= lambda: usuario.consignacion())
    consignar.grid(row=7,column=5)
    retirar=tkinter.Button(cuenta, text="retirar", command= lambda: usuario.retiro())
    retirar.grid(row=8,column=5)

    cerrarsecion=tkinter.Button(cuenta, text="cerrar secion", command= cuenta.destroy)
    cerrarsecion.grid(row=10, column=4)
    

ventana=tkinter.Tk()
ventana.geometry("300x100")


etiqueta1=tkinter.Label(ventana, text="documento")
etiqueta1.grid(row=0, column=1)
doc=tkinter.Entry(ventana)
doc.grid(row=0,column=2)
etiqueta2=tkinter.Label(ventana, text="clave")
etiqueta2.grid(row=1,column=1)
passw=tkinter.Entry(ventana)
passw.grid(row=1,column=2)


boton=tkinter.Button(ventana, text="ingresar",command= lambda: DOCU())
boton.grid(row=1,column=5)

crear=tkinter.Button(ventana,text="crear cuenta", command=lambda: pruebas.crearUsuario())
crear.grid(row=5, column=2)

ventana.mainloop()