import pygame
from Buttons.Button import *
import time

class TimelineButton(Button):

    def __init__(self, x, y, width,height,screen,backPicture,frontPicture):
        super().__init__(x,y,width,height,screen)
        self.time=time.time()
        self.backPicture = pygame.image.load("picture/interface/" + backPicture)
        self.backPicture = pygame.transform.scale(self.backPicture, (self.width, self.height))
        self.frontPicture = pygame.image.load("picture/interface/" + frontPicture)
        self.frontScalePicture = pygame.transform.scale(self.frontPicture, (0, self.height))
        self.showButton()


    def showButton(self):
        self.screen.blit(self.backPicture, (self.x, self.y))
        self.screen.blit(self.frontScalePicture, (self.x, self.y))


    def changeStat(self,percent):
        self.frontScalePicture=pygame.transform.scale(self.frontPicture, (self.width*percent, self.height))
        self.showButton()