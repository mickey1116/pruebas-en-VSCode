


class usuario():
    def __init__(self, nombre, edad, codigo, clave):
        self.nombre = nombre
        self.edad = edad
        self.codigo = codigo
        self.clave = clave
        

class cajero():
    def __init__(self, nombre,edad,codigo, clave):
        self.nombre=nombre
        self.edad = edad
        self.codigo = codigo
        self.clave=clave

        import json
        nombreArchivo="usuario.json"
        ruta="proyecto/" + nombreArchivo
        opcion="r"

        with open(ruta, opcion) as file:
            data=json.load(file)
        
        listaUsuarios = []
        for diccionarioUsuarios in data:
            nombre = diccionarioUsuarios["nombre"]
            edad =   diccionarioUsuarios["edad"]
            codigo = diccionarioUsuarios["codigo"]
            clave =  diccionarioUsuarios["clave"]
            objetoUsuario = usuario(nombre,edad,codigo,clave)
            listaUsuarios.append(objetoUsuario)

        self.usuarios = listaUsuarios

    def crearUsuario(self):
        
        infoUsuario={"nombre":self.nombre,"edad":self.edad, "codigo":self.codigo,"clave": self.clave}
        usuario={self.documento:infoUsuario}
        data=self.usuarios.append(usuario)

        import json
        nombreArchivo="usuario.json"
        ruta="proyecto/" + nombreArchivo
        opcion="w"

        with open(ruta, opcion) as file:
            json.dump(data, file)

    def actualizarDatos(self):
        infoUsuario=usuario(self.nombre,self.edad,self.codigo,self.clave)
        datoActulizar=input("dato a actualizar: ")
        del infoUsuario[datoActulizar]
        datoActualizado=input("ingrese el dato actulizado: ")
        infoUsuario[datoActulizar]=datoActualizado
        self.usuarios.append(infoUsuario)
        print(self.usuarios)
        data=self.usuarios

        import json
        nombreArchivo="usuarios.json"
        ruta="proyecto/" + nombreArchivo
        opcion="w"

        with open(ruta, opcion) as file:
            json.dump(data, file)

if __name__ == "__main__":
    curso1 = cajero("Camilo Diaz",20, "001",123)

    print("media del curso=>", curso1.actualizarDatos())