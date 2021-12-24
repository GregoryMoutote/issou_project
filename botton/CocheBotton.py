import pygame

class cocheBotton:

    def __init__(self, x, y, radius, screen,trueColor,falseColor,actif):
        self.x = x
        self.y = y
        self.radius=radius
        self.screen = screen
        self.trueColor = trueColor
        self.falseColor = falseColor
        self.actif = actif
        self.showBotton()


    def showBotton(self):
        if self.actif:
            pygame.draw.circle(self.screen, self.trueColor, (self.x,self.y), self.radius)
        else:
            pygame.draw.circle(self.screen, self.falseColor, (self.x,self.y), self.radius)

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

