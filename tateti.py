tablero = [ "-","-","-",
            "-","-","-",
            "-","-","-",]

ganador = None
def jugar():
    global ganador
    print("Empieza el juego")
    ver_tablero()
    for i in range(5):
        print("Turno del jugador 1 - x")
        valor="X"
        #empieza a jugar - jugador 1
        jugada(valor)
        huboGanador()
        if ganador != "X" and i < 4 :    
            for j in range(3):
                print("Turno del jugador 2 - O")
                valor="O"
                jugada(valor)
                huboGanador()
                if ganador == "O":
                    print("Felicidades jugador 2")
                break
        elif ganador=="X":
            print("Felicidades jugador 1")
            break
        else:
            print("empataron")
def huboGanador():
    global ganador
    controlLinea()
    controlVertical()
    controlDiagonal()
def controlLinea():
    global ganador
    if tablero[0] == [1] == [2] !="-":
        ganador = tablero[0]
    elif tablero[3] == [4] == [5] !="-":
        ganador = tablero[3]
    elif tablero[6] == [7] == [8] !="-":
        ganador = tablero[6]
def controlVertical():
    global ganador
    if tablero[0] == [3] == [6] !="-":
        ganador = tablero[0]
    elif tablero[1] == [4] == [7] !="-":
        ganador = tablero[1]
    elif tablero[2] == [5] == [8] !="-":
        ganador = tablero[2]
def controlDiagonal():
    global ganador
    if tablero[0]== [4]== [8]!= "-":
        ganador = tablero[0]
    elif tablero[2]== [4]== [6]!="-":
        ganador = tablero[2]
def jugada(valor):
    anoto = False
    while anoto==False:
        posicion = int(input("Elegi una posicion del 1 al 9: "))
        posicion -= 1 
        if tablero[posicion] == "-":
            anoto = True
        else:
            print("Esa posicion ya a sido ocupada")
    tablero[posicion] = valor
    ver_tablero()
def ver_tablero():
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2] + "        1 | 2 | 3" )
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5] + "        4 | 5 | 6" )
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8] + "        7 | 8 | 9" )
    print("\n")

jugar()
