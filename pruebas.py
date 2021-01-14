import Grafo

g = Grafo.Grafo()

g.AgregarVertice("dad",12,12,False)
g.AgregarVertice("dad1",12,12,False)
g.AgregarVertice("dad2",12,12,False)
g.AgregarVertice("dad3",12,12,False)
g.AgregarVertice("dad4",12,12,False)
g.AgregarVertice("dad5",12,12,False)
g.AgregarVertice("dad7",12,12,False)
g.AgregarVertice("dad8",12,12,False)

g.AgregarArista(1,2,5)
g.AgregarArista(2,4,3)
g.AgregarArista(4,6,1)
g.AgregarArista(1,6,100)

print(g.vertices)
g.Eliminar("dad1")
print(g.vertices)

g.DikjstraMaximo(1)
print("El camino maximo seria "  + str(g.Camino(1,6)))
g.DikjstraMinimo(1)
print("el camino minimo seria " + str(g.Camino(1,6)))


