class Resistencia:

    def __init__(self,nombre, valor, amperios):

        self.nombre = nombre
        self.valor = valor

    def SetValor(self, v):
        self.valor = v

    def SetNombre(self,n):
        self.nombre = n

    def GetNombre(self):
        return self.nombre

