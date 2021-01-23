from Button import Button
from Calculos import Formulas
from CircuitDesigner import Circuit
from Simulation import SimWin
from EntryBox import EntryBox
import Json
import Grafo
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Circuit Designer")

def Main_Win():
    bg = pygame.image.load('.\Images\CDBG.png')
    run = True
    # BOTON: color boton, posicion x, posicion y, ancho, altura, tamano de letra, texto, color texto
    createbtn = Button((0, 0, 0), 310, 275, 150, 60, 26, "Create", (0, 191, 255))
    importbtn = Button((0, 0, 0), 310, 375, 150, 60, 26, "Import", (0, 191, 255))

    f_name = EntryBox("Introduce name:", 310, 405, 40, 180)
    read = Button((0,0,0), 310, 460, 120, 50, 24, "Import", (0,191,255))

    Import = False
    while run:
        screen.blit(bg,(0,0))
        createbtn.Draw(screen)
        if Import:
            f_name.Draw(screen)
            read.Draw(screen)
        else:
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
                if importbtn.Click(pos):
                    Import = True

                if read.Click(pos) and Import:
                    if f_name != "":
                        circuit = Json.Read(f_name.GetText())
                        CircuitDes = Circuit()
                        CircuitDes.ReadComponents(circuit)
                        DesignWin()
                    else:
                        pass

                if f_name.Click(pos) and Import:
                    pass

            if event.type == pygame.KEYDOWN:
                if f_name.CheckSelected():
                    if event.key == pygame.K_BACKSPACE:
                        text = f_name.GetText()
                        new = text[:-1]
                        f_name.SetText(new)
                    elif event.key == pygame.K_RETURN:
                        f_name.SetSelected(False)
                    else:
                        text = f_name.GetText()
                        new = text + event.unicode
                        f_name.SetText(new)


def AddRes(graph):

    graph.AgregarVertice("Res1",10,10,False)

def AddPower(graph):

    graph.AgregarVertice("Power",10,10,True)

def Simulation():
    circuit = Circuit()
    simulation = SimWin()
    simulation.SetScreen(screen)
    simulation.SetComponents(circuit.GetNodes(), circuit.GetEdges(), circuit.GetPowers(), circuit.GetGraph(), circuit.GetComponentsType(), circuit.GetYellowEdges(),circuit.Getcomponents(),circuit.GetResNames(),circuit.GetResValues(),circuit.GetPowerNames(),circuit.GetPowerValues())
    simulation.RunWin()
    DesignWin()

def DesignWin():
    CircuitDes = Circuit()
    CircuitDes.RunWin(screen)
    Simulation()

if __name__ == '__main__':
    #Formulas1 = Formulas()
    Main_Win()


