import Resistencia
import Fuente

class Vertice:

    def __init__(self, i,n,v,a,t,pos):

        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')
        self.CrearComponente(n,v,a,t)
        self.pos = pos

    def AgregarVecino(self, vertice, valor):

        if id not in self.vecinos:
            self.vecinos.append([vertice, valor])

    def CrearComponente(self,n,v,a,t):

        if t:
            self.componente = Fuente.fuente(n,v)
        else:
            self.componente = Resistencia.Resistencia(n,v,a)
