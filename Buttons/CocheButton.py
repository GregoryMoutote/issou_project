import pygame
from Buttons.Button import *
import time

class CocheButton(Button):

    def __init__(self, x, y, width,height, screen,truePicture,falsePicture,actif):
        super().__init__(x,y,width,height,screen)
        self.time=time.time()
        self.picture = pygame.image.load("picture/interface/" + truePicture)
        self.truePicture = pygame.transform.scale(self.picture, (self.width, self.height))
        self.picture2 = pygame.image.load("picture/interface/" + falsePicture)
        self.falsePicture = pygame.transform.scale(self.picture2, (self.width, self.height))
        self.actif = actif
        self.showButton()

    def showButton(self):
        if self.actif:
            #pygame.draw.circle(self.screen, self.trueColor, (self.x,self.y), self.radius)
            self.screen.blit(self.truePicture, (self.x, self.y))
        else:
            #pygame.draw.circle(self.screen, self.falseColor, (self.x,self.y), self.radius)
            self.screen.blit(self.falsePicture, (self.x, self.y))


    def changeStat(self):
        if(time.time()-self.time>1):
            self.time=time.time()
            if self.actif:
                self.actif=False
                self.showButton()
                return False
            else:
                self.actif=True
                self.showButton()
                return True
