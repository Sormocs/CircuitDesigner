from Grafo import Grafo
from Json import *

g = Grafo()

g.AgregarVertice("dad",12,12,False,[1,2])
g.AgregarVertice("dad1",12,12,False,[1,2])
g.AgregarVertice("dad2",12,12,False,[1,2])
g.AgregarVertice("dad3",12,12,False,[1,2])
g.AgregarVertice("dad3",12,12,False,[1,2])


g.AgregarArista(1,2,3)
g.AgregarArista(1,4,8)
g.AgregarArista(1,3,15)
g.AgregarArista(2,4,3)
g.AgregarArista(3,4,8)
g.AgregarArista(4,5,3)



a = [1,2,3,4,5,6,7,8,9]

for i in a:

    if i == 3:
        a.remove(i)

print(a)

# g.Eliminar("dad1")
# print(g.vertices)
#
g.DikjstraMaximo(1)
print("El camino maximo seria "  + str(g.Camino(1,5)))
g.DikjstraMinimo(1)
print("el camino minimo seria " + str(g.Camino(1,5)))


