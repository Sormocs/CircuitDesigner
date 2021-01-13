class Formulas():

    __instance = None

    def __new__(cls):
        if Formulas.__instance is None:
            Formulas.__instance = object.__new__(cls)
        return Formulas.__instance

    def CalcCorriente(self,v,r):
        i = v/r
        imA = i/1000
        return imA

    def CalcTension(self,i,r):
        v = i*r
        return v

    def CalcResistencia(self,i,v):
        r = v/i
        return r

