#Circuit Design
from Simulation import SimWin
import pygame
import pygame as pg
import sys
import Grafo
import random


pygame.init()
clock = pygame.time.Clock()

class Circuit:

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    YELLOW = (255,255,0)
    BLUE = (0,0,255)

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Circuit Designer")
    left_background = pygame.image.load(r'Images\fondo1.jpg')

    color = (255, 255, 255)
    inputRectName = pygame.Rect(7,150,112,22)
    inputRectValue = pygame.Rect(7,200,82,22) 

    
    #Resistor positions images
    node2 = pygame.image.load(r'Images\resistorH.png')
    node2.set_colorkey([255,255,255])
    node3 = pygame.image.load(r'Images\resistorH.png')
    node3.set_colorkey([255,255,255])
    node4 = pygame.image.load(r'Images\resistorV.png')
    node4.set_colorkey([255,255,255])
    node5 = pygame.image.load(r'Images\resistorV.png')
    node5.set_colorkey([255,255,255])

    #Power supply positions images
    power_supply1 = pygame.image.load(r'Images\powersupplyV.png')
    power_supply1.set_colorkey([255,255,255])
    power_supply2 = pygame.image.load(r'Images\powersupplyH.png')
    power_supply2.set_colorkey([255,255,255])

    #Resistor positions images simulation
    b_resistor = pygame.image.load(r'Images\resistor_bH.png')
    b_resistor.set_colorkey([255,255,255])
    b_resistorV = pygame.image.load(r'Images\resistor_bV.png')
    b_resistorV.set_colorkey([255,255,255])

    #Power supply positions images simulation
    y_power_supply = pygame.image.load(r'Images\y_powersupplyV.png')
    y_power_supply.set_colorkey([255,255,255])
    y_power_supplyH = pygame.image.load(r'Images\y_powersupplyH.png')
    y_power_supplyH.set_colorkey([255,255,255])
    
    #Buttons images
    r_resistor = pygame.image.load(r'Images\r_resistor.png')
    r_resistor.set_colorkey([255,255,255])
    edge = pygame.image.load(r'Images\add_edges.png')
    edge_delete = pygame.image.load(r'Images\plus.png')
    power_supply = pygame.image.load(r'Images\power.png')
    power_supply.set_colorkey([255,255,255])
    cross = pygame.image.load(r'Images\cross.png')
    algo_button = pygame.image.load(r'Images\algo_button.png')
    add_button = pygame.image.load(r'Images\add_edges.png')
    button_font = pygame.font.Font('roboto.ttf', 20)
    msg_font = pygame.font.Font('roboto.ttf', 15)
    valuesFont = pygame.font.Font('roboto.ttf', 13)
    letterFont = pygame.font.Font(None,23)
    

    #Buttons states
    add_node = button_font.render('Add Resistor', True, BLACK)
    add_edge = button_font.render('Add Edges', True, BLACK)
    delete_edge = button_font.render('Delete Edges', True, BLACK)
    add_power_supply = button_font.render('Add power supply', True, BLACK)
    end_desing = button_font.render('End Desing', True, BLACK)
    simulation_button = button_font.render('Simulate', True, WHITE) 
    clear_button = button_font.render('Clear Screen', True, WHITE) 
    msg_box = msg_font.render('', True, BLUE)

    #Button creator
    node_button = r_resistor
    edge_button = edge
    edge_button_delete = edge_delete
    power_supply_button = power_supply

    #Resistors created
    resistorName = ''
    resistorValue = ''

    components_names = []
    components_values = []

    #Power supply created
    power_supplyName = ''
    power_supplyValue = ''

    power_supply_names = []
    power_supply_value = []

    #Nodes and components lists
    nodes = []
    edges= []
    powers = []
    components = [node2, power_supply1, b_resistor, y_power_supply, node3, node4, node5, power_supply2, b_resistorV, y_power_supplyH]
    components_type = []
    yellow_edges = []
    color_power_supply = [power_supply1]
    power_supply_color = []

    pos = (-1,-1)
    pointA = -1
    pointB = -1
    point = -1
    state = 'start'
    msg = ''

    graph = Grafo.Grafo()

    move = False

    #Components configuratios states
    nameRectStatus = False
    valueRectStatus = False
    __instance = None

    def __new__(cls):
        if Circuit.__instance is None:
            Circuit.__instance = object.__new__(cls)
        return Circuit.__instance

    def GetNodes(self):
        return self.nodes

    def GetEdges(self):
        return self.edges

    def GetPowers(self):
        return self.powers

    def GetComponentsType(self):
        return self.components_type

    def GetGraph(self):
        return self.graph

    def GetYellowEdges(self):
        return self.yellow_edges

    def Getcomponents(self):
        return self.components

    def GetCompsNames(self):
        return self.components_names

    def GetCompsValues(self):
        return self.components_values

    def GetPowerNames(self):
        return self.power_supply_names

    def GetPowerValues(self):
        return self.power_supply_value

    def ReadComponents(self,components):
        self.graph = components[0]
        self.nodes = components[1]
        self.edges = components[2]
        self.components_names = components[3]
        self.components_values = components[4]
        c_types = components[5]
        comps = []
        for c in c_types:
            if c == "power":
                comps.insert(0, self.components[1])
            else:
                comps.append(self.components[0])
        self.components_type = comps

    
    def isClicked(self,x1,y1,x2,y2,mos_x,mos_y):
        """Metodo para identificar cuando se hace click en los botones"""
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
        
    
    def ishovering(self,x1,y1,x2,y2):
        """Metodo para mostrar textos al pasar sobre botones"""
        mos_x, mos_y = pygame.mouse.get_pos()
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

    
    def simulation_mode(self,s,vis,adj):
        """Metodo de simulación"""
        vis[s] = 1
        if self.components_type[s] == self.components[1]:
            self.components_type[s] = self.components[3]
        else:
            if self.components_type[s] == self.components[0]:
                self.components_type[s] = self.components[2]
            
        self.show_edges()
        self.show_nodes()
        pygame.display.update()
        pygame.time.delay(200)
        for i in range(len(adj[s])):
            if vis[adj[s][i]] != 1:
                self.yellow_edges.append((s,adj[s][i]))
                self.yellow_edges.append((adj[s][i],s))
                self.show_edges()
                self.show_nodes()
                pygame.display.update()
                pygame.time.delay(400)
                self.simulation_mode(adj[s][i],vis,adj)

    def start_simulation_mode(self,point):
        if(len(self.nodes)==0 or len(self.edges)==0):
            return
        adj = [[] for i in range(len(self.nodes))]
        vis = [0 for i in range(len(self.nodes))]
        for i in range(len(self.edges)):
            adj[self.edges[i][0]].append(self.edges[i][1])
        self.simulation_mode(point,vis,adj)

    def make_equal(self, listA, listB):
        for i in range(len(listA)):
            listA[i] = listB[i]
    
    def getNode(self,mos_x,mos_y):
        """Metodo para obtener posiciones de los nodos"""
        for i in range(len(self.nodes)):
            self.x1 = self.nodes[i][0]
            self.y1 = self.nodes[i][1]
            if self.isClicked(self.x1, self.y1, self.x1 + self.node2.get_width(), self.y1 + self.node2.get_height(), mos_x, mos_y):
                return i
        return -1

    def show_nodes(self):
        """Muestra los nodos además de sus nombres y sus valores"""
        if(len(self.nodes)==0): return
        for i in range(len(self.nodes)):
            self.screen.blit(self.components_type[i],self.nodes[i])

        for i in range(len(self.components_names)):
            #Horizontal resistor
            if self.components_type[i] == self.components[0] or self.components_type[i] == self.components[4]:
                self.resistorV = self.valuesFont.render(self.components_values[i] +"\u03A9", False, (0,0,0))
                self.resistorN = self.valuesFont.render(self.components_names[i], False, (0,0,0))
                self.screen.blit(self.resistorN, (self.nodes[i][0],self.nodes[i][1]-20))
                self.screen.blit(self.resistorV,(self.nodes[i][0]+20,self.nodes[i][1]-20))
            #Vertical resistor
            elif self.components_type[i] == self.components[5] or self.components_type[i] == self.components[6]:
                self.resistorV = self.valuesFont.render(self.components_values[i] +"\u03A9", False, (0,0,0))
                self.resistorN = self.valuesFont.render(self.components_names[i], False, (0,0,0))
                self.screen.blit(self.resistorN, (self.nodes[i][0]+20,self.nodes[i][1]+20))
                self.screen.blit(self.resistorV,(self.nodes[i][0]+40,self.nodes[i][1]+20))
            #Vertical power supply
            elif self.components_type[i] == self.components[1]:
                self.powersupplyV = self.valuesFont.render(self.components_values[i] +"V", False, (0,0,0))
                self.powersupplyN = self.valuesFont.render(self.components_names[i], False, (0,0,0))
                self.screen.blit(self.powersupplyN, (self.nodes[i][0]-30,self.nodes[i][1]-20))
                self.screen.blit(self.powersupplyV, (self.nodes[i][0]-10,self.nodes[i][1]-20))
            '''
            #Horizontal power supply
            elif self.components_type[i] == self.components[1]:
                self.powersupplyV = self.valuesFont.render(self.components_values[i] +"V", False, (0,0,0))
                self.powersupplyN = self.valuesFont.render(self.components_names[i], False, (0,0,0))
                self.screen.blit(self.powersupplyN, (self.nodes[i][0],self.nodes[i][1]-20))
                self.screen.blit(self.powersupplyV, (self.nodes[i][0]+20,self.nodes[i][1]-20))
            '''

    def show_edges(self):

        """Muestra las aristas"""

        for i in range(len(self.edges)):

            if self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen,self.BLACK,(self.nodes[self.edges[i][0]][0]+50,self.nodes[self.edges[i][0]][1]+6),(self.nodes[self.edges[i][0]][0]+50,self.nodes[self.edges[i][1]][1]+6),1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]+50,self.nodes[self.edges[i][1]][1]+6),(self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0]+50 > self.nodes[self.edges[i][1]][0] and self.move:

                    i = self.getNode(self.nodes[self.edges[i][1]][0]+10, self.nodes[self.edges[i][1]][1]+5)
                    self.components_type[i] = self.components[4]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 100, self.nodes[self.edges[i][1]][1] + 6),(self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][1]][1] + 6), 1)

                if self.nodes[self.edges[i][0]][0]+50 < self.nodes[self.edges[i][1]][0] and self.move:

                    i = self.getNode(self.nodes[self.edges[i][1]][0]+10, self.nodes[self.edges[i][1]][1]+5)
                    self.components_type[i] = self.components[0]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]+6), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]+6),(self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] ), 1)

                if self.nodes[self.edges[i][0]][1]+50 > self.nodes[self.edges[i][1]][1]+50 and self.move:

                    i = self.getNode(self.nodes[self.edges[i][1]][0]+10, self.nodes[self.edges[i][1]][1]+5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0] + 50, self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]+6), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]+6),(self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1] +50 ), 1)

                if self.nodes[self.edges[i][0]][1]+50 < self.nodes[self.edges[i][1]][1]+50 and self.move:

                    i = self.getNode(self.nodes[self.edges[i][1]][0]+10, self.nodes[self.edges[i][1]][1]+5)
                    self.components_type[i] = self.components[5]

            elif self.components_type[self.edges[i][0]] == self.components[0] and self.components_type[self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]+50,self.nodes[self.edges[i][0]][1]+6),(self.nodes[self.edges[i][0]][0]+50,self.nodes[self.edges[i][1]][1]+55),1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]+50,self.nodes[self.edges[i][1]][1]+55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][1]][0]+20, self.nodes[self.edges[i][1]][1] + 55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][1]][0]+20, self.nodes[self.edges[i][1]][1] + 55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][0]][0]-50, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]-50, self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][0]][0]-50, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]-50, self.nodes[self.edges[i][1]][1] + 6),(self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)


            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),(self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][1]][1] + 6),(self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]), 1)

                if self.nodes[self.edges[i][0]][1]+50 > self.nodes[self.edges[i][1]][1]+50 and self.move:

                    i = self.getNode(self.nodes[self.edges[i][1]][0]+10, self.nodes[self.edges[i][1]][1]+5)
                    self.components_type[i] = self.components[6]

            elif self.components_type[self.edges[i][0]] == self.components[4] and self.components_type[self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0], self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][0]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0] + 6, self.nodes[self.edges[i][1]][1]+50), 1)

                if self.nodes[self.edges[i][0]][1]+50 < self.nodes[self.edges[i][1]][1]+50 and self.move:

                    i = self.getNode(self.nodes[self.edges[i][1]][0]+10, self.nodes[self.edges[i][1]][1]+5)
                    self.components_type[i] = self.components[5]


            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]+50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1]+6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][0]][1]+50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][1]][1]+6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][0]][1]+50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][0]][1]+50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][0]][1]+50),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][1]][1]+50), 1)


            elif self.components_type[self.edges[i][0]] == self.components[5] and self.components_type[self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]+50),(self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][1]][1] + 55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][1]][0]+20, self.nodes[self.edges[i][1]][1] + 55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)


            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1]+6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][1]][1]+6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][1]][1]+50), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][1]][0]+ 6, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[6] and self.components_type[self.edges[i][1]] == self.components[1]:

                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][0]][1]),(self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][0]][0]+ 6, self.nodes[self.edges[i][1]][1] + 55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 55), 1)
                pygame.draw.line(self.screen, self.BLACK,(self.nodes[self.edges[i][1]][0]+20, self.nodes[self.edges[i][1]][1] + 55),(self.nodes[self.edges[i][1]][0] + 20, self.nodes[self.edges[i][1]][1] + 38), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[self.edges[i][1]] == self.components[0]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0], self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[self.edges[i][1]] == self.components[4]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1] + 6),
                                 (self.nodes[self.edges[i][1]][0]+50, self.nodes[self.edges[i][1]][1] + 6), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[self.edges[i][1]] == self.components[5]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][1]][1]), 1)

            elif self.components_type[self.edges[i][0]] == self.components[1] and self.components_type[self.edges[i][1]] == self.components[6]:

                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][0]][1]),
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]+50), 1)
                pygame.draw.line(self.screen, self.BLACK,
                                 (self.nodes[self.edges[i][0]][0] + 20, self.nodes[self.edges[i][1]][1]+50),
                                 (self.nodes[self.edges[i][1]][0]+6, self.nodes[self.edges[i][1]][1]+50), 1)

        for i in range(len(self.yellow_edges)):
            pygame.draw.line(self.screen,self.YELLOW,(self.nodes[self.yellow_edges[i][0]][0]+16,self.nodes[self.yellow_edges[i][0]][1]+16),(self.nodes[self.yellow_edges[i][1]][0]+16,self.nodes[self.yellow_edges[i][1]][1]+16),1)

        self.move = False

    def show_buttons(self):
        """Muestra los botones en el modo 'start'"""
        if(self.state == 'start'):
            self.screen.blit(self.algo_button,(7,550))
            self.screen.blit(self.clear_button,(7+self.algo_button.get_width()/2-53,550+self.algo_button.get_height()/2-13))
            self.screen.blit(self.algo_button,(7,498))
            self.screen.blit(self.simulation_button,(7+self.algo_button.get_width()/2-20,498+self.algo_button.get_height()/2-13))
              
    def show_msg(self):
        """Muestra los mensajes en pantalla"""
        self.msg_box = self.msg_font.render(self.msg, True, self.BLUE)
        self.screen.blit(self.msg_box,(215,570))

    def SetComponents(self,nodes, edges, powers, graph,components_type,yellow_edges):
        self.nodes = nodes
        self.edges = edges
        self.powers = powers
        self.graph = graph
        self.components_type = components_type
        self.yellow_edges = yellow_edges

    def RunWin(self,sc):
        self.screen = sc
        running = True
        while running:
            
            #Muestra los botones dependiendo del modo
            self.screen.fill(self.WHITE)
            self.screen.blit(self.left_background,(0,0))

            if(self.state == 'start' or  self.state == 'exit'):
                self.screen.blit(self.node_button,(5,5)) and self.screen.blit(self.power_supply_button,(5,42)) and self.screen.blit(self.edge_button,(5,79)) and self.screen.blit(self.edge_button_delete,(5,116))

            if(self.state == 'add_node' or self.state == 'exit'):
                self.screen.blit(self.cross,(5,5)) and self.screen.blit(self.add_button,(5,250))

            if(self.state == 'add_power_supply' or self.state == 'exit'):
                self.screen.blit(self.cross,(5,5)) and self.screen.blit(self.add_button,(5,250))

            if(self.state == 'add_edge1' or self.state == 'add_edge2'):
                self.screen.blit(self.cross,(5,5))
            
            if(self.state == 'delete_edge1' or self.state == 'detele_edge2'):
                self.screen.blit(self.cross,(5,5))

            self.show_buttons()
            self.show_msg()
            
            #Start mode muestra muestra botones
            if self.state == 'start':
                self.node_button = self.r_resistor
                self.edge_button = self.edge
                self.edge_button_delete = self.edge_delete
                self.power_supply_button = self.power_supply
                if(self.ishovering(5,5,5+self.node_button.get_width(),5+self.node_button.get_height())):
                    self.screen.blit(self.add_node,(50,12))
                if(self.ishovering(5,42,5+self.power_supply_button.get_width(),42+self.power_supply_button.get_height())):
                    self.screen.blit(self.add_power_supply,(50,48))
                if(self.ishovering(5,79,5+self.edge_button.get_width(),79+self.edge_button.get_height())):
                    self.screen.blit(self.add_edge,(50,84))
                if(self.ishovering(5,116,5+self.edge_button_delete.get_width(),116+self.edge_button_delete.get_height())):
                    self.screen.blit(self.delete_edge,(50,120))
           
            #Resistor mode muestra muestra text box y botones
            if self.state == 'add_node':

                if(self.ishovering(5,5,5+self.cross.get_width(),42+self.cross.get_height())):
                    self.screen.blit(self.end_desing,(50,12))
                
                pygame.draw.rect(self.screen,self.color,self.inputRectName)
                self.textSurface = self.letterFont.render(self.resistorName,True,(0,0,0))
                self.screen.blit(self.textSurface,self.inputRectName)
                self.name_resistor = self.letterFont.render("Enter resistor name", True, (0,0,0))
                self.screen.blit(self.name_resistor,(7,120))

                pygame.draw.rect(self.screen,self.color,self.inputRectValue)
                self.textSurface2 = self.letterFont.render(self.resistorValue,True,(0,0,0))
                self.screen.blit(self.textSurface2,self.inputRectValue)
                self.value_resistor= self.letterFont.render(("Enter resistor value "+"(\u03A9)"), True, (0,0,0))
                self.screen.blit(self.value_resistor,(7,180))
            
            #Power supply mode muestra muestra text box y botones
            if self.state == 'add_power_supply':

                if(self.ishovering(5,5,5+self.cross.get_width(),42+self.cross.get_height())):
                    self.screen.blit(self.end_desing,(50,12))

                pygame.draw.rect(self.screen,self.color,self.inputRectName)
                self.textSurface = self.letterFont.render(self.power_supplyName,True,(0,0,0))
                self.screen.blit(self.textSurface,self.inputRectName)
                self.name_power_supply = self.letterFont.render("Enter power supply name", True, (0,0,0))
                self.screen.blit(self.name_power_supply,(7,120))

                pygame.draw.rect(self.screen,self.color,self.inputRectValue)
                self.textSurface2 = self.letterFont.render(self.power_supplyValue,True,(0,0,0))
                self.screen.blit(self.textSurface2,self.inputRectValue)
                self.letterFont = pygame.font.Font(None,21)
                self.value_power_supply= self.letterFont.render("Enter power supply name "+"(V)", True, (0,0,0))
                self.screen.blit(self.value_power_supply,(7,180))
            
            #Simulation mode
            if self.state == 'simulation_mode':
                self.temp_node = [self.components[0] for i in range(len(self.components_type))]
                self.make_equal(self.temp_node,self.components_type)
                self.start_simulation_mode(self.point)
                self.make_equal(self.components_type,self.temp_node)
                self.yellow_edges.clear()
                self.state = 'start'  
                self.point = -1

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if(pos[0]!=-1 & pos[1]!=-1):
                        
                        #Muestra botones y redirecciona a los diferentes modos
                        if self.state == 'start':
                            if(self.isClicked(5,5,5+self.node_button.get_width(),5+self.node_button.get_height(),pos[0],pos[1])):
                                self.state = 'add_node'
                                self.msg = 'Click on the screen to add a node or power there.'

                            elif(self.isClicked(5,42,5+self.power_supply_button.get_width(),42+self.power_supply_button.get_height(),pos[0],pos[1])):
                                self.state = 'add_power_supply'
                                self.msg = 'Click on the screen to add a power there.'

                            elif(self.isClicked(5,79,5+self.edge_button.get_width(),79+self.edge_button.get_height(),pos[0],pos[1])):
                                self.state = 'add_edge1'
                                self.msg = 'Choose initial vertex of the edge.'
                            
                            elif(self.isClicked(5,116,5+self.edge_button_delete.get_width(),116+self.edge_button_delete.get_height(),pos[0],pos[1])):
                                self.state = 'delete_edge1'
                                self.msg = 'Choose initial vertex of the edge.'
                            
                            elif(self.isClicked(7,498,7+self.algo_button.get_width(),498+self.algo_button.get_height(),pos[0],pos[1])):
                                if len(self.nodes) != 0:
                                    running = False
                                    self.state = 'start'
                                    return
                                    # simulation = SimWin()
                                    # simulation.SetScreen(self.screen)
                                    # simulation.SetComponents(self.nodes, self.edges, self.powers, self.graph,self.components_type,self.yellow_edges)
                                    # simulation.RunWin()
                                    # self.state = 'Simulation mode'
                                    # self.msg = 'Start circuit simulation mode'
                                else: self.state = 'start'

                            elif(self.isClicked(7,550,7+self.algo_button.get_width(),550+self.algo_button.get_height(),pos[0],pos[1])):
                                self.nodes.clear()
                                self.components_type.clear()
                                self.edges.clear()
                                self.powers.clear()
                                self.power_supply_color.clear()
                                
                        #Add resistor mode 
                        elif self.state == 'add_node':
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                            
                            if(self.isClicked(5,250,5+self.add_button.get_width(),250+self.add_button.get_height(),pos[0],pos[1])):
                                if self.resistorName == "" or self.resistorValue == "":
                                    print("Incomplete Information")

                                else:
                                    self.components_names.append(self.resistorName)
                                    self.components_values.append(self.resistorValue)


                                    self.resistorName = ""
                                    self.resistorValue = ""
                                    self.power_supplyName = ""
                                    self.power_supplyValue = ""

                                    self.nodes.append((250,250))
                                    self.components_type.append(self.components[0])

                                    self.graph.AgregarVertice(self.components_names[-1], int(self.components_values[-1]),
                                                              50, False, [250,250])
                        #Add power_supply mode           
                        elif self.state == 'add_power_supply':
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                            if(self.isClicked(5,250,5+self.add_button.get_width(),250+self.add_button.get_height(),pos[0],pos[1])):
                                if self.power_supplyName == "" or self.power_supplyValue == "":
                                    print("Incomplete Information")

                                else:
                                    self.components_names.insert(0, self.power_supplyName)
                                    self.components_values.insert(0, self.power_supplyValue)

                                                                        
                                    self.power_supplyName = ""
                                    self.power_supplyValue = ""
                                    self.resistorName = ""
                                    self.resistorValue = ""
                                    
                                    self.nodes.insert(0,(250,250))
                                    self.components_type.insert(0, self.components[1])

                                    self.graph.AgregarVertice(self.components_names[-1], int(self.components_values[-1]),
                                                              0, True, [250, 250])
                        #Add edges modes 
                        elif self.state == 'add_edge1':
                            self.pointA = self.getNode(pos[0],pos[1])
                            if(self.pointA != -1):
                                self.state = 'add_edge2'
                                self.msg = 'Choose terminal vertex of the edge.'
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                        #Add edges modes 
                        elif self.state == 'add_edge2':
                            self.pointB = self.getNode(pos[0],pos[1])
                            if self.pointB != -1 and self.pointB != self.pointA:
                                self.edges.append((self.pointA,self.pointB))

                                #self.edges.append((self.pointB,self.pointA))
                                self.graph.AgregarArista(self.pointA+1,self.pointB+1,0)
                                self.state = 'add_edge1'
                                self.msg = 'Choose initial vertex of the edge.'
                                self.pointA = -1
                                self.pointB = -1
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                        #Delete edges modes
                        elif self.state == 'delete_edge1':
                            self.pointA = self.getNode(pos[0],pos[1]) 
                            if(self.pointA != -1):
                                self.state = 'delete_edge2'
                                msg = 'Choose terminal vertex of the edge.'
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                        #Delete edges modes
                        elif self.state == 'delete_edge2':
                            self.pointB = self.getNode(pos[0],pos[1])
                            if self.pointB != -1 and self.pointB != self.pointA:
                                self.edges.remove((self.pointA,self.pointB))
                                #self.edges.remove((self.pointB,self.pointA))
                                self.graph.EliminarAristaEspecifica(self.pointA+1,self.pointB+1)
                                self.state = 'delete_edge1'
                                self.msg = 'Choose initial vertex of the edge.'
                                self.pointA = -1
                                self.pointB = -1
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                        #Simulation mode 
                        # elif self.state == 'Simulation mode':
                        #     self.point  = self.getNode(pos[0],pos[1])
                        #     self.state = 'simulation_mode'
                        #     self.msg = ''
                        #Exit mode      
                        elif self.state == 'exit':
                            if(self.isClicked(5,5,5+self.node_button.get_width(),5+self.node_button.get_height(),pos[0],pos[1])):
                                self.make_equal(self.components_type,self.temp_node)
                                self.yellow_edges.clear()
                                self.state = 'start'
                                self.msg = ''
                    self.pos = (-1,-1)

                if event.type == pygame.KEYDOWN:
                    if self.nameRectStatus == True:
                        if event.key == pygame.K_BACKSPACE:
                            self.resistorName = self.resistorName[0:-1]
                            self.power_supplyName = self.power_supplyName[0:-1]
                        else:    
                            self.resistorName += event.unicode
                            self.power_supplyName += event.unicode
                    if self.valueRectStatus == True:
                        if event.key == pygame.K_BACKSPACE:
                            self.resistorValue = self.resistorValue[0:-1]
                            self.power_supplyValue = self.power_supplyValue[0:-1]
                        else:    
                            self.resistorValue += event.unicode
                            self.power_supplyValue += event.unicode
                
                #Metodo para identificar text box de los valores 
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    PositionMenu = pygame.mouse.get_pos()

                    if self.inputRectName.collidepoint(event.pos):
                        self.nameRectStatus = True

                    if not self.inputRectName.collidepoint(event.pos):
                        self.nameRectStatus = False

                    if self.inputRectValue.collidepoint(event.pos):
                        self.valueRectStatus = True

                    if not self.inputRectValue.collidepoint(event.pos):
                        self.valueRectStatus = False

                    if PositionMenu[0]<20 and PositionMenu[1]<200:
                        resistorNameInfo = self.letterFont.render(self.resistorName, True, (0,0,0))
                        resistorValueInfo = self.letterFont.render(self.resistorValue, True, (0,0,0))
                        self.screen.blit(resistorNameInfo,(PositionMenu[0],PositionMenu[1]))
                        self.screen.blit(resistorValueInfo,(PositionMenu[0],PositionMenu[1]+20))

                        powerSupplyNameInfo = self.letterFont.render(self.power_supplyName, True, (0,0,0))
                        powerSupplyVlueInfo = self.letterFont.render(self.power_supplyValue, True, (0,0,0))
                        self.screen.blit(powerSupplyNameInfo,(PositionMenu[0],PositionMenu[1]))
                        self.screen.blit(powerSupplyVlueInfo,(PositionMenu[0],PositionMenu[1]+20))
                
                #Components movement
                if event.type == pg.MOUSEMOTION:
                    if event.buttons[0]:

                        self.move = True

                        i = self.getNode(pos[0],pos[1])

                        if i != -1:
                            tuple = self.nodes[i]

                            x = tuple[0] + event.rel[0]
                            y = tuple[1] + event.rel[1]

                            self.nodes[i] = (x,y)

                            self.graph.vertices[i+1].pos = [x,y]

                if pygame.mouse.get_pressed() == (0, 0, 1):

                    i = self.getNode(pos[0], pos[1])

                    if i != -1 and self.components_type[i] != self.components[1]:

                        if self.components_type[i] == self.components[0]:

                            self.components_type[i] = self.components[4]

                        elif self.components_type[i] == self.components[4]:

                            self.components_type[i] = self.components[5]

                        elif self.components_type[i] == self.components[5]:

                            self.components_type[i] = self.components[6]

                        elif self.components_type[i] == self.components[6]:

                            self.components_type[i] = self.components[0]


            self.show_edges()
            self.show_nodes()
            pygame.display.update()
            #self.clock.tick(60)
            
            
