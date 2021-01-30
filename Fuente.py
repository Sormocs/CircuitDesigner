class fuente:

    """Clase del componente fuente"""

    def __init__(self,n,v):

        self.nombre = n
        self.voltaje = v

    def GetNombre(self):
        """Retorna el nombre de la fuente"""
        return self.nombre
