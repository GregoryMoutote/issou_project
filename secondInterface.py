from Interface import *
from target import *
import pygame
from math import *

class SecondInterface (Interface):


    def __init__(self,screenData,screen):
        super().__init__(screenData,screen)
        background = pygame.image.load("picture/fond.png")
        screen.blit(background, (0, 0))
        self.cible=[Target("rondBleu.png",500,400,100,screen)]
        self.cible.append(Target("rondVert.png",100,0,300,screen))
        self.targetInt()

    def targetInt(self):
        continuer=True
        while continuer:
            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for c in self.cible:
                        if self.toucheCible(c.x, c.y, c.radius, x, y):
                            print("fin")
                            continuer=False
            pygame.display.update()

    def toucheCible(self,left, top, radius, x, y):

        if (x > left - radius and x < left + radius):
            hypotenuse = (radius) ** 2
            adjacent = (left - x) ** 2
            if (adjacent <= hypotenuse):
                axeY = sqrt(hypotenuse - adjacent)

                if (y > top - axeY and y < top + axeY):
                    return True

        return False


