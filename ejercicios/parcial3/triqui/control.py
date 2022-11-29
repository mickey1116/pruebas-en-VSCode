import interfaz
import logica

interfaz.explicarJuego()
tableroJuego = logica.obtenerTableroLogico()
for turno in ["x", "x", "x","x","x"]:
    print("\nTurno jugador ", turno)
    posicion = int(input("   Ingrese posicion de juego: "))
    while tableroJuego[posicion] != None:
        posicion= int(input("seleccione una posicion vacia: "))
    else: tableroJuego[posicion] = turno
    tableroJuego = logica.actualizarTableroLogico(tableroJuego, posicion, turno)
    interfaz.dibujarTablero(tableroJuego)
    posibleGanador = logica.determinarGanador(tableroJuego)
    if posibleGanador in ["x", "o"]:
        print("Felicidades ha ganado el juego jugador ", turno)
        break
    posIA= logica.jugadaIA(posicion)
    while tableroJuego[posIA] != None:
        posIA= logica.jugadaIA(posIA)
    else: tableroJuego[posIA] = "o"
    tableroJuego= logica.actualizarTableroLogico(tableroJuego,posIA,"o")
    interfaz.dibujarTablero(tableroJuego)
