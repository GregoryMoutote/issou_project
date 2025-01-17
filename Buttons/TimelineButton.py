import pygame
from Buttons.Button import *
import time

class TimelineButton(Button):

    def __init__(self, x, y, width, height, screen, back_picture, front_picture):
        super().__init__(x, y, width, height, screen)
        self.time = time.time()
        self.back_picture = pygame.image.load("Pictures/Interfaces/" + back_picture)
        self.back_picture = pygame.transform.scale(self.back_picture, (self.width, self.height))
        self.front_picture = pygame.image.load("Pictures/Interfaces/" + front_picture)
        self.front_scale_picture = pygame.transform.scale(self.front_picture, (0, self.height))
        self.percent = 0
        self.show_button()

    """
    affiche le bouton
    """
    def show_button(self):
        self.screen.blit(self.back_picture, (self.x, self.y))
        self.screen.blit(self.front_scale_picture, (self.x, self.y))

    """
    change la valeur de la time line
    """
    def change_stat(self, percent):
        print(percent)
        if percent <= 1:
            self.percent = percent
            self.front_scale_picture = pygame.transform.scale(self.front_picture,(self.width * percent, self.height))
            self.show_button()