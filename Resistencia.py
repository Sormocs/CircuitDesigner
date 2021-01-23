class Resistencia:

    """Clase del componente resistencia"""

    def __init__(self,nombre, voltaje, amperios):

        self.nombre = nombre
        self.voltaje = voltaje
        self.amperios = amperios

    def SetValor(self, v):
        self.valor = v

    def SetNombre(self,n):
        self.nombre = n

    def GetNombre(self):
        return self.nombre

