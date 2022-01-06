import pygame

class Target:

    def __init__(self, picture, x,y,radius,screen):
        self.x=x
        self.y=y
        self.radius=radius
        self.screen=screen
        self.picture=pygame.image.load("picture/cible/"+picture)
        self.picture=pygame.transform.scale(self.picture, (self.radius*2, self.radius*2))
        self.showTarget()

    def showTarget(self):
        self.screen.blit(self.picture, (self.x - self.radius, self.y - self.radius))



