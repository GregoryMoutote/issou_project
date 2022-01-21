import pygame
from Buttons.Button import *
import time

class TimelineButton(Button):

    def __init__(self, x, y, width,height,screen,backPicture,frontPicture):
        super().__init__(x,y,width,height,screen)
        self.time=time.time()
        self.backPicture = pygame.image.load("Pictures/Interfaces/" + backPicture)
        self.backPicture = pygame.transform.scale(self.backPicture, (self.width, self.height))
        self.frontPicture = pygame.image.load("Pictures/Interfaces/" + frontPicture)
        self.frontScalePicture = pygame.transform.scale(self.frontPicture, (0, self.height))
        self.percent=0
        self.showButton()


    def showButton(self):
        self.screen.blit(self.backPicture, (self.x, self.y))
        self.screen.blit(self.frontScalePicture, (self.x, self.y))


    def changeStat(self,percent):
        if percent<=100:
            self.percent=percent
            self.frontScalePicture=pygame.transform.scale(self.frontPicture, (self.width*percent/100, self.height))
            self.showButton()