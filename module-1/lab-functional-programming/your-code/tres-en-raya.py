# Ejercicio planteado y validado por Elena, Rafa y Fer.
# Antes de nada, debo decir que este código no está optimizado, ya que he juntado el de multijugador y
# el de contra la máquina, para dar a elegir el modo con un solo código, pero hay varias funciones y
# muchas líneas que podrían optimizarse. Sé que es una chapu, sería cuestión de meterse un rato más,
# pero prefiero dedicar tiempo a otros labs. Pero funcionar, ¡funciona! :P
# Nota: habíamos pensado pedir el nombre del jugador, y llamar a los jugadores por su nombre en lugar de "Jugador 1" o "Jugador 2",
# pero creemos que hace la jugabilidad más coñazo. Lo dejamos así para que sea más dinámico.
# Nota2: solo nos hemos encontrado un "problema". Nos imprime dos veces seguidas el mensaje del ganador (¿?)

import random
import time # Para poder usar sleep, para que la máquina no tire de forma inmediata.
import os # Para poder limpiar la pantalla si el jugador quiere seguir jugando una partida nueva.

# Función para imprimir el tablero
def print_tablero(tablero):
    [print(fila) for fila in tablero]

# Función para tirar una ficha y comprobar si cae en el tablero y si la posición está libre (Multijugador)
def tirar_ficha_multijugador(huecos):
    # Pedimos número de fila
    fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")
    # Comprobamos que la fila está dentro del rango
    while fila not in ["1", "2", "3"]:
        print("Fila inválida. Tienes que meter la ficha dentro del tablero.")
        fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")
    
    # Pedimos número de columna
    col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")
    # Comprobamos que la columna está dentro del rango
    while col not in ["1", "2", "3"]:
        print("Columna inválida. Tienes que meter la ficha dentro del tablero.")
        col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")
    
    # Comprobamos si la posición está libre
    while tablero[int(fila)-1][int(col)-1] != "-":
        print("Posición inválida. El hueco no está libre.")
        # Las siguientes 8 líneas son repetidas de arriba, por lo que se podría crear una función para comprobar solo el rango.
        fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")
        while fila not in ["1", "2", "3"]:
            print("Fila inválida. Tienes que meter la ficha dentro del tablero.")
            fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")
        col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")
        while col not in ["1", "2", "3"]:
            print("Columna inválida. Tienes que meter la ficha dentro del tablero.")
            col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")
    # Asignamos "x" o "o" en función del turno del jugador
    if huecos%2 != 0:
        tablero[int(fila)-1][int(col)-1] = "x"
    else:
        tablero[int(fila)-1][int(col)-1] = "o"
    return tablero

# Función para tirar una ficha y comprobar si cae en el tablero y si la posición está libre (Modo máquina)
def tirar_ficha_modomaquina(huecos):
    if huecos%2 != 0:
        # Pedimos número de fila
        fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")
        # Comprobamos que la fila está dentro del rango
        while fila not in ["1", "2", "3"]:
            print("Fila inválida. Tienes que meter la ficha dentro del tablero.")
            fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")

        # Pedimos número de columna
        col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")
        # Comprobamos que la columna está dentro del rango
        while col not in ["1", "2", "3"]:
            print("Columna inválida. Tienes que meter la ficha dentro del tablero.")
            col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")

        # Comprobamos si la posición está libre
        while tablero[int(fila)-1][int(col)-1] != "-":
            print("Posición inválida. El hueco no está libre.")
            # Las siguientes 8 líneas son repetidas de arriba, por lo que se podría crear una función para comprobar solo el rango.
            fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")
            while fila not in ["1", "2", "3"]:
                print("Fila inválida. Tienes que meter la ficha dentro del tablero.")
                fila = input("Introduce un número de fila (de 1 a 3) en el que haya un hueco libre: ")
            col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")
            while col not in ["1", "2", "3"]:
                print("Columna inválida. Tienes que meter la ficha dentro del tablero.")
                col = input("Introduce un número de columna (de 1 a 3) en el que haya un hueco libre: ")
        tablero[int(fila)-1][int(col)-1] = "x"
    # Ahora viene la tirada de la máquina
    else:
        pos_libres = []
        time.sleep(2) # Hacemos que la máquina tarde dos segundos en tirar
        if tablero[1][1] == "-": # Esta es toda la IA que le hemos dado. Si el centro está libre, pone en el centro. Se nos ocurren más cosas, pero no hay tiempo pa to.
            tablero[1][1] = "o"
            print("\nLa máquina ha puesto su ficha.")
        else: # Recorremos el tablero y metemos en una lista todas las posiciones libres
            for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == "-":
                        pos_libres.append([i, j]) 
            ind_random = random.choice(pos_libres) # Seleccionamos al azar una posición libre
            tablero[ind_random[0]][ind_random[1]] = "o" # Asignamos un valor a esa posición
            # En el siguiente print hemos puesto varias frases para que no aparezca siempre la misma, por hacer algo diferente.
            print(random.choice(["\nLa máquina contrataca.", "\nLa máquina ya ha elegido.", "\nOjo con la tirada que acaba de hacer la máquina."]))
    return tablero

