import Grafo


if __name__ == '__main__':

    grafo = Grafo.Grafo()

    grafo.AgregarVertice(1, "hola", 50)
    grafo.AgregarVertice(2, "hola", 50)
    grafo.AgregarVertice(3, "hola", 50)
    grafo.AgregarVertice(4, "hola", 50)
    grafo.AgregarVertice(5, "hola", 50)
    grafo.AgregarVertice(6, "hola", 50)
    grafo.AgregarArista(1,2,5)
    grafo.AgregarArista(1, 3, 23)
    grafo.AgregarArista(1, 4, 11)
    grafo.AgregarArista(1, 5, 141)
    grafo.AgregarArista(1, 6, 131)
    grafo.AgregarArista(2, 1, 13)
    grafo.AgregarArista(2, 4, 23)
    grafo.AgregarArista(2, 5, 134)
    grafo.AgregarArista(5, 6, 213)

    grafo.Dikjstra(1)
    print(grafo.Camino(1,6))



