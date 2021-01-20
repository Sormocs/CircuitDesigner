import Vertice

class Grafo:

    def __init__(self):
        self.vertices = {}
        self.aristas = []
        self.id = 1

    def GetVertices(self):
        return self.vertices

    def GetAristas(self):
        return self.aristas

    def AgregarVertice(self,n,v,a,t,c):

        self.vertices[self.id] = Vertice.Vertice(self.id,n,v,a,t,c)
        self.id+=1

    def AgregarArista(self, inicio, fin, valor):

        if inicio in self.vertices and fin in self.vertices:
            self.aristas.append([inicio,fin,valor])
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
        self.EliminarArista(id)

    def EliminarArista(self, id):

        for i in self.vertices:
            for j in self.vertices[i].vecinos:
                if j[0] == id:
                    self.vertices[i].vecinos.remove(j)

        for i in self.vertices:
            if self.vertices[i].padre == id:
                self.vertices[i].padre = None

        for i in self.aristas:
            if i[0] == id:
                self.aristas.remove(i)


    def EliminarAristaEspecifica(self, id1, id2):
        for i in self.aristas:
            if i[0] == id1 and i[1] == id2:
                self.aristas.remove(i)

        for i in self.vertices[id1].vecinos:
            if j[0] == id2:
                self.vertices[id1].vecinos.remove(j)

    def CambiarValorArista(self, id,valor):

        for i in self.vertices[id].vecinos:
            i[1] = valor

    def CambiarPos(self, coords, id):

        self.vertices[id].pos = coords

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

    def Show(self):
        vertices = self.GenerarLista()
        print("~~~~~~~~~~~~~~")
        for v in vertices:
            print(v.GetName())
            print(v.GetPos())

        print("~~~~~~~~~~~~~~")

        for e in self.aristas:
            print("Aristas:")
            print(e[0])
            print(e[1])
            print(e[2])

        print("~~~~~~~~~~~~~~")
