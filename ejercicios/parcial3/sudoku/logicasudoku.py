def obtenerTableroLogico():
    tableroLogico = [None, None, None, None, None, None, None, None, None,None, None, None, None, None,None]
    return tableroLogico

def actualizarTableroLogico(tableroLogico, posicion, numero):
    tableroLogico[posicion] = numero
    return tableroLogico

def determinarGanador(tableroLogico):
    posicionesParaGanar = [(0, 1, 4,5),
                           (2, 3, 6, 7),
                           (8,9,12,13),
                           (10,11,14,15),
                           (0,4,8,12),
                           (1,5,9,13),
                           (2,6,10,14),
                           (3,7,11,15),
                           (0,1,2,3),
                           (4,5,6,7)
                           (8,9,10,11),
                           (12,13,14,15)]
    ganador = None
    for p1, p2, p3,p4 in posicionesParaGanar:
        if (tableroLogico[p1] != tableroLogico[p2] != tableroLogico[p3]!=tableroLogico[p4]):
            if tableroLogico[p1] != None:
                ganador = tableroLogico[p1]
    return ganador



if __name__ == "__main__":
    tablero = obtenerTableroLogico()
    tableroNuevo = actualizarTableroLogico(tablero, 0, "x")
    print(tableroNuevo)
    ganador =  determinarGanador(["x", "x", "x", None, None,None,None,None,None,None, None,None,None,None,None ])
    print(ganador)