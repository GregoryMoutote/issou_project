import pygame
from Button.Button import *

class colorButton(Button):

    def __init__(self, x, y, width, height, screen,color, text, textSize, textLeftSpace, font,textColor):
        super().__init__(x,y,width,height,screen)
        self.text = text
        self.textSize = textSize
        self.textLeftSpace = textLeftSpace
        self.font = "./font/" + font
        self.textColor = textColor
        self.color = color
        self.showButton()


    def showButton(self):
        pygame.font.init()
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        myfont = pygame.font.Font(self.font, self.textSize)
        textsurface = myfont.render(self.text, True, self.textColor)
        pygame.font.quit()
        self.screen.blit(textsurface, (self.x+self.textLeftSpace, self.y+(self.height-self.textSize)/2))