import pygame

class cocheBottun:

    def __init__(self, x, y, radius, screen,truePicture,falsePicture,actif):
        self.x = x
        self.y = y
        self.radius=radius
        self.screen = screen

        self.picture = pygame.image.load("picture/interface/" + truePicture)
        self.truePicture = pygame.transform.scale(self.picture, (self.radius * 2, self.radius * 2))
        self.picture2 = pygame.image.load("picture/interface/" + falsePicture)
        self.falsePicture = pygame.transform.scale(self.picture2, (self.radius * 2, self.radius * 2))

        self.actif = actif
        self.showBotton()

    def showBotton(self):
        if self.actif:
            #pygame.draw.circle(self.screen, self.trueColor, (self.x,self.y), self.radius)
            self.screen.blit(self.truePicture, (self.x - self.radius, self.y - self.radius))
        else:
            #pygame.draw.circle(self.screen, self.falseColor, (self.x,self.y), self.radius)
            self.screen.blit(self.falsePicture, (self.x - self.radius, self.y - self.radius))

        pygame.display.update()

    def changeStat(self):
        if self.actif:
            self.actif=False
            self.showBotton()
            return False
        else:
            self.actif=True
            self.showBotton()
            return True
