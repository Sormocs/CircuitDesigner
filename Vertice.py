import Resistencia
import Fuente

class Vertice:

    """Clase que crea los nodos que iran almacenos en el grafo
    """

    def __init__(self, i,n,v,a,t,pos):

        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.name = n
        self.v = v
        self.a = a
        self.t = t
        self.distancia = float('inf')
        self.CrearComponente(n,v,a,t)
        self.pos = pos

    def GetName(self):
        """retorna el nombre"""
        return self.name

    def GetPos(self):
        """retorna la posicion"""
        return self.pos

    def GetV(self):
        """retorna el voltaje"""
        return self.v

    def GetA(self):
        """retorna los amperios"""
        return self.a

    def GetT(self):
        """retorna el tipo"""
        return self.t

    def AgregarVecino(self, vertice, valor):

        """agrega una arista que conecta 2 nodos, recibe el nodo al cual se quiere conectar y el valor de dicha arista"""

        print("Hola")
        self.vecinos.append([vertice, valor])

    def CrearComponente(self,n,v,a,t):

        """Crea el componente si es una resistencia o una fuente, parametros: nombre, voltaje, amperios y tipo"""

        if t:
            self.componente = Fuente.fuente(n,v)
        else:
            self.componente = Resistencia.Resistencia(n,v,a)

