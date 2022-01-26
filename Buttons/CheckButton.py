import pygame
from Buttons.Button import *
import time

class CheckButton(Button):

    def __init__(self, x, y, width, height, screen, true_picture, false_picture, active):
        super().__init__(x, y, width, height, screen)
        self.time = time.time()
        self.picture = pygame.image.load("Pictures/Interfaces/" + true_picture)
        self.true_picture = pygame.transform.scale(self.picture, (self.width, self.height))
        self.picture2 = pygame.image.load("Pictures/Interfaces/" + false_picture)
        self.false_picture = pygame.transform.scale(self.picture2, (self.width, self.height))
        self.active = active
        self.show_button()

    def show_button(self):
        if self.active:
            self.screen.blit(self.true_picture, (self.x, self.y))
        else:
            self.screen.blit(self.false_picture, (self.x, self.y))


    def change_stat(self):
        if time.time() - self.time > 1:
            self.time = time.time()
            if self.active:
                self.active = False
                self.show_button()
                return False
            else:
                self.active = True
                self.show_button()
                return True
