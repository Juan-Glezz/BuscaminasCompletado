import random

class Casilla:
    def __init__(self):
        self.contieneMina = False
        self.minasAdyacentes = 0
        self.adyacentes = []

class Tablero:
    def __init__(self, fila, columna, minas):
        self.fila = fila
        self.columna = columna
        self.minas = minas
        self.tabla = [[Casilla() for _ in range(columna)] for _ in range(fila)]
        self.colocadorMinas()
        self.CalculoAdyacentes()
        

    def colocadorMinas(self):
        minasColocadas = 0
        while minasColocadas < self.minas:
            fila = random.randint(0, self.fila - 1)
            columna = random.randint(0, self.columna - 1)
            if not self.tabla[fila][columna].contieneMina:
                self.tabla[fila][columna].contieneMina = True
                minasColocadas += 1

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

    
            