# Función para comprobar ganador (Multijugador)
def comprobar_ganador_multijugador(tablero):
    col0 = "" # Primera columna
    col1 = "" # Segunda columna
    col2 = "" # Tercera columna
    cont_fila = 0
    diag1 = "" # Diagonal principal
    diag2 = "" # Diagonal secundaria
    for fila in tablero: # Primero comprobamos si alguna fila tiene ganador
        if "".join(fila) == "xxx":
            print("\nEnhorabuena jugador 1, has ganado.")
            return True
        elif "".join(fila) == "ooo":
            print("\nEnhorabuena jugador 2, has ganado.")
            return True
        # Aprovechamos el bucle para crear variables que faciliten las comprobaciones siguientes de columnas y diagonales
        col0 += tablero[cont_fila][0] # Al final del bucle tendremos un string con los valores de la primera columna
        col1 += tablero[cont_fila][1] # Al final del bucle tendremos un string con los valores de la segunda columna
        col2 += tablero[cont_fila][2] # Al final del bucle tendremos un string con los valores de la tercera columna
        diag1 += tablero[cont_fila][cont_fila] # Al final del bucle tendremos un string con los valores de la diagonal principal
        diag2 += tablero[cont_fila][(cont_fila + 1)*(-1)] # Al final del bucle tendremos un string con los valores de la diagonal secundaria
        cont_fila += 1
    # Comprobamos si alguna columna tiene ganador
    if col0 == "xxx" or col1 == "xxx" or col2 == "xxx":
        print("\nEnhorabuena jugador 1, has ganado.")
        return True
    elif col0 == "ooo" or col1 == "ooo" or col2 == "ooo":
        print("\nEnhorabuena jugador 2, has ganado.")
        return True
    # Comprobamos si alguna diagonal tiene ganador
    elif diag1 == "xxx" or diag2 == "xxx":
        print("\nEnhorabuena jugador 1, has ganado.")
        return True
    elif diag1 == "ooo" or diag2 == "ooo":
        print("\nEnhorabuena jugador 2, has ganado.")
        return True

# Función para comprobar ganador (Modo máquina)
# Es prácticamente igual que la anterior función, solo cambian los mensajes. Para hacerlo solo en una función,
# le pasaríamos como parámetro el modo, y dentro le mostraríamos un mensaje y otro en función del modo (no time to do it, sorry).
def comprobar_ganador_modomaquina(tablero):
    col0 = "" # Primera columna
    col1 = "" # Segunda columna
    col2 = "" # Tercera columna
    cont_fila = 0
    diag1 = "" # Diagonal principal
    diag2 = "" # Diagonal secundaria
    for fila in tablero: # Primero comprobamos si alguna fila tiene ganador
        if "".join(fila) == "xxx":
            print("\nEnhorabuena, has ganado.")
            return True
        elif "".join(fila) == "ooo":
            print("\nHas perdido.")
            return True
        # Aprovechamos el bucle para crear variables que faciliten las comprobaciones siguientes de columnas y diagonales
        col0 += tablero[cont_fila][0] # Al final del bucle tendremos un string con los valores de la primera columna
        col1 += tablero[cont_fila][1] # Al final del bucle tendremos un string con los valores de la segunda columna
        col2 += tablero[cont_fila][2] # Al final del bucle tendremos un string con los valores de la tercera columna
        diag1 += tablero[cont_fila][cont_fila] # Al final del bucle tendremos un string con los valores de la diagonal principal
        diag2 += tablero[cont_fila][(cont_fila + 1)*(-1)] # Al final del bucle tendremos un string con los valores de la diagonal secundaria
        cont_fila += 1
    # Comprobamos si alguna columna tiene ganador
    if col0 == "xxx" or col1 == "xxx" or col2 == "xxx":
        print("\nEnhorabuena, has ganado.")
        return True
    elif col0 == "ooo" or col1 == "ooo" or col2 == "ooo":
        print("\nHas perdido.")
        return True
    # Comprobamos si alguna diagonal tiene ganador
    elif diag1 == "xxx" or diag2 == "xxx":
        print("\nEnhorabuena, has ganado.")
        return True
    elif diag1 == "ooo" or diag2 == "ooo":
        print("\nHas perdido.")
        return True

