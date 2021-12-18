import pygame
from pygame.transform import smoothscale


class Botton:


    def __init__(self, x, y, width, height, screen,color, text, textSize, textLeftSpace, font,textColor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.text = text
        self.textSize = textSize
        self.textLeftSpace = textLeftSpace
        self.font = "font/" + font
        self.textColor = textColor
        self.color = color
        self.botton = pygame.Rect(self.x, self.y, self.width, self.height)
        self.showBotton()


    def showBotton(self):
        pygame.font.init()
        pygame.draw.rect(self.screen, self.color, self.botton)
        myfont = pygame.font.Font(self.font, self.textSize)
        textsurface = myfont.render(self.text, True, self.textColor)
        self.screen.blit(textsurface, (self.x+self.textLeftSpace, self.y+(self.height-self.textSize)/2))
        pygame.display.update()
        pygame.font.quit()

