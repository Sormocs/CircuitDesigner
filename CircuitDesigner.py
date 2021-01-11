#Circuit Design 
import pygame

clock = pygame.time.Clock()
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

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
msg_box = msg_font.render('', True, BLUE);

#Button creator
node_button = r_resistor
edge_button = edge
power_button = power
nodes = []
edges= []
powers = []
color = [node2]
node_color = []

color_power = [power1]
power_color = []

pos = (-1,-1)
pointA = -1
pointB = -1
point = -1
state = 'start'
msg = ''


def isClicked(x1,y1,x2,y2,mos_x,mos_y):
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

def ishovering(x1,y1,x2,y2):
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

def getNode(mos_x,mos_y):
    for i in range(len(nodes)):
        x1 = nodes[i][0]
        y1 = nodes[i][1]
        if isClicked(x1, y1, x1 + node2.get_width(), y1 + node2.get_height(), mos_x, mos_y):
            return i
    return -1

def show_nodes():
    if(len(nodes)==0): return
    for i in range(len(nodes)):
        screen.blit(node_color[i],nodes[i])

def getPowers(mos_x,mos_y):
    for i in range(len(powers)):
        x1 = powers[i][0]
        y1 = powers[i][1]
        if isClicked(x1, y1, x1 + power1.get_width(), y1 + power1.get_height(), mos_x, mos_y):
            return i
    return -1

def show_powers():
    if(len(powers)==0): return
    for i in range(len(powers)):
        screen.blit(power_color[i],powers[i])

def show_edges():
    for i in range(len(edges)):
            pygame.draw.line(screen,BLACK,(powers[edges[i][0]][0]+16,powers[edges[i][0]][1]+16),(powers[edges[i][1]][0]+16,powers[edges[i][1]][1]+16),1)
            #pygame.draw.line(screen, BLACK, nodes, powers)
            
def show_buttons():
    if(state == 'start'):
        screen.blit(algo_button,(7,550))
        screen.blit(clear_button,(7+algo_button.get_width()/2-53,550+algo_button.get_height()/2-13))
        
def show_msg():
    msg_box = msg_font.render(msg, True, BLUE);
    screen.blit(msg_box,(215,570))
    
running = True

while running:
    screen.fill(WHITE)
    screen.blit(left_background,(0,0))
    
    if(state == 'start' or  state == 'exit'):
        screen.blit(node_button,(5,5)) and screen.blit(power_button,(5,42)) and screen.blit(edge_button,(5,79))

    if(state == 'add_node' or state == 'exit'):
        screen.blit(cross,(5,5))
    
    if(state == 'add_power' or state == 'exit'):
        screen.blit(cross,(5,5))

    if(state == 'add_edge1' or state == 'add_edge2'):
        screen.blit(cross,(5,5))
     
    show_buttons()
    show_msg()
    
    if state == 'start':
        node_button = r_resistor
        edge_button = edge
        power_button = power
        if(ishovering(5,5,5+node_button.get_width(),5+node_button.get_height())):
            screen.blit(add_node,(60,12))
        if(ishovering(5,42,5+power_button.get_width(),42+power_button.get_height())):
            screen.blit(add_power,(60,48))
        if(ishovering(5,79,5+edge_button.get_width(),79+edge_button.get_height())):
            screen.blit(add_edge,(60,84))    

    if state == 'add_node':

        if(ishovering(5,5,5+cross.get_width(),42+cross.get_height())):
            screen.blit(end_desing,(60,12))

        name_resistor = fuente2.render("Name:", True, (0,0,0))
        screen.blit(name_resistor,(7,150))

        value_resistor= fuente2.render("Value:", True, (0,0,0))
        screen.blit(value_resistor,(7,180))

    if state == 'add_power':

        if(ishovering(5,5,5+cross.get_width(),42+cross.get_height())):
            screen.blit(end_desing,(60,12))
        
        name_power = fuente2.render("Name:", True, (0,0,0))
        screen.blit(name_power,(7,150))

        value_power= fuente2.render("Value:", True, (0,0,0))
        screen.blit(value_power,(7,180))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break;
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if(pos[0]!=-1 & pos[1]!=-1):
                if state == 'start':
                    if(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                        state = 'add_node'
                        msg = 'Click on the screen to add a node there.'

                    elif(isClicked(5,42,5+power_button.get_width(),42+power_button.get_height(),pos[0],pos[1])):
                        state = 'add_power'
                        msg = 'Click on the screen to add a power there.'
                    
                    elif(isClicked(5,79,5+edge_button.get_width(),79+edge_button.get_height(),pos[0],pos[1])):
                        state = 'add_edge1'
                        msg = 'Choose initial vertex of the edge.'
                        
            
                    elif(isClicked(7,550,7+algo_button.get_width(),550+algo_button.get_height(),pos[0],pos[1])):
                        nodes.clear()
                        node_color.clear()
                        edges.clear()
                        powers.clear()
                        power_color.clear()

                elif state == 'add_node':
                    if pos[0]>200 and pos[1]<550:
                        nodes.append((pos[0]-16,pos[1]-16))
                        node_color.append(color[0]) 

                    if(isClicked(5,5,5+cross.get_width(),5+cross.get_height(),pos[0],pos[1])):
                        state = 'start'
                        msg = ''
                    
                    #if pos[0]>200 and pos[0]<300:
                     #       powers.append((pos[0]-16,pos[1]-16))
                      #      power_color.append(color_power[0])
                           
                elif state == 'add_power':  
                    if pos[0]>200 and pos[1]<550:
                        powers.append((pos[0]-16,pos[1]-16))
                        power_color.append(color_power[0])
                    if(isClicked(5,5,5+cross.get_width(),5+cross.get_height(),pos[0],pos[1])):
                        state = 'start'
                        msg = ''
  
                elif state == 'add_edge1':
                    pointA = getPowers(pos[0],pos[1]) 
                    if(pointA != -1):
                        state = 'add_edge2'
                        msg = 'Choose terminal vertex of the edge.'
                    if(isClicked(5,5,5+cross.get_width(),5+cross.get_height(),pos[0],pos[1])):
                        state = 'start'
                        msg = ''


                elif state == 'add_edge2':
                    pointB = getPowers(pos[0],pos[1])
                    if pointB != -1 and pointB != pointA:
                        edges.append((pointA,pointB))
                        edges.append((pointB,pointA))
                        state = 'add_edge1'
                        msg = 'Choose initial vertex of the edge.'
                        pointA = -1
                        pointB = -1
                    if(isClicked(5,5,5+cross.get_width(),5+cross.get_height(),pos[0],pos[1])):
                        state = 'start'
                        msg = ''

                elif state == 'exit':
                    if(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])): 
                        state = 'start'
                        msg = ''
            pos = (-1,-1)
            
    show_edges()
    show_nodes()
    show_powers()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
