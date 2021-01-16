from Button import Button
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

    # Components images
    node2 = pygame.image.load(r'Images\r_resistor.png')
    node2.set_colorkey([255, 255, 255])
    b_resistor = pygame.image.load(r'Images\resistor1.png')
    b_resistor.set_colorkey([255, 255, 255])

    power_supply1 = pygame.image.load(r'Images\powersupply.png')
    power_supply1.set_colorkey([255, 255, 255])
    y_power_supply = pygame.image.load(r'Images\y_powersupply.png')
    y_power_supply.set_colorkey([255, 255, 255])

    # Buttons images
    r_resistor = pygame.image.load(r'Images\r_resistor.png')
    r_resistor.set_colorkey([255, 255, 255])
    edge = pygame.image.load(r'Images\add_edges.png')
    edge_delete = pygame.image.load(r'Images\plus.png')
    power_supply = pygame.image.load(r'Images\power.png')
    power_supply.set_colorkey([255, 255, 255])

    nodes = []
    edges = []
    powers = []
    components = [node2, power_supply1, b_resistor, y_power_supply]
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
        print(self.edges)
        print(self.components_type)
        for i in range(len(self.edges)):

            if self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[0]:
                print('if 1')
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[self.edges[i][1]] == self.components[0]:
                print('if 2')
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),(self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[1]:
                print('if 3')
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

        for i in range(len(self.yellow_edges)):
            pygame.draw.line(self.screen, self.YELLOW,(self.nodes[self.yellow_edges[i][0]][0] + 16, self.nodes[self.yellow_edges[i][0]][1] + 16),(self.nodes[self.yellow_edges[i][1]][0] + 16, self.nodes[self.yellow_edges[i][1]][1] + 16),1)

    def SetScreen(self,sc):
        self.screen = sc

    def SetComponents(self,nodes, edges, powers, graph,components_type,yellow_edges):
        self.nodes = nodes
        self.edges = edges
        self.powers = powers
        self.graph = graph
        self.components_type = components_type
        self.yellow_edges = yellow_edges

    def RunWin(self):
        run = True
        # BOTON: color boton, posicion x, posicion y, ancho, altura, tamano de letra, texto, color texto
        edit_again = Button(self.LIME_GREEN,20,500,150,70,24,"Back to design",self.WHITE)
        while run:
            pygame.display.set_mode((800,600))
            self.screen.fill((255,255,255))
            edit_again.Draw(self.screen)

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

            self.show_edges()
            self.show_nodes()
            self.show_powers()
            pygame.display.update()
