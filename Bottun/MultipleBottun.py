from Bottun.CocheBottun import *
from Bottun.Bottun import *

class multipleBottun(bottun):

    def __init__(self, x, y, width, height, screen,trueColor,falseColor,nbBottun,nbActif):
        super().__init__(x,y,width,height,screen)
        self.nbBottun = nbBottun
        self.nbActif = nbActif
        self.trueColor = trueColor
        self.falseColor = falseColor
        self.coche=[]

        for i in range(0, self.nbBottun):
            if i < self.nbActif:
                self.coche.append(cocheBottun(self.x +self.height/2+ i * self.width / (self.nbBottun+1), self.y,self.height, self.height,self.screen, self.trueColor, self.falseColor, True))
            else:
                self.coche.append(cocheBottun(self.x +self.height/2+ i * self.width / (self.nbBottun+1), self.y,self.height, self.height,self.screen, self.trueColor, self.falseColor, False))

        self.showBottun()

    def showBottun(self):
        for i in range(0, self.nbBottun):
             self.coche[i].showBottun()
        pygame.display.update()

    def changeStat(self,nbActif):
        self.nbActif=nbActif

        for i in range(0, self.nbBottun):
            if i < self.nbActif:
                self.coche[i].actif=True
            else:
                self.coche[i].actif=False

        self.showBottun()

    def __del__(self):
        self.coche.clear()