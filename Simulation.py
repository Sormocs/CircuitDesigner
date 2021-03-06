from Button import Button
from EntryBox import EntryBox
from QuickSort import SortDown
from ShellSort import SortUp
from Calculos import Formulas
import Json
import pygame
import sys
import Grafo

pygame.init()

class SimWin:
    """Clase SimWin que se crea para el modo simulacion"""

    LIME_GREEN = (50,205,50)
    WHITE = (255,255,255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUEITO = (0,255,255)

    node2 = pygame.image.load(r'Images\resistorH.png')
    
    valuesFont = pygame.font.Font('roboto.ttf', 13)
    font = pygame.font.SysFont("Comic Sans MS", 22)

    nodes = []
    edges = []
    powers = []
    components = []
    components_type = []
    yellow_edges = []

    resistors_names = []
    resistors_value = []

    total_val = 0
    total_i = 0

    #power_supply_names = []
    #power_supply_value = []

    sorted_names = []
    sorted_values = []

    selected_nodes = []

    node_val = 0
    node_name = ""
    node_current = 0
    v = ""
    edge = ""

    formulas = Formulas()

    path = []

    graph = None

    instance = None
    screen = None

    def __new__(cls):
        """Constructor para el singleton de la clase"""
        if SimWin.instance is None:
            SimWin.instance = object.__new__(cls)
        return SimWin.instance

    def show_nodes(self):
        """Muestra los nodos (resistencias)"""
        if (len(self.nodes) == 0): return
        for i in range(len(self.nodes)):
            self.screen.blit(self.components_type[i], self.nodes[i])
        for i in range(len(self.resistors_names)):
            #Horizontal resistor
            if self.components_type[i] == self.components[0] or self.components_type[i] == self.components[4]:
                self.resistorV = self.valuesFont.render(self.resistors_value[i] +"\u03A9", False, (0,0,0))
                self.resistorN = self.valuesFont.render(self.resistors_names[i], False, (0,0,0))
                self.screen.blit(self.resistorN, (self.nodes[i][0],self.nodes[i][1]-20))
                self.screen.blit(self.resistorV,(self.nodes[i][0]+20,self.nodes[i][1]-20))
            #Vertical resistor
            elif self.components_type[i] == self.components[5] or self.components_type[i] == self.components[6]:
                self.resistorV = self.valuesFont.render(self.resistors_value[i] +"\u03A9", False, (0,0,0))
                self.resistorN = self.valuesFont.render(self.resistors_names[i], False, (0,0,0))
                self.screen.blit(self.resistorN, (self.nodes[i][0]+20,self.nodes[i][1]+20))
                self.screen.blit(self.resistorV,(self.nodes[i][0]+40,self.nodes[i][1]+20))
            
            #Vertical power supply
            elif self.components_type[i] == self.components[1]:
                self.powersupplyV = self.valuesFont.render(self.resistors_value[i] +"V", False, (0,0,0))
                self.powersupplyN = self.valuesFont.render(self.resistors_names[i], False, (0,0,0))
                self.screen.blit(self.powersupplyN, (self.nodes[i][0]-30,self.nodes[i][1]-20))
                self.screen.blit(self.powersupplyV, (self.nodes[i][0]-10,self.nodes[i][1]-20))
            

    def getPowers(self, mos_x, mos_y):
        """Obtiene click en la fuente de poder"""
        for i in range(len(self.powers)):
            self.x1 = self.powers[i][0]
            self.y1 = self.powers[i][1]
            if self.isClicked(self.x1, self.y1, self.x1 + self.power1.get_width(), self.y1 + self.power1.get_height(),mos_x, mos_y):
                return i
        return -1

    def show_djs(self, listaCamino):
        """Dibuja las aristas del grafo para el camino con mayor o menor tension"""

        lista = listaCamino[0]

        recorrido = []

        for x in range(0, len(lista)):

            if x == len(lista)-1:

                break

            recorrido.append((lista[x], lista[x+1]))

        flag = self.edges

        self.edges = recorrido

        for i in range(len(recorrido)):


            if self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0] + 50 > self.nodes[self.edges[i][1]][0] and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[4]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0] + 50 < self.nodes[self.edges[i][1]][0] and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[0]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

                if self.nodes[self.edges[i][0]][1] + 50 > self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

                if self.nodes[self.edges[i][0]][1] + 50 < self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[5]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

                if self.nodes[self.edges[i][0]][1] + 50 > self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

                if self.nodes[self.edges[i][0]][1] + 50 < self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[5]

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUEITO,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)
        self.edges = flag

    def show_edges(self):
        """Dibuja las aristas del grafo"""
        for i in range(len(self.edges)):

            if self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0] + 50 > self.nodes[self.edges[i][1]][0] and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[4]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0] + 50 < self.nodes[self.edges[i][1]][0] and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[0]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

                if self.nodes[self.edges[i][0]][1] + 50 > self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

                if self.nodes[self.edges[i][0]][1] + 50 < self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[5]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            # arreglar
            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

                if self.nodes[self.edges[i][0]][1] + 50 > self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

                if self.nodes[self.edges[i][0]][1] + 50 < self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[5]

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLUE,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.RED,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]), 1)
                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 50), 1)
                pygame.draw.line(self.screen, self.GREEN,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

        for i in range(len(self.yellow_edges)):
            pygame.draw.line(self.screen, self.YELLOW,
                             (self.nodes[self.yellow_edges[i][0]][0] + 16, self.nodes[self.yellow_edges[i][0]][1] + 16),
                             (self.nodes[self.yellow_edges[i][1]][0] + 16, self.nodes[self.yellow_edges[i][1]][1] + 16),
                             1)

        self.move = False

    def SetScreen(self,sc):
        """Asigna el screen"""
        self.screen = sc

    def SetComponents(self,nodes, edges, powers, graph,components_type,yellow_edges,com,r_names,r_values,p_names,p_values):
        """Obtiene los componentes de archivo .json para asiganrlos directamente y rehacer un circuito guardado."""
        self.nodes = nodes
        self.edges = edges
        self.powers = powers
        self.graph = graph
        self.components_type = components_type
        self.yellow_edges = yellow_edges
        self.components = com
        self.resistors_names = r_names
        self.resistors_value = r_values

    def isClicked(self,x1,y1,x2,y2,mos_x,mos_y):
        """Verificar un click"""
        if mos_x>x1 and (mos_x<x2):
            x_inside = True
        else: x_inside = False
        if mos_y>y1 and (mos_y<y2):
            y_inside = True
        else: y_inside = False
        if x_inside and y_inside:
            return True
        else:
            return False

    def getNode(self,mos_x,mos_y):
        """Obtener la posicion de un nodo en un grafo"""
        for i in range(len(self.nodes)):
            self.x1 = self.nodes[i][0]
            self.y1 = self.nodes[i][1]
            if self.isClicked(self.x1, self.y1, self.x1 + self.node2.get_width(), self.y1 + self.node2.get_height(), mos_x, mos_y):
                return i
        return -1

    def ShowRes(self):
        """Muestra los valores de las listas formadas por los algoritmos de ordenamiento"""
        y = 45
        j = 0
        for i in self.sorted_values:
            text = self.sorted_names[j]+" "+str(i)
            stext = self.font.render(text,True,(0,0,0))
            self.screen.blit(stext,(20,y))
            y += 30
            j += 1

    def TotalValues(self):
        res = 0
        for n in self.resistors_value[1:]:
            num = int(n)
            res += num
        self.total_val = res
        self.total_i = self.formulas.CalcCorriente(self.resistors_value[0],res)

    def EdgeVal(self,i):
        """Metodo para obtener valor del voltaje de las aristas"""
        j=1
        res = self.formulas.CalcTension(self.total_i, self.resistors_value[i])
        while j < i:
            res += self.formulas.CalcTension(self.total_i, self.resistors_value[j])
            j+=1
        return float(self.resistors_value[0])-float(res)

    def RunWin(self):

        run = True
        self.TotalValues()
        # BOTON: color boton, posicion x, posicion y, ancho, altura, tamano de letra, texto, color texto
        show_up = Button(self.LIME_GREEN,20,40,155,70,21,"Show Hi-to-Low",self.WHITE)
        show_down = Button(self.LIME_GREEN,20,130,155,70,21,"Show Low-to-Hi",self.WHITE)
        edit_again = Button(self.LIME_GREEN,20,500,150,70,22,"Back to design",self.WHITE)
        export = Button(self.LIME_GREEN,620,500,150,70,24,"Export",self.WHITE)
        export2 = Button(self.LIME_GREEN, 630, 410, 120, 50, 24, "Cancel", self.WHITE)
        cancel_s = Button(self.LIME_GREEN, 35, 400, 120, 50, 24, "Close", self.WHITE)
        cancel_s2 = Button(self.LIME_GREEN, 35, 400, 120, 50, 24, "Close", self.WHITE)
        sel_nodes = Button(self.LIME_GREEN, 20, 250, 155, 70, 24, "Select Nodes", self.WHITE)
        g_name = EntryBox("Introduce name:",600,490,40,180)
        save = Button(self.LIME_GREEN,630,540,120,50,24,"Save",self.WHITE)
        res_title = self.font.render("Show resistors:",True,(0, 0, 0))
        path_title = self.font.render("Show path:", True, (0, 0, 0))
        save_clicked = False
        selection = True
        show = False
        showing = "NOTHING"
        while run:
            value = self.font.render("Value: " + str(self.node_val), True, (0, 0, 0))
            name = self.font.render("Name: " + self.node_name, True, (0, 0, 0))
            current = self.font.render("mA: " + str(self.node_current), True, (0, 0, 0))
            v = self.font.render("V: " + str(self.v), True, (0, 0, 0))
            edge = self.font.render("Edge: " + str(self.edge), True, (0, 0, 0))
            pygame.display.set_mode((800,600))
            self.screen.fill((255,255,255))
            edit_again.Draw(self.screen)
            self.show_edges()
            self.show_nodes()

            if save_clicked:
                g_name.Draw(self.screen)
                export2.Draw(self.screen)
                save.Draw(self.screen)

            else:
                export.Draw(self.screen)

            if showing == "RESISTORS":
                self.screen.blit(res_title, (20, 5))
                pygame.draw.rect(self.screen, self.LIME_GREEN, (620, 20, 160, 160))
                self.screen.blit(name, (622, 22))
                self.screen.blit(value, (622, 55))
                self.screen.blit(current, (622, 85))
                self.screen.blit(v, (622, 115))
                self.screen.blit(edge,(622,145))
                self.ShowRes()
                cancel_s.Draw(self.screen)
            elif showing == "PATH":
                if show:
                    self.show_djs(self.path)

                if len(self.selected_nodes) == 1:
                    text1 = self.font.render("Node 1: ", True, (0, 0, 0))
                    self.screen.blit(text1, (20, 50))
                elif len(self.selected_nodes) == 2:
                    text1 = self.font.render("Node 1: ", True, (0, 0, 0))
                    self.screen.blit(text1, (20, 50))
                    text1 = self.font.render("Node 2: ", True, (0, 0, 0))
                    self.screen.blit(text1, (20, 80))

                cancel_s2.Draw(self.screen)
            else:
                pygame.draw.rect(self.screen, self.LIME_GREEN, (620, 20, 160, 160))
                self.screen.blit(name, (622, 22))
                self.screen.blit(value, (622, 55))
                self.screen.blit(current, (622, 85))
                self.screen.blit(v,(622,115))
                self.screen.blit(edge, (622, 145))
                self.screen.blit(res_title,(20,5))
                self.screen.blit(path_title, (20, 210))
                show_up.Draw(self.screen)
                show_down.Draw(self.screen)
                sel_nodes.Draw(self.screen)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    i = 0
                    for n in self.nodes:
                        if n[0] <= pos[0] <= n[0]+50 and n[1] <= pos[1] <= n[1]+50:
                            self.node_name = self.resistors_names[i]
                            if n == self.nodes[0]:
                                self.node_val = str(self.resistors_value[i])+" V"
                                self.node_current = "NA"
                                self.v = "NA"
                                self.edge = self.resistors_value[0]
                            else:
                                self.node_val = str(self.resistors_value[i]) + " Ω"
                                self.v = str(self.formulas.CalcTension(self.total_i,self.resistors_value[i]))
                                self.node_current =self.total_i * 1000
                                self.edge = self.EdgeVal(i)
                        i += 1


                if event.type == pygame.MOUSEBUTTONUP:
                    if edit_again.Click(pos):
                        run = False
                        return

                    if g_name.Click(pos) and save_clicked:
                        pass

                    if export.Click(pos):
                         save_clicked = True

                    if export2.Click(pos) and save_clicked:
                        save_clicked = False

                    if save.Click(pos) and save_clicked:
                        fname = g_name.GetText()
                        if fname != "":
                            Json.Write(self.graph,self.nodes,self.edges,self.resistors_names,self.resistors_value,fname)
                        else:
                            pass
                    if show_down.Click(pos) and showing == "NOTHING":
                        showing = "RESISTORS"
                        show = SortDown(self.resistors_value[1:],self.resistors_names[1:])
                        self.sorted_values = show[0]
                        self.sorted_names = show[1]

                    if show_up.Click(pos) and showing == "NOTHING":
                        showing = "RESISTORS"
                        show = SortUp(self.resistors_value[1:],self.resistors_names[1:])
                        self.sorted_values = show[0]
                        self.sorted_names = show[1]

                    if sel_nodes.Click(pos) and showing == "NOTHING":
                        show = False
                        showing = "PATH"
                        selection = True

                    if selection:
                        for n in self.nodes:
                            if n[0] <= pos[0] <= n[0] + 50 and n[1] <= pos[1] <= n[1] + 50:
                                if len(self.selected_nodes) < 2:
                                    if n != []:
                                        self.selected_nodes.append(n)
                                        print(self.selected_nodes)
                                else:
                                    selection = False
                                    show = True
                                    print(show)
                                    ids = []
                                    for n in self.selected_nodes:
                                        id = self.getNode(n[0]+5, n[1]+5)
                                        if id != -1:
                                            ids += [id]
                                    print(ids)
                                    self.graph.DikjstraMinimo(ids[0])
                                    self.path = self.graph.Camino(ids[0], ids[1])
                                    print(self.path)


                    if cancel_s.Click(pos) and showing == "RESISTORS":
                        showing = "NOTHING"
                        self.sorted_values = []
                        self.sorted_names = []

                    if cancel_s2.Click(pos) and showing == "PATH":
                        show = False
                        selection = False
                        showing = "NOTHING"
                        self.selected_nodes = []

                    else:
                        pass

                if event.type == pygame.KEYDOWN:
                    if g_name.CheckSelected():
                        if event.key == pygame.K_BACKSPACE:
                            text = g_name.GetText()
                            new = text[:-1]
                            g_name.SetText(new)
                        elif event.key == pygame.K_RETURN:
                            g_name.SetSelected(False)
                        else:
                            text = g_name.GetText()
                            new = text + event.unicode
                            g_name.SetText(new)

            pygame.display.update()
