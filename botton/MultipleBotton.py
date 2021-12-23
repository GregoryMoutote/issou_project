import pygame
from botton.CocheBotton import *

class multipleBotton:

    def __init__(self, x, y, width, height, screen,color1,color2,nbBotton,nbActif):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.nbBotton = nbBotton
        self.nbActif = nbActif
        self.color1 = color1
        self.color2 = color2
        self.coche=[]
        self.showBotton()

    def showBotton(self):
        for i in range(0, self.nbBotton):
            if i < self.nbActif:
                self.coche.append(cocheBotton(self.x +self.height/2+ i * self.width / (self.nbBotton+1), self.y + self.height/2, self.height/2,self.screen, self.color1, self.color2, True))
            else:
                self.coche.append(cocheBotton(self.x +self.height/2+ i * self.width / (self.nbBotton+1), self.y + self.height/2, self.height/2,self.screen, self.color1, self.color2, False))
        pygame.display.update()

    def changeStat(self,nbActif):
        self.nbActif=nbActif
        self.showBotton()