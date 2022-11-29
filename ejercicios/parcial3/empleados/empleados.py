class empresa:
    def __init__(self, nombre, ciudad, empleados):
        self.nombre = nombre
        self.ciudad= ciudad
        self.empleados = empleados

        import json
        ruta= "ejercicios/empleados.json"
        with open(ruta,"r") as file:
            data=json.load(file)

