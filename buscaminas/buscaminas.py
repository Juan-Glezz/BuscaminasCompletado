import random

#las funciones __init__ es el metodo constructor con el que se  inicializan las variables de las clases

#Esta clase representa una casilla del tablero del juego
#La variable contieneMina es un booleano que indica si la casilla contiene una mina o no.
#La variable minasAdyacentes es un entero que indica el numeros de minas adaycentes a dicha casilla
#La variable adyacente es una lista que almacena las coordenadas de las casillas adayacentes a esta casilla
class Casilla:
    def __init__(self):
        self.contieneMina = False
        self.minasAdyacentes = 0
        self.adyacentes = []

#Esta clase representa el tablero del buscaminas
#La variable fila es un entero que indica el numero de filas en el tablero
#La variable columna es un entero que indica el numero de columna en el tablero
#La variable minas es un entero que indica el numero total de minas que contendra el tablero
#La variable tabla es una lista que representa el tablero y contiene objetos de la clase casilla
#La funcion colocadorMinas es una funcion que coloca aleatoriamente las mians en el tablero
#La funcion CalculoAdyacentes es una funcion que calcula el numero de minas adayacentes en cada casilla del tablero
class Tablero:
    def __init__(self, fila, columna, minas):
        self.fila = fila
        self.columna = columna
        self.minas = minas
        self.tabla = [[Casilla() for _ in range(columna)] for _ in range(fila)]
        self.colocadorMinas()
        self.CalculoAdyacentes()
        
#Esta funcion se encarga  de colocar minas en poisciones no ocupadas en el tablero,esto haciendose
#a traves de un bucle  while que genera aleatoriamnete una posicions dentro de la tabla(siempre que la cantidad 
# de minas sea menor que el total de minas que se colocan) utilizando la funcion random en varibales de fila  
# y columna, posteriormente comprueba de que dicha posicion no este ya ocupada por una minas y si no eesta
#ocupada se crea en esacasilla una mina y asi repitiendose hasta llegar al nuemero que establezacmos en ek formulario 
    def colocadorMinas(self):
        minasColocadas = 0
        while minasColocadas < self.minas:
            fila = random.randint(0, self.fila - 1)
            columna = random.randint(0, self.columna - 1)
            if not self.tabla[fila][columna].contieneMina:
                self.tabla[fila][columna].contieneMina = True
                minasColocadas += 1
#Esta funcion se encarga de de calcular el numero de minas adyacentes en  cada casilla,
#utilizando bucles anidados para recorrer todas las casillas del tablero y posteriormente comprobar
#las casillas adyacentees en cada una de ellas
    def CalculoAdyacentes(self):
        for fila in range(self.fila):
            for columna in range(self.columna):
                casilla = self.tabla[fila][columna]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= fila + i < self.fila and 0 <= columna + j < self.columna:
                            casilla.adyacentes.append((fila + i, columna + j))
                            if self.tabla[fila + i][columna + j].contieneMina:
                                casilla.minasAdyacentes += 1
#ESra funcion se encarga de mostrar el tablero, creando una lista padre (tabla_tablero),
#que representa el estado actual de dicho tablero y guarda el simbolo correspondiente en dicha lista
#Devolviendo asi dicha lista que seria el tablero del busca minas
    def muestraTablero(self):
        tabla_tablero = []
        for fila in range(self.fila):
            tabla_fila = []
            for columna in range(self.columna):
                casilla = self.tabla[fila][columna]
                if casilla.contieneMina:
                    tabla_fila.append('💣')
                elif casilla.minasAdyacentes > 0:
                    tabla_fila.append(str(casilla.minasAdyacentes))
                else:
                    tabla_fila.append('ㅤ')
            tabla_tablero.append(tabla_fila)

        return tabla_tablero

    
            