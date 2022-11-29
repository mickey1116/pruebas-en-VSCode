class Automoviles:
    def __init__(self, color, personasSentadas, uso):
        self.color = color
        self.personasSentadas = personasSentadas
        self.uso = uso

    def acelerar(self, a, t):
        v=a*t
        return v
    def frenar(self,v, a):
        t=-v/a
        return t



FERRARI_458= Automoviles("rojo", 2, "deportivo")
MCLAREN_720S= Automoviles("negro", 4,"deportivo")
AUTOLEGAL=Automoviles("blanco", 20, "publico")


atributoA= FERRARI_458.color
atributoB= MCLAREN_720S.uso
atributoC= AUTOLEGAL.personasSentadas
print(atributoA, atributoB,atributoC)

salida1=FERRARI_458.acelerar(4,5)
salida2=AUTOLEGAL.frenar(16,-8)
print("aceleracion es: , tiempo es: " ,salida1,salida2)