import pygame
from pygame.transform import smoothscale


class cocheBotton:


    def __init__(self, x, y, radius, screen,color1,color2,actif):
        self.x = x
        self.y = y
        self.radius=radius
        self.screen = screen
        self.color1 = color1
        self.color2 = color2
        self.actif = actif
        self.showBotton()


    def showBotton(self):
        if self.actif:
            pygame.draw.circle(self.screen, self.color1, (self.x,self.y), self.radius)
        else:
            pygame.draw.circle(self.screen, self.color2, (self.x,self.y), self.radius)

        pygame.display.update()

    def changeStat(self):
        if self.actif:
            self.actif=False
        else:
            self.actif=True
        self.showBotton()

