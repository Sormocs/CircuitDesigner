class Formulas():

    __instance = None

    def __new__(cls):
        if Formulas.__instance is None:
            Formulas.__instance = object.__new__(cls)
        return Formulas.__instance

