import Vertice

class Grafo:

    def __init__(self):
        self.vertices = {}
        self.id = 1

    def AgregarVertice(self,n,v,a,t):

        self.vertices[self.id] = Vertice.Vertice(self.id,n,v,a,t)
        self.id+=1

    def AgregarArista(self, inicio, fin, valor):

        if inicio in self.vertices and fin in self.vertices:
            self.vertices[inicio].AgregarVecino(fin, valor)
            #self.vertices[fin].AgregarVecino(inicio, volts)


    def BuscarID(self, nombre):

        for i in self.vertices:


            if self.vertices[i].componente.GetNombre() == nombre:

                return self.vertices[i].id

    def Eliminar(self, nombre):
        #cambiar
        id = self.BuscarID(nombre)
        del(self.vertices[id])
        self.EliminarArita(id)

    def EliminarArita(self, id):

        for i in self.vertices:
            for j in self.vertices[i].vecinos:
                if j[0] == id:
                    self.vertices[i].vecinos.remove(j)

        for i in self.vertices:
            if self.vertices[i].padre == id:
                self.vertices[i].padre = None

    def CambiarValorArista(self, id,valor):

        for i in self.vertices[id].vecinos:
            i[1] = valor

    def Camino(self, a, b):

        camino = []
        actual = b

        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre

        return [camino, self.vertices[b].distancia]

    def Minimo(self, lista):

        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]

            for i in lista:
                if m > self.vertices[i].distancia:
                    m = self.vertices[i].distancia
                    v = i

            return v

    def Maximo(self, lista):

        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]

            for i in lista:
                if m < self.vertices[i].distancia:
                    m = self.vertices[i].distancia
                    v = i

            return v

    def ResetearVisitado(self):

        for i in self.vertices:

            self.vertices[i].visitado = False

    def DikjstraMinimo(self, vertice):

        self.ResetearVisitado()

        if vertice in self.vertices:
            self.vertices[vertice].distancia = 0
            actual = vertice
            noVisitados = []

            for i in self.vertices:
                if i != vertice:
                    self.vertices[i].distancia = float('inf')

                self.vertices[i].padre = None
                noVisitados.append(i)

            while len(noVisitados) > 0:

                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.Minimo(noVisitados)

        else:
            return False


    def DikjstraMaximo(self, vertice):

        self.ResetearVisitado()

        if vertice in self.vertices:
            self.vertices[vertice].distancia = 0
            actual = vertice
            noVisitados = []

            for i in self.vertices:
                if i != vertice:
                    self.vertices[i].distancia = float('inf')

                self.vertices[i].padre = None
                noVisitados.append(i)

            while len(noVisitados) > 0:

                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.Maximo(noVisitados)

        else:
            return False



    def EditarVertice(self,i,n,v):

        self.vertices[i].nombre = n
        self.vertices[i].volts = v

    def GenerarLista(self):

        lista = []

        for i in self.vertices:

            lista.append(self.vertices[i])

        return  lista
