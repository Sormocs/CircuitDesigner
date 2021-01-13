#Circuit Design 
import pygame
import sys

pygame.init()
#clock = pygame.time.Clock()

class Circuit:

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    YELLOW = (255,255,0)
    BLUE = (0,0,255)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Circuit Designer")
    left_background = pygame.image.load(r'Images\fondo1.jpg')

    #Components images
    node2 = pygame.image.load(r'Images\resistor1.png')
    #node2.set_colorkey([255,255,255])
    power1 = pygame.image.load(r'Images\power.png')

    #Buttons images
    r_resistor = pygame.image.load(r'Images\r_resistor.png')
    r_resistor.set_colorkey([255,255,255])
    edge = pygame.image.load(r'Images\add_edges.png')
    power = pygame.image.load(r'Images\power.png')
    power.set_colorkey([255,255,255])
    cross = pygame.image.load(r'Images\cross.png')
    algo_button = pygame.image.load(r'Images\algo_button.png')
    button_font = pygame.font.Font('roboto.ttf', 20)
    msg_font = pygame.font.Font('roboto.ttf', 15)
    fuente2 = pygame.font.Font(None,25)

    #Buttons states
    add_node = button_font.render('Add Resistor', True, BLACK)
    add_edge = button_font.render('Add Edges', True, BLACK)
    add_power = button_font.render('Add Power', True, BLACK)
    end_desing = button_font.render('End Desing', True, BLACK)
    clear_button = button_font.render('Clear Screen', True, WHITE)
    msg_box = msg_font.render('', True, BLUE)

    #Button creator
    node_button = r_resistor
    edge_button = edge
    power_button = power
    nodes = []
    edges= []
    powers = []

    components = [node2, power1]
    components_type = []

    color_power = [power1]
    power_color = []

    pos = (-1,-1)
    pointA = -1
    pointB = -1
    point = -1
    state = 'start'
    msg = ''
    __instance = None

    def __new__(cls):
        if Circuit.__instance is None:
            Circuit.__instance = object.__new__(cls)
        return Circuit.__instance



    def isClicked(self,x1,y1,x2,y2,mos_x,mos_y):
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

    def getNode(self,mos_x,mos_y):
        for i in range(len(self.nodes)):
            self.x1 = self.nodes[i][0]
            self.y1 = self.nodes[i][1]
            if self.isClicked(self.x1, self.y1, self.x1 + self.node2.get_width(), self.y1 + self.node2.get_height(), mos_x, mos_y):
                return i
        return -1

    def show_nodes(self):
        if(len(self.nodes)==0): return
        for i in range(len(self.nodes)):
            self.screen.blit(self.components_type[i],self.nodes[i])

    def getPowers(self,mos_x,mos_y):
        for i in range(len(self.powers)):
            self.x1 = self.powers[i][0]
            self.y1 = self.powers[i][1]
            if self.isClicked(x1, y1, x1 + self.power1.get_width(), y1 + self.power1.get_height(), mos_x, mos_y):
                return i
        return -1

    def show_powers(self):
        if(len(self.powers)==0): return
        for i in range(len(self.powers)):
            self.screen.blit(self.power_color[i],self.powers[i])

    def show_edges(self):
        for i in range(len(self.edges)):
                pygame.draw.line(self.screen,self.BLACK,(self.nodes[self.edges[i][0]][0]+16,self.nodes[self.edges[i][0]][1]+16),(self.nodes[self.edges[i][1]][0]+16,self.nodes[self.edges[i][1]][1]+16),1)
                #pygame.draw.line(screen, BLACK, nodes, powers)

    def show_buttons(self):
        if(self.state == 'start'):
            self.screen.blit(self.algo_button,(7,550))
            self.screen.blit(self.clear_button,(7+self.algo_button.get_width()/2-53,550+self.algo_button.get_height()/2-13))

    def show_msg(self):
        self.msg_box = self.msg_font.render(self.msg, True, self.BLUE)
        self.screen.blit(self.msg_box,(215,570))

    def RunWin(self,sc):
        self.screen = sc
        print(self.screen)
        running = True
        while running:
            self.screen.fill(self.WHITE)
            self.screen.blit(self.left_background,(0,0))

            if(self.state == 'start' or  self.state == 'exit'):
                self.screen.blit(self.node_button,(5,5)) and self.screen.blit(self.power_button,(5,42)) and self.screen.blit(self.edge_button,(5,79))

            if(self.state == 'add_node' or self.state == 'exit'):
                self.screen.blit(self.cross,(5,5))

            if(self.state == 'add_power' or self.state == 'exit'):
                self.screen.blit(self.cross,(5,5))

            if(self.state == 'add_edge1' or self.state == 'add_edge2'):
                self.screen.blit(self.cross,(5,5))

            self.show_buttons()
            self.show_msg()

            if self.state == 'start':
                self.node_button = self.r_resistor
                self.edge_button = self.edge
                self.power_button = self.power
                if(self.ishovering(5,5,5+self.node_button.get_width(),5+self.node_button.get_height())):
                    self.screen.blit(self.add_node,(60,12))
                if(self.ishovering(5,42,5+self.power_button.get_width(),42+self.power_button.get_height())):
                    self.screen.blit(self.add_power,(60,48))
                if(self.ishovering(5,79,5+self.edge_button.get_width(),79+self.edge_button.get_height())):
                    self.screen.blit(self.add_edge,(60,84))

            if self.state == 'add_node':

                if(self.ishovering(5,5,5+self.cross.get_width(),42+self.cross.get_height())):
                    self.screen.blit(self.end_desing,(60,12))

                self.name_resistor = self.fuente2.render("Name:", True, (0,0,0))
                self.screen.blit(self.name_resistor,(7,150))

                self.value_resistor= self.fuente2.render("Value:", True, (0,0,0))
                self.screen.blit(self.value_resistor,(7,180))

            if self.state == 'add_power':

                if(self.ishovering(5,5,5+self.cross.get_width(),42+self.cross.get_height())):
                    self.screen.blit(self.end_desing,(60,12))

                self.name_power = self.fuente2.render("Name:", True, (0,0,0))
                self.screen.blit(self.name_power,(7,150))

                self.value_power= self.fuente2.render("Value:", True, (0,0,0))
                self.screen.blit(self.value_power,(7,180))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if(pos[0]!=-1 & pos[1]!=-1):
                        if self.state == 'start':
                            if(self.isClicked(5,5,5+self.node_button.get_width(),5+self.node_button.get_height(),pos[0],pos[1])):
                                self.state = 'add_node'
                                self.msg = 'Click on the screen to add a node or power there.'

                            elif(self.isClicked(5,42,5+self.power_button.get_width(),42+self.power_button.get_height(),pos[0],pos[1])):
                                self.state = 'add_power'
                                self.msg = 'Click on the screen to add a power there.'

                            elif(self.isClicked(5,79,5+self.edge_button.get_width(),79+self.edge_button.get_height(),pos[0],pos[1])):
                                self.state = 'add_edge1'
                                self.msg = 'Choose initial vertex of the edge.'



                            elif(self.isClicked(7,550,7+self.algo_button.get_width(),550+self.algo_button.get_height(),pos[0],pos[1])):
                                self.nodes.clear()
                                self.components_type.clear()
                                self.edges.clear()
                                self.powers.clear()
                                self.power_color.clear()

                        elif self.state == 'add_node':
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                            if pos[0]>200 and pos[1]<550:
                                self.nodes.append((pos[0]-16,pos[1]-16))
                                self.components_type.append(self.components[0])
                            #else:
                             #   nodes.append((pos[0]-16,pos[1]-16))
                              #  components_type.append(components[1])


                            #if pos[0]>200 and pos[0]<300:
                             #       powers.append((pos[0]-16,pos[1]-16))
                              #      power_color.append(color_power[0])

                        elif self.state == 'add_power':
                            if pos[0]>200 and pos[1]<550:
                                self.nodes.append((pos[0]-16,pos[1]-16))
                                self.components_type.append(self.components[1])
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''

                        elif self.state == 'add_edge1':
                            self.pointA = self.getNode(pos[0],pos[1])
                            if(self.pointA != -1):
                                self.state = 'add_edge2'
                                self.msg = 'Choose terminal vertex of the edge.'
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''


                        elif self.state == 'add_edge2':
                            self.pointB = self.getNode(pos[0],pos[1])
                            if self.pointB != -1 and self.pointB != self.pointA:
                                self.edges.append((self.pointA,self.pointB))
                                self.edges.append((self.pointB,self.pointA))
                                self.state = 'add_edge1'
                                self.msg = 'Choose initial vertex of the edge.'
                                self.pointA = -1
                                self.pointB = -1
                            if(self.isClicked(5,5,5+self.cross.get_width(),5+self.cross.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''

                        elif self.state == 'exit':
                            if(self.isClicked(5,5,5+self.node_button.get_width(),5+self.node_button.get_height(),pos[0],pos[1])):
                                self.state = 'start'
                                self.msg = ''
                    self.pos = (-1,-1)

            self.show_edges()
            self.show_nodes()
            self.show_powers()
            pygame.display.update()
            self.clock.tick(60)



