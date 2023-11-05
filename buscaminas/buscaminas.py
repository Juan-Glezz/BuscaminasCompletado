import random
from views import coor_minas

class Casillas:
    def __init__(self, coordenadas, minass=false, mina_adyacente=0)
        self.adya=adya
        self.minass=minass
        self.mina_adyacente=mina_adyacente
    def __str__(self):
        return f"({self.fila}, {self.columna})"
        
class Tablero:
    def __init__(self, columna, fila, numMina):
        self.columna=columna
        self.fila=fila
        self.minas=minas
        self.casillas=[]

         for fila in range(fila):
            for columna in range(columna):
                coordenadas = (fila, columna)
                minas = False
                casilla = Casilla(coordenadas, minas)
                self.casillas.append(casilla)
                coor_minas = set()
            for i in range(5):
                randomFila = random.randint(0, fila - 1)
                randomColumna = random.randint(0, columna - 1)
                coor_minas.add((fila, columna))
            for casilla in self.casillas:
            fila, columna = casilla.coordenadas
            adyacentes_coords = [
                (fila-1, columna-1), (fila-1, columna), (fila-1, columna+1),
                (fila, columna-1),                     (fila, columna+1),
                (fila+1, columna-1), (fila+1, columna), (fila+1, columna+1)
            ]
            for coords in adyacentes_coords:
                fila_ady, columna_ady = coords
                if (0 <= fila_ady < self.num_filas) and (0 <= columna_ady < self.num_columnas):
                    adyacente = self.get_casilla(coords)
                    if adyacente.contiene_mina:
                        casilla.num_minas_adyacentes += 1
        def get_casilla(self, coordenadas):
            for casilla in self.casillas:
                if casilla.coordenadas == coordenadas:
                    return casilla
            return None
    
            