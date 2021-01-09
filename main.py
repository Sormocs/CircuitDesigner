import Grafo


if __name__ == '__main__':

    grafo = Grafo.Grafo()

    grafo.AgregarVertice(1, "hola", 50)
    grafo.AgregarVertice(2, "hola", 50)
    grafo.AgregarVertice(3, "feo", 50)
    grafo.AgregarVertice(4, "hola", 50)
    grafo.AgregarVertice(5, "hola", 50)
    grafo.AgregarVertice(6, "juan", 50)
    grafo.AgregarArista(1,6,5222222)
    grafo.AgregarArista(1, 3, 23)
    grafo.AgregarArista(3, 4, 11)
    grafo.AgregarArista(4, 6, 1)

    grafo.Dikjstra(1)
    print(grafo.Camino(1, 6))

    print(grafo.vertices)

    grafo.Eliminar("feo")
    print(grafo.vertices)
