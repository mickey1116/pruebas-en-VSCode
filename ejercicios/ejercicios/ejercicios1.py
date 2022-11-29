"""
En este archivo encontramos ejercicios para introducirnos en el lenguaje, 
ejercicios introductorios para uso de variables y ejercicios con operadores.
"""

#====================== EJERCICIOS INTRODUCTORIOS ====================
#==>  EJERCICIO 1 
""" Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
mostrando en pantalla en formato "horas:minutos"  """

#tiempo=input("ingrese su tiempo en segundos: ")
from xml.etree.ElementTree import PI


tiempo=5400
tiempo=int(tiempo)
minutos=tiempo/60
horas=minutos/60
minu=((horas-int(horas))*60)
print("su tiempo es: ", int(horas), ":", int(minu))
#==>  EJERCICIO 2 30
""" ¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm? """
v=5**3
print(v)
r=(((3*v)/(4*3.14))**(1/3))
print("el valor del radio debe ser: ", r)

#==>  EJERCICIO 3 
""" ¿Cuantas veces supera, el area de un cubo, al area de una esfera, si el lado del
cubo es 10 cm. Y el radio de la esfera 2 cm ? """
Acubo= 10**2
Aesfera= 4*3.1416*(2**2)
diferencia=Acubo/Aesfera
print("el area del cubo supera a la esfera en: ", diferencia)
#==>  EJERCICIO 4 
""" Realice un código, que permita la conversión de millas a km y km a millas """
millas=16467486
kil=millas*1.609
print(kil)
kilometros=1368468
mill=kilometros/1.609
print(mill)

#==>  EJERCICIO 5 
""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """
punto1=[5,4,5]
punto2=[0,10,9]
resultante=[]
tamañolista=len(punto1)
for indice in range(0, tamañolista):
    resultado=(punto1[indice]-punto2[indice])**2
    resultante.append(resultado)

suma=sum(resultante)
distancia=suma**(1/2)
print("la distantcia entre los dos puntos es: " , distancia)

#==>  EJERCICIO 6 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """
nota1=4
nota2=5
nota3=2
notaNecesaria= (3-(nota1*0.15)-(nota2*0.25)-(nota3*0.2))/0.4
print("la nota necesaria es: ", notaNecesaria)

#==>  EJERCICIO 7 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas,
 con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 2 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de las dos últimas notas para pasar la materia. """
notanecesaria=(3-(nota1*0.15)-(nota2*0.25))/0.6
print(notanecesaria)

#==>  EJERCICIO 8 
""" Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
prestará solo de ida.
Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        No        Si    No
CAMILA        Si        Si        No        No    No
JOSE          Si        No        Si        No    No
MARIA         Si        Si        Si        No    No      
¿Cuanto debe pagar cada estudiante? """

tlunes=15000/4
tmartes=15000/3
tmiercoles=15000/2
tjueves=15000
tviernes=10000/4

juan= tlunes + tmartes + tjueves + tviernes
camila= tlunes + tmartes + tviernes
jose= tlunes + tmiercoles + tviernes
maria= tlunes + tmartes + tmiercoles + tviernes

print("juan, camila, jose y maria deben pagar respectibamente: ", juan, camila, jose, maria)

#==>  EJERCICIO 9 
""" El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
    en donde el precio de cada seguro es de $120000. 
    Para los primeros 20 seguros, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.
    a) Si un empleado vende 435 seguros, ¿cual será su salario?
    b) Para un salario de $10'000.000. ¿Cuántos seguros debe vender?
    c) Si un empleado devenga $15'000.000. ¿Cuantos salarios vendió en promedio al dia? 
       Teniendo en cuenta que solo trabajaba de lunes a jueves """

salario1=(120000+(120000)*0.2)*20
salario2=(120000+ (120000)*0.3)*100
salario3=(120000+ (120000)*0.1)*315

salarioA= salario1 + salario2 + salario3
print("el salario del punto A es: ", salarioA)
salarioB= (10000000-((120000)*0.2)-((120000)*0.3)-((120000)*0.1))/120000
print("el empleado debe vender: ", salarioB)

salarioc= (15000000-((120000)*0.2)-((120000)*0.3)-((120000)*0.1))/120000
promedioaldia= salarioc/5
print("el promedio de ventas al dia es: " , promedioaldia)

#==>  EJERCICIO 10 
""" El salario de un empleado de una empresa se calcula, utilizando como base el 
salario minimo, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
           
            precio_unidad  comisión
