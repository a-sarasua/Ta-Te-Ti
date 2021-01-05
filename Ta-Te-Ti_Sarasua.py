def inicializarTablero():
    """Crea el tablero de juego mediante una lista."""
    tablero = [
        ['|','_', '|', '_','|','_','|'],
        ['|','_', '|', '_','|','_','|'],
        ['|','_', '|', '_','|','_','|']
    ]
    return(tablero)

def dibujarTablero(tablero):
    """Imprime en pantalla al tablero."""
    for i in range(3): 
        print(''.join(tablero[i]))

def elegirSimbolo():
    """Permite elegir el símbolo al jugador"""
    while True:
        jugador1 = input('Ingrese O o X para el jugador 1 (el jugador 2 será el otro): ').upper()
        if jugador1 == 'O':
            jugador2 = 'X'
            return(jugador1, jugador2)
        elif jugador1 == 'X':
            jugador2 = 'O'
            return(jugador1, jugador2)
        else:
            print("Valor incorrecto, vamos de nuevo")

def ingresarJugada():
    """Pide un valor para la fila o la columna y se fija si es válido."""
    while True:
        try:
            valorIngresado = int(input('Ingrese un valor entre 1 y 3: '))
            if valorIngresado == 3 or valorIngresado == 2 or valorIngresado ==1:
                return valorIngresado
            else:
                print('Número equivocado')
        except: 
            print('¡Tiene que ser un número!')

def chequearJugada(fila, columna, ocupado):
    """Se fija si el espacio está ocupado."""
    fila -= 1
    if columna == 2:
        columna +=1
    elif columna ==3:
        columna +=2
    if tablero[fila][columna] == '_':
        ocupado = False
        return (fila, columna, ocupado)
    else:
        print('Ese lugar está ocupado, probá con otro.')
        return (0, 0, True) 

def completarTablero(jugador, fila, columna):
    """Completa el tablero con el valor ingresado."""
    tablero[fila][columna] = jugador
    return tablero

def consultarGanador(jugador):
    """Compara todos los casos posibles para ver si hay un ganador."""
    if ((tablero[0][1] == jugador and tablero[0][3] == jugador and tablero[0][5] == jugador) or 
    (tablero[1][1] == jugador and tablero[1][3] == jugador and tablero[1][5] == jugador) or 
    (tablero[2][1] == jugador and tablero[2][3] == jugador and tablero[2][5] == jugador) or 
    (tablero[0][1] == jugador and tablero[1][1] == jugador and tablero[2][1] == jugador) or 
    (tablero[0][3] == jugador and tablero[1][3] == jugador and tablero[2][3] == jugador) or 
    (tablero[0][5] == jugador and tablero[1][5] == jugador and tablero[2][5] == jugador) or
    (tablero[0][1] == jugador and tablero[1][3] == jugador and tablero[2][5] == jugador) or
    (tablero[0][5] == jugador and tablero[1][3] == jugador and tablero[2][1] == jugador)):
        ganador = True
        return ganador
    else: 
        ganador = False
        return ganador    

def juego(jugador):
    """Resume cada turno del jugador en cuestión."""
    ocupado = True
    while ocupado == True:
        print('Elegí una fila')            
        fila = ingresarJugada()
        print('Ahora elegí una columna')
        columna = ingresarJugada()
        fila, columna, ocupado = chequearJugada(fila, columna, ocupado)
    completarTablero(jugador, fila, columna)
    dibujarTablero(tablero)
    ganador = consultarGanador(jugador)
    return ganador

def elegirJugador(jugador1, jugador2, tablero):
    """Cambia entre jugadores hasta terminar el juego."""
    print('Arranquemos el juego')
    for i in range(1, 10):
        if i % 2 == 1:
            print('Le toca al jugador 1')
            ganador = juego(jugador1)
            if ganador == True:
                print('¡El jugador 1 ha ganado!')
                return
        if i % 2 == 0:
            print('Le toca al jugador 2')
            ganador = juego(jugador2)
            if ganador == True:
                print('¡El jugador 2 ha ganado!')
                return
    print('¡Hubo un empate!')
    return 

jugar = True
while jugar == True:
    tablero = inicializarTablero()
    print('Juguemoso al Ta Te Ti. Vamos a jugar en este tablero:')
    dibujarTablero(tablero)
    jugador1, jugador2 = elegirSimbolo()
    elegirJugador(jugador1, jugador2, tablero)
    respuestaUsuario = input('¿Quieren jugar de vuelta? Responda "si" o "no": ').upper()
    if respuestaUsuario == 'SI':
        continue
    elif respuestaUsuario == 'NO':
        print("Está bien, aquí termina el programa.")
        jugar = False
    else: 
        print("No se reconoce su respuesta, fin del programa.")
        jugar = False
