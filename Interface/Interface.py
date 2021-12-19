import pygame
from abc import ABC, abstractmethod

class Interface(ABC):

    def __init__(self,screenData,screen):
        self.screen=screen
        self.screenData=screenData
        self.screenWidth=screenData.GetSystemMetrics(0)
        self.screenHeight=screenData.GetSystemMetrics(1)

    def updateInterface(self):
        pygame.display.update()