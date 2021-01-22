import pygame

pygame.init()

class EntryBox:

    def __init__(self,text_above,xcord,ycord,box_height,box_width):

        self.box_xcord = xcord
        self.box_ycord = ycord
        self.box_height = box_height
        self.box_width = box_width
        self.text = ""
        self.font = pygame.font.SysFont("Comic Sans MS",28, bold=True,italic=True)
        self.font2 = pygame.font.SysFont("Comic Sans MS", 24, bold=True, italic=True)
        self.text_above = self.font2.render(text_above, True, (120, 255, 255))
        self.color_selected= (140,255,255)
        self.color_unselected = (160, 160, 160)
        self.color = self.color_unselected
        self.selected = False

    def Draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.box_xcord, self.box_ycord, self.box_width, self.box_height), 2)
        showtxt = self.font.render(self.text, True, (120, 255, 255))
        screen.blit(self.text_above, (self.box_xcord, self.box_ycord - 30))
        screen.blit(showtxt, (self.box_xcord + 5, self.box_ycord - 4))

    def Click(self,mpos):
        if self.box_xcord<mpos[0]<self.box_xcord + self.box_width and self.box_ycord<mpos[1]<self.box_ycord+self.box_height:
            self.selected = True
            self.color = self.color_selected
        else:
            self.color = self.color_unselected
            self.selected = False
            return False

    def CheckSelected(self):
        if self.selected:
            return True
        else:
            return False

    def SetSelected(self,selected):
        self.selected = selected

    def SetText(self,text):
        self.text = text

    def GetText(self):
        return self.text