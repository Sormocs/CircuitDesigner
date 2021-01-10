from Button import Button
from Calculos import Formulas
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

def DesignWin():
    # BOTON: color boton, posicion x, posicion y, ancho, altura, tamano de letra, texto, color texto
    addbtn = Button((255, 255, 255), 830, 30, 150, 60, 26, "Agregar", (160, 160, 160))
    deletebtn = Button((255, 255, 255), 830, 120, 150, 60, 26, "Eliminar", (160, 160, 160))
    SimuationBTN =  Button((255, 255, 255), 830, 480, 150, 60, 26, "Simular", (160, 160, 160))
    pygame.display.set_mode((1000,600))
    run = True
    while run:
        screen.fill((0,0,0))
        addbtn.Draw(screen)
        deletebtn.Draw(screen)
        SimuationBTN.Draw(screen)
        pygame.draw.rect(screen, (95, 158, 160), [20, 100, 800, 400])
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    #Formulas1 = Formulas()
    Main_Win()


