import pygame

class Button():
    def __init__(self, color, posx, posy, width, height, fsize, text, tcolor):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.text = text
        self.fontsize = fsize
        self.text_color = tcolor

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.posx, self.posy, self.width, self.height), 0)
        font = pygame.font.SysFont("Comic Sans MS", self.fontsize)
        text = font.render(self.text, 1, self.text_color)
        screen.blit(text, (self.posx + (self.width // 2 - text.get_width() // 2),
                           self.posy + (self.height // 2 - text.get_height() // 2)))  #

    def Click(self, mpos):
        if self.posx < mpos[0] < self.posx + self.width and self.posy < mpos[1] < self.posy + self.height:
            return True
        else:
            return False

    def MouseOver(self, mpos):
        if self.posx < mpos[0] < self.posx + self.width and self.posy < mpos[1] < self.posy + self.height:
            return True
        else:
            return False

    def SetColor(self, color, tcolor):
        self.color = color
        self.text_color = tcolor

    def SetText(self, text):
        self.text = text