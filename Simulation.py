from Button import Button
from EntryBox import EntryBox
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

    nodes = []
    edges = []
    powers = []
    components = []
    components_type = []
    yellow_edges = []

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
            if self.isClicked(self.x1, self.y1, self.x1 + self.power1.get_width(), self.y1 + self.power1.get_height(),
                              mos_x, mos_y):
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

    def SetComponents(self,nodes, edges, powers, graph,components_type,yellow_edges,com):
        self.nodes = nodes
        self.edges = edges
        self.powers = powers
        self.graph = graph
        self.components_type = components_type
        self.yellow_edges = yellow_edges
        self.components = com
        print("Nodes")
        print(nodes)
        print("Edges")
        print(edges)
        print("Powers")
        print(powers)
        print("Components_type")
        print(components_type)
        print("Yellow edges")
        print(yellow_edges)

    def RunWin(self):
        print(str(self.graph.GetVertices()[1].GetT()))
        run = True
        # BOTON: color boton, posicion x, posicion y, ancho, altura, tamano de letra, texto, color texto
        edit_again = Button(self.LIME_GREEN,20,500,150,70,22,"Back to design",self.WHITE)
        export = Button(self.LIME_GREEN,620,500,150,70,24,"Export",self.WHITE)
        export2 = Button(self.LIME_GREEN, 630, 410, 120, 50, 24, "Cancel", self.WHITE)
        g_name = EntryBox("Introduce name:",600,490,40,180)
        save = Button(self.LIME_GREEN,630,540,120,50,24,"Save",self.WHITE)
        save_clicked = False
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

                    elif g_name.Click(pos):
                        pass

                    elif export.Click(pos):
                         save_clicked = True

                    elif export2.Click(pos):
                        save_clicked = False
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
