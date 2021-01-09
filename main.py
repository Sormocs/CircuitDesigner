from Button import Button
from Calculos import Formulas
import Grafo
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Circuit Designer")

def GrafoGen():
    grafo = Grafo.Grafo()

    grafo.AgregarVertice(1, "hola", 50)
    grafo.AgregarVertice(2, "hola", 50)
    grafo.AgregarVertice(3, "feo", 50)
    grafo.AgregarVertice(4, "hola", 50)
    grafo.AgregarVertice(5, "hola", 50)
    grafo.AgregarVertice(6, "juan", 50)
    grafo.AgregarArista(1,6,5222222)
    grafo.AgregarVertice(6, "hola", 50)
    grafo.AgregarArista(1, 6, 5222222)
    grafo.AgregarArista(1, 3, 23)
    grafo.AgregarArista(3, 4, 11)
    grafo.AgregarArista(4, 6, 1)

    grafo.Dikjstra(1)
    print(grafo.Camino(1, 6))
    print(grafo.vertices)

def Main_Win():
    run = True
    # BOTON: color boton, posicion x, posicion y, ancho, altura, tamano de letra, texto, color texto
    createbtn = Button((255, 255, 255), 230, 265, 150, 60, 26, "Crear", (160, 160, 160))
    importbtn = Button((255, 255, 255), 420, 265, 150, 60, 26, "Importar", (160, 160, 160))
    while run:
        screen.fill((0, 0, 0))
        createbtn.Draw(screen)
        importbtn.Draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if createbtn.Click(pos):
                    GrafoGen()

if __name__ == '__main__':
    Formulas1 = Formulas()
    Main_Win()

    grafo.Eliminar("feo")
    print(grafo.vertices)
