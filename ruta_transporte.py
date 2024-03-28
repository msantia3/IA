"""
La línea de código a continuación (from collections import defaultdict) tiene dos funciones principales:

1. Importar el módulo collections:

El módulo collections proporciona una colección de tipos de datos especializados que son más eficientes 
que los tipos de datos estándar de Python en ciertas situaciones.

2. Importar el tipo de dato defaultdict:

El tipo de dato defaultdict es un diccionario que se diferencia de un diccionario normal en que siempre 
proporciona un valor por defecto para una clave que no existe. Este valor por defecto puede ser un objeto arbitrario, 
como una lista, un conjunto o una función.
"""

from collections import defaultdict

"""
La clase (SistemaTransporte) representa el sistema inteligente para encontrar rutas en el sistema de transporte público.

Atributos:
    reglas: Lista de objetos `Regla` que representan las reglas de negocio que se deben aplicar a las rutas.
    paradas: Lista de las paradas del sistema de transporte.
    conexiones: Lista de tuplas que representan las conexiones entre las paradas, donde cada tupla tiene la forma `(origen, destino, costo)`.
    grafo: Grafo que representa la red de transporte.
"""

class SistemaTransporte:
    def __init__(self, reglas, paradas, conexiones):
        self.reglas = reglas
        self.paradas = paradas
        self.conexiones = conexiones
        self.grafo = self._construir_grafo()

    """
    Construye un grafo que representa la red de transporte.

    Argumentos:
        Ninguno.

    Retorno:
        Un grafo que representa la red de transporte.
    """

    def _construir_grafo(self):
        grafo = defaultdict(list)
        for parada in self.paradas:
            for conexion in self.conexiones:
                if parada == conexion[0]:
                    grafo[parada].append((conexion[1], conexion[2]))
        return grafo

    """
    Aplica las reglas de negocio a una ruta dada.

    Argumentos:
        camino: La ruta a la que se aplicarán las reglas.

    Retorno:
        La ruta modificada después de aplicar las reglas.
    """

    def _aplicar_reglas(self, camino):
        for regla in self.reglas:
            if regla.aplica(camino):
                return regla.aplica(camino)
        return camino

    """
    Encuentra la mejor ruta desde el origen al destino utilizando el algoritmo de Dijkstra y aplicando las reglas de negocio.

    Argumentos:
        origen: La parada de origen.
        destino: La parada de

    destino.

    Retorno:
        La mejor ruta desde el origen al destino, o None si no hay ruta disponible.
    """

    def _mejor_ruta(self, origen, destino):
        visitados = set()
        rutas = [(origen, 0, [])]
        while rutas:
            actual, costo, ruta = rutas.pop(0)
            if actual == destino:
                return ruta  # Se retorna la ruta directamente
            if actual in visitados:
                continue
            visitados.add(actual)
            for vecino, costo_adyacente in self.grafo[actual]:
                nueva_ruta = ruta + [vecino]
                # Se agregó la condición para evitar agregar rutas vacías
                if self._aplicar_reglas(nueva_ruta):
                    rutas.append((vecino, costo + costo_adyacente, nueva_ruta))
        return None

    """
    Busca la ruta entre dos paradas.

    Argumentos:
        origen: La parada de origen.
        destino: La parada de destino.

    Retorno:
        La ruta entre las dos paradas, o "No hay ruta disponible" si no hay ruta disponible.
    """

    def buscar_ruta(self):
        origen = input("Ingrese la parada de origen: ")
        destino = input("Ingrese la parada de destino: ")
        ruta = sistema._mejor_ruta(origen, destino)
        if ruta is None:
            print("No hay ruta disponible entre", origen, "y", destino)
        else:
            coste_total = self._calcular_coste_total(ruta)
            print("La mejor ruta es:", end=" ")
            for parada in ruta[:-1]:  # Se excluye la última parada del bucle
                print(parada, end=" -> ")
            print(ruta[-1])  # Se imprime la última parada sin flecha
            print(f"Coste total: {coste_total}")

    """
    Calcula el coste total del viaje basado en la ruta y la información de las conexiones.

    Argumentos:
        ruta: La lista de paradas que conforman la ruta.

    Retorno:
        El coste total del viaje.
    """

    def _calcular_coste_total(self, ruta):
        coste_total = 0
        for i in range(len(ruta) - 1):
            origen = ruta[i]
            destino = ruta[i + 1]
            for conexion in self.conexiones:
                if origen == conexion[0] and destino == conexion[1]:
                    coste_total += conexion[2]
        return coste_total

"""
Definición de las reglas de negocio.
"""

class Regla:
    def __init__(self, aplica, modifica):
        self.aplica = aplica
        self.modifica = modifica

    def aplica(self, camino):
        return self.aplica(camino)

    def modifica(self, camino):
        return self.modifica(camino)

reglas = [
    # Regla para evitar transbordos
    Regla(lambda camino: len(camino) > 2, lambda camino: camino[1:]),
    # Regla para preferir rutas con menor costo
    Regla(lambda camino: camino[-1] == "E", lambda camino: camino[:-1]),
]

"""
Definición de las paradas y las conexiones del sistema de transporte.
"""

paradas = ["A", "B", "C", "D", "E"]

conexiones = [
    ("A", "B", 10),
    ("A", "C", 20),
    ("B", "D", 30),
    ("C", "D", 40),
    ("D", "E", 50),
]

"""
Creación de una instancia del sistema de transporte.
"""

sistema = SistemaTransporte(reglas, paradas, conexiones)

ruta = sistema.buscar_ruta()