* Zapatos:    $ 50 000        5%
* Tenis:      $ 70 000        4%  
* Camizas:    $ 40 000        6%
* Corbatas:   $ 25 000        7%
* Pantalon:   $ 35 000        5%
* Blusas:     $ 80 000        3%
* Vestidos:   $ 95 000        2%
* Medias:     $ 10 000        8%
a) Realice un algoritmo que calcule el salario del empleado teniendo en cuenta el numero de ventas realizadas 
b) Uno de los directivos, quiere que la comisión de cada uno de los productos no supere los $2000
   ¿Qué productos deben cambiar en su porcentaje de comision?
c) Otro directivo desea que la comisión de cada producto se fije en $1900, 
   ¿en cuanto se deben fijar las comisiones de los productos"""

data=[["zapatos", 50000,0.05],
     ["Tenis", 70000, 0.04],
    ["Camizas", 40000,  0.06],
    ["Corbatas", 25000, 0.07],
    ["Pantalon", 35000, 0.05],
    ["Blusas",  80000, 0.03],
    ["Vestidos", 95000, 0.02],
    ["Medias",  10000, 0.08]]
dicsalario={}
for salario in data:
    dicsalario[salario[0]]={"precio": salario[1], "comision": salario[2]}

print(dicsalario["zapatos"])
#==>  EJERCICIO 11 
""" Un auto acelera de manera uniforme 0.5 km/s², 
a) ¿cuantas horas deben pasar para alcanzar la velocidad de la luz?
b) ¿qué distancia se habrá recorrido? (suponga que es posible alcanzar la velocidad de la luz) """

#==>  EJERCICIO 12 
""" Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
alcanzar una altura dada. """

#==>  EJERCICIO 13 
""" Un proyectil es lanzado siguiendo una trayectoria parabólica, calcule el ángulo y la velocidad inicial
que debe tener para alcanzar una distancia horizontal y vertical dada. """

#==>  EJERCICIO 14 
""" Un atleta inicia su entrenamiento, desde el punto de partida de una pista, a una velocidad constante de 3m/s. 
Diez segundos después otro atleta empieza su recorrido a una velocidad constante de 5m/s. ¿Cuánto tiempo 
habrá pasado para que el segundo atleta alcance al primero? """

#==>  EJERCICIO 15 
""" Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """

#====================== EJERCICIOS OPERADORES ====================
#==> Ejercicio 1 
""" Realice las siguientes operaciones mentalmente. Intente determinar la respuesta, luego verifique en python
   1 + 3 - 5      "cristian" + "Unal"     [1,2,3] + [4,5,6]    True and False          5 > 3          1 in [1,2,3]
   13 / 2         "Unal" * 5              [1,2] * 4            1 and 2                 2 != 2            "A" in ("A", "B", "C")   
   19 // 6                                (1,2,3) + (4,5,6)    5 and True              3 == "3"          1 not in ["A", "B", "C"]    
   31 % 3                                 (1,2) * 4            False and 5             5 > True          "A" in {"A", "B", "C"} 
   2 ** 5                                                      [] and "resultado"      True < 0
   16 ** 0.5                                                   True and (2,3,4)        True != False
                                                               False or True           "abc" < "bcd"
                                                               0 or 5
                                                               True or 5
                                                               "resultado" or False
   """

#==> EJERCICIO 2 
""" ¿Qué operaciones puede realizar con los anteriores operadores?
¿Qué tipos de datos se pueden utilizar con cada uno de los operadores? """

#==> EJERCICIO 3 
""" De los operadores *, /, +. ¿Cual tiene mayor prioridad?
=> 3 / 2 * 5  compare con 3 * 2 / 5
=> 3 / 2 + 5  compare con 3 + 2 / 5
=> 3 * 2 + 5  compare con 3 + 2 * 5  """

#==> EJERCICIO 4 
""" De los operadores *, **. ¿Cual tiene mayor prioridad?
=> 3 * 2 ** 5  compare con 3 ** 2 * 5
=> 2 * 2 ** 3  compare con 2 ** 2 * 3
=> 2 ** 2 ** 3 ¿Qué sucede en este caso? """

#==> EJERCICIO 5 
""" De los operadores *, /, //, % ¿cual tiene mayor prioridad?:
=> 13 // 6 * 2 compare con 27 // 6 * 2
=> 13 / 6 // 2 compare con 13 // 6 / 2
=> 13 * 6 % 2 compare con 13 % 6 * 2 """

#==> EJERCICIO 6 
""" Realice las siguientes operaciones, y determine:
¿Cuál es el orden de prioridades de los operadores not, and, or?
=> not True and False
=> True and not False
=> True and False or False
=> True or False and False """

#==> EJERCICIO 7
""" Intente determinar mentalmente la salida de las siguientes operaciones
 1 and 2 and 3     1 or 2 or 3
 1 and 0 and 3     1 or 0 or 3
 0 and 2 and 3     0 or 1 or 2
 """