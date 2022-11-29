import interfazsudoku
import logicasudoku

interfazsudoku.explicarJuego()
tableroJuego = logicasudoku.obtenerTableroLogico()
for turno in ["x", "x", "x","x","x","x", "x", "x","x","x", "x", "x", "x","x","x"]:
    print("\nTurno jugador ", turno)
    posicion = int(input("   Ingrese posicion de juego: "))
    while tableroJuego[posicion] != None:
        posicion= int(input("seleccione una posicion vacia: "))
    else: tableroJuego[posicion] = turno
    tableroJuego = logicasudoku.actualizarTableroLogico(tableroJuego, posicion, turno)
    interfazsudoku.dibujarTablero(tableroJuego)
    posibleGanador = logicasudoku.determinarGanador(tableroJuego)
    if posibleGanador in ["x", "o"]:
        print("Felicidades ha ganado el juego jugador ", turno)
        break
