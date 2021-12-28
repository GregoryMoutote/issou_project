import pygame
from Bottun.Bottun import *

class pictureBottun(bottun):

    def __init__(self, x, y, width, height, screen,picture):
        super().__init__(x,y,width,height,screen)
        picture = pygame.image.load("picture/interface/" + picture)
        self.Picture = pygame.transform.scale(picture, (width, height))
        self.showBotton()


    def showBotton(self):
        self.screen.blit(self.truePicture, (self.x, self.y))

