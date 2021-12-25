from botton.CocheBotton import *

class multipleBotton:

    def __init__(self, x, y, width, height, screen,trueColor,falseColor,nbBotton,nbActif):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.nbBotton = nbBotton
        self.nbActif = nbActif
        self.trueColor = trueColor
        self.falseColor = falseColor
        self.coche=[]

        for i in range(0, self.nbBotton):
            if i <= self.nbActif:
                self.coche.append(cocheBotton(self.x +self.height/2+ i * self.width / (self.nbBotton+1), self.y + self.height/2, self.height/2,self.screen, self.trueColor, self.falseColor, True))
            else:
                self.coche.append(cocheBotton(self.x +self.height/2+ i * self.width / (self.nbBotton+1), self.y + self.height/2, self.height/2,self.screen, self.trueColor, self.falseColor, False))

        self.showBotton()

    def showBotton(self):
        for i in range(0, self.nbBotton):
             self.coche[i].showBotton()
        pygame.display.update()

    def changeStat(self,nbActif):
        self.nbActif=nbActif

        for i in range(0, self.nbBotton):
            if i <= self.nbActif:
                self.coche[i].setActif(True)
            else:
                self.coche[i].setActif(False)

        self.showBotton()