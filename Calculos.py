class Formulas():

    """Clase para las formulas del modo simulacion"""

    __instance = None

    def __new__(cls):
        if Formulas.__instance is None:
            Formulas.__instance = object.__new__(cls)
        return Formulas.__instance

    def CalcCorriente(self,v,r):
        """Calcula corriente"""
        i = float(v)/float(r)
        return i

    def CalcTension(self,i,r):
        """Calcula tension"""

        v = float(i)*float(r)
        return v

    def CalcResistencia(self,v,i):
        """Calcula el valor de la resistencia"""
        r = float(v)/float(i)
        return r