######################################## Tras haber definido las funciones, empieza el juego.
seguir_jugando = "s" # Para darle la opción de seguir jugando tras la primera partida.
while seguir_jugando == "s":
    tablero = [["-", "-","-"],["-", "-","-"],["-", "-","-"]] # El guión es igual a vacío. Lo hemos representado así porque creemos que se visualiza mejor que el espacio.
    # Le damos a elegir entre modo multijugador o contra la máquina.
    modo = input("¿Quieres jugar contra otro jugador o contra la máquina? Teclea 'j' para multijugador o 'm' para jugar contra la máquina: ")
    while modo not in ["j", "m"]:
        modo = input("Una de dos: o no sabes leer o no sabes escribir. Teclea 'j' para multijugador o 'm' para jugar contra la máquina: ")

    if modo.lower() == 'j':
        print("Has elegido multijugador.")
        print("\n¡Empieza la partida! A continuación verás el tablero vacío")
        huecos = 9 # Posiciones vacías en el tablero. Iremos restando cada turno. Sirve para saber en qué turno estamos en función de si par o impar.
        fin = False # Se pondrá a True cuando alguien gane.
        while fin == False and huecos > 0:
            print_tablero(tablero)
            if huecos%2 != 0:
                print("\nJugador 1, tu turno.")
            else:
                print("\nJugador 2, tu turno.")
            tirar_ficha_multijugador(huecos)
            huecos -=1
            if huecos <= 4: # Esto es para que no compruebe ganador hasta que haya como mínimo 5 fichas en el tablero
                comprobar_ganador_multijugador(tablero)
                if comprobar_ganador_multijugador(tablero):
                    print_tablero(tablero)
                    fin = True
    else:
        print("Juegas contra la máquina.")
        huecos = 9
        # Le damos a elegir quién empieza, jugador o máquina.
        empezar_yo = input("\n¿Quieres empezar tú?(s/n) Teclea 's' para empezar tú o 'n' para que empiece la máquina: ")
        if empezar_yo.lower() == 's':
            print("\nCagón")
            print("¡Empieza la partida! A continuación verás el tablero vacío")
            print_tablero(tablero)
        elif empezar_yo.lower() == 'n':
            print("\n¡Valiente!")
            print("¡Empieza la partida! Turno para la máquina ")
            tirar_ficha_modomaquina(huecos-1)
            print_tablero(tablero)
        else:
            print("\nComo no sabes ni escribir, empieza la máquina")
            tirar_ficha_modomaquina(huecos-1)
            print_tablero(tablero)
        fin = False

        while fin == False and huecos > 0:
            if huecos <= 8:
                print_tablero(tablero)
            if huecos%2 != 0:
                print("\nTu turno.")
            tirar_ficha_modomaquina(huecos)
            huecos -=1
            if huecos <= 4: # Esto es para que no compruebe ganador hasta que haya como mínimo 5 fichas en el tablero
                comprobar_ganador_modomaquina(tablero)
                if comprobar_ganador_modomaquina(tablero):
                    print_tablero(tablero)
                    fin = True
            if empezar_yo.lower() != 's' and huecos == 1: # Tengo que hacer esto para que, en caso de que hubiese empezado la máquina, salga del while en caso de nadie gane.
                huecos -=1

    if huecos == 0 and fin == False: # Si el número de posiciones vacías es 0 y nadie ha ganado, hay tablas.
        print("\nSon tablas.")
        print_tablero(tablero)

    print("\nPartida finalizada.")
    seguir_jugando = input("\n¿Quieres seguir jugando?(s/n): ")
    while seguir_jugando not in ["s","n"]:
        seguir_jugando = input("Introduce 's' si quieres seguir jugando o 'n' para dejar de jugar: ")
    if seguir_jugando == "n":
        print("\n¡Gracias por jugar! Vuelve pronto.")
    elif seguir_jugando == "s":
        os.system('clear') # En caso de que quiera seguir jugando, limpiamos la pantalla.