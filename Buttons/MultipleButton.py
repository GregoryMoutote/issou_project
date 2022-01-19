from Buttons.CocheButton import *
from Buttons.Button import *

class multipleButton(Button):

    def __init__(self, x, y, width, height, screen,trueColor,falseColor,nbButton,nbActif):
        super().__init__(x,y,width,height,screen)
        self.nbButton = nbButton
        self.nbActif = nbActif
        self.trueColor = trueColor
        self.falseColor = falseColor
        self.coche=[]

        for i in range(0, self.nbButton):
            if i < self.nbActif:
                self.coche.append(cocheButton(self.x + i * self.width / (self.nbButton + 1), self.y, self.height, self.height, self.screen, self.trueColor, self.falseColor, True))
            else:
                self.coche.append(cocheButton(self.x + i * self.width / (self.nbButton + 1), self.y, self.height, self.height, self.screen, self.trueColor, self.falseColor, False))
        self.showButton()

    def showButton(self):
        for i in range(0, self.nbButton):
             self.coche[i].showButton()

    def changeStat(self,nbActif):
        self.nbActif=nbActif

        for i in range(0, self.nbButton):
            if i < self.nbActif:
                self.coche[i].actif=True
            else:
                self.coche[i].actif=False
        self.showButton()

    def __del__(self):
        self.coche.clear()