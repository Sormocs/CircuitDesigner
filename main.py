from Button import Button
from Calculos import Formulas
from CircuitDesigner import Circuit
import Grafo
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Circuit Designer")

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
                    run = False
                    DesignWin()

def AddRes(graph):

    graph.AgregarVertice("Res1",10,10,False)

def AddPower(graph):

    graph.AgregarVertice("Power",10,10,True)


def DesignWin():
    print(screen)
    CircuitDes = Circuit()
    CircuitDes.RunWin(screen)
if __name__ == '__main__':
    #Formulas1 = Formulas()
    Main_Win()


