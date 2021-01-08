class Vertice:

    def __init__(self, i, n, v):

        self.valor = v
        self.nombre = n
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padres = None
        self.distancia = float('inf')

    def AgregarVecino(self, vertice, valor):

        if id not in self.vecinos:
            self.vecinos.append([vertice, valor])




