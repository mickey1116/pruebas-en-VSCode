"""
Este modulo contiene 3 funciones para imprimir en el juego triqui
"""

def explicarJuego():
    explicacion = """
    ====================================================
    Este es el juego triqui
    
    Es un juego de 1 jugador y la computadora, para ganar debe 
    completar 3 caracteres iguales en linea ("x" o "o")
    
    Para ingresar la posicion en el juego, guiese
    con los siguientes numeros
                0  | 1 | 2 | 3
                ------------- 
                4  | 5 | 6 | 7
                ------------- 
                8  | 9 | 10 | 11
                -------------
                12 | 13 | 14 | 15
    =====================================================
    """
    print(explicacion)
    input("...Ingrese enter para empezar el juego...")

tableroLista = ["1", "2", "3", "4",None,None,None,None,None, None,None,None,None,None,None]

def dibujarTablero(tableroLogico:list):
    tableroVisual = """
                {}  | {} | {} | {}
                ------------------   
                {}  | {} | {} | {}
                ------------------ 
                {}  | {} | {} | {}
                ------------------
                {}  | {} | {} | {}
    """.format(tableroLogico[0], tableroLogico[1],
               tableroLogico[2], tableroLogico[3],
               tableroLogico[4], tableroLogico[5],
               tableroLogico[6], tableroLogico[7],
               tableroLogico[8],tableroLogico[9],
               tableroLogico[10],tableroLogico[11],
               tableroLogico[12],tableroLogico[13],
               tableroLogico[14],tableroLogico[15])
    tableroVisual = tableroVisual.replace("None", " ")
    print(tableroVisual)


