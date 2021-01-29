from Button import Button
from EntryBox import EntryBox
from QuickSort import SortDown
from ShellSort import SortUp
import Json
import pygame
import sys
import Grafo

pygame.init()

class SimWin:

    LIME_GREEN = (50,205,50)
    WHITE = (255,255,255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)

    font = pygame.font.SysFont("Comic Sans MS", 22)

    nodes = []
    edges = []
    powers = []
    components = []
    components_type = []
    yellow_edges = []

    resistors_names = []
    resistors_value = []

    #power_supply_names = []
    #power_supply_value = []

    sorted_names = []
    sorted_values = []

    graph = None

    instance = None
    screen = None

    def __new__(cls):
        if SimWin.instance is None:
            SimWin.instance = object.__new__(cls)
        return SimWin.instance

    def show_nodes(self):
        if (len(self.nodes) == 0): return
        for i in range(len(self.nodes)):
            self.screen.blit(self.components_type[i], self.nodes[i])

    def getPowers(self, mos_x, mos_y):
        for i in range(len(self.powers)):
            self.x1 = self.powers[i][0]
            self.y1 = self.powers[i][1]
            if self.isClicked(self.x1, self.y1, self.x1 + self.power1.get_width(), self.y1 + self.power1.get_height(),mos_x, mos_y):
                return i
        return -1

    def show_powers(self):
        if (len(self.powers) == 0): return
        for i in range(len(self.powers)):
            self.screen.blit(self.power_supply_color[i], self.powers[i])

    def show_edges(self):

        for i in range(len(self.edges)):

            if self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0] + 50 > self.nodes[self.edges[i][1]][0] and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[4]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0] + 50 < self.nodes[self.edges[i][1]][0] and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[0]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

                if self.nodes[self.edges[i][0]][1] + 50 > self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

                if self.nodes[self.edges[i][0]][1] + 50 < self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[5]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] - 50, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)


            # arreglar
            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

                if self.nodes[self.edges[i][0]][1] + 50 > self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

                if self.nodes[self.edges[i][0]][1] + 50 < self.nodes[self.edges[i][1]][1] + 50 and self.move:
                    i = self.getNode(self.nodes[self.edges[i][1]][0] + 10, self.nodes[self.edges[i][1]][1] + 5)
                    self.components_type[i] = self.components[5]


            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)


            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1] + 50),
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)


            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[
                self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 6, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55),
                                 (self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[
                self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 50),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] + 50), 1)

        for i in range(len(self.yellow_edges)):
            pygame.draw.line(self.screen, self.YELLOW,
                             (self.nodes[self.yellow_edges[i][0]][0] + 16, self.nodes[self.yellow_edges[i][0]][1] + 16),
                             (self.nodes[self.yellow_edges[i][1]][0] + 16, self.nodes[self.yellow_edges[i][1]][1] + 16),
                             1)

        self.move = False

    def SetScreen(self,sc):
        self.screen = sc

    def SetComponents(self,nodes, edges, powers, graph,components_type,yellow_edges,com,r_names,r_values,p_names,p_values):
        self.nodes = nodes
        self.edges = edges
        self.powers = powers
        self.graph = graph
        self.components_type = components_type
        self.yellow_edges = yellow_edges
        self.components = com
        self.resistors_names = r_names
        self.resistors_value = r_values

    def ShowRes(self):
        y = 45
        j = 0
        for i in self.sorted_values:
            text = self.sorted_names[j]+" "+str(i)
            stext = self.font.render(text,True,(0,0,0))
            self.screen.blit(stext,(20,y))
            y += 30
            j += 1

    def RunWin(self):
        print(str(self.graph.GetVertices()[1].GetT()))
        run = True
        # BOTON: color boton, posicion x, posicion y, ancho, altura, tamano de letra, texto, color texto
        show_up = Button(self.LIME_GREEN,20,40,155,70,21,"Show Hi-to-Low",self.WHITE)
        show_down = Button(self.LIME_GREEN,20,130,155,70,21,"Show Low-to-Hi",self.WHITE)
        edit_again = Button(self.LIME_GREEN,20,500,155,70,22,"Back to design",self.WHITE)
        export = Button(self.LIME_GREEN,620,500,150,70,24,"Export",self.WHITE)
        export2 = Button(self.LIME_GREEN, 630, 410, 120, 50, 24, "Cancel", self.WHITE)
        cancel_s = Button(self.LIME_GREEN, 35, 400, 120, 50, 24, "Close", self.WHITE)
        sel_nodes = Button(self.LIME_GREEN, 20, 250, 155, 70, 24, "Select Nodes", self.WHITE)
        g_name = EntryBox("Introduce name:",600,490,40,180)
        save = Button(self.LIME_GREEN,630,540,120,50,24,"Save",self.WHITE)
        res_title = self.font.render("Show resistors:",True,(0, 0, 0))
        path_title = self.font.render("Show path:", True, (0, 0, 0))
        save_clicked = False
        showing = "NOTHING"
        while run:
            pygame.display.set_mode((800,600))
            self.screen.fill((255,255,255))
            edit_again.Draw(self.screen)

            if save_clicked:
                g_name.Draw(self.screen)
                export2.Draw(self.screen)
                save.Draw(self.screen)

            else:
                export.Draw(self.screen)

            if showing == "RESISTORS":
                self.screen.blit(res_title, (20, 5))
                pygame.draw.rect(self.screen, self.LIME_GREEN, (640, 20, 130, 100))
                self.ShowRes()
                cancel_s.Draw(self.screen)
            elif showing == "PATH":
                pass
            else:
                pygame.draw.rect(self.screen, self.LIME_GREEN, (640, 20, 130, 100))
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

                if event.type == pygame.MOUSEBUTTONUP:
                    if edit_again.Click(pos):
                        run = False
                        return

                    elif g_name.Click(pos) and save_clicked:
                        pass

                    elif export.Click(pos):
                         save_clicked = True

                    elif export2.Click(pos) and save_clicked:
                        save_clicked = False

                    elif save.Click(pos) and save_clicked:
                        fname = g_name.GetText()
                        if fname != "":
                            Json.Write(self.graph,self.nodes,self.edges,self.resistors_names,self.resistors_value,fname)
                        else:
                            pass
                    elif show_down.Click(pos) and showing == "NOTHING":
                        showing = "RESISTORS"
                        show = SortDown(self.resistors_value[1:],self.resistors_names[1:])
                        self.sorted_values = show[0]
                        self.sorted_names = show[1]

                    elif show_up.Click(pos) and showing == "NOTHING":
                        showing = "RESISTORS"
                        show = SortUp(self.resistors_value[1:],self.resistors_names[1:])
                        self.sorted_values = show[0]
                        self.sorted_names = show[1]

                    elif cancel_s.Click(pos) and showing == "RESISTORS":
                        showing = "NOTHING"
                        self.sorted_values = []
                        self.sorted_names = []

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


            self.show_edges()
            self.show_nodes()
            self.show_powers()
            pygame.display.update()
