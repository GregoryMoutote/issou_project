import pygame.draw

from Interface.Interface import *
from botton.BooleanBotton import *
from botton.NavigationBotton import *


class InterfaceSettings(Interface):

    def __init__(self,detection,screendata,screen):
        print("paramètre")
        self.detection=detection
        self.detection.initHandCapture()
        self.screenData=screendata
        self.screen=screen

        super().__init__(self.screenData, self.screen)
        self.fondLogo=pygame.image.load("./picture/fondLogo.png")
        #self.screen.fill((0, 0, 0))

        self.botton = [navigationBotton(100, self.screenHeight/2+50, self.screenWidth / 2.4, 75,self.screen, (0, 112, 192,0), "FAIRE LE TUTORIAL", 50, 0, "Arial.ttf", (255, 255, 255))]
        self.botton.append(navigationBotton(100, self.screenHeight/2+150, self.screenWidth / 2.4, 75,self.screen, (0, 172, 240,0), "RECALIBRER", 50, 0, "Arial.ttf", (255, 255, 255)))
        self.botton.append(navigationBotton(100, self.screenHeight/2+250, self.screenWidth / 2.4, 75,self.screen, (0, 112, 192,0), "AIDE", 50,0, "Arial.ttf", (255, 255, 255)))

        self.animation = cocheBotton(self.screenWidth/2, self.screenHeight/2, 25, self.screen, (255, 0, 0), (0, 255, 0), True)

        pygame.font.init()
        fontGlitch=pygame.font.Font("./font/Glitch.otf",100)
        fontArial=pygame.font.Font("./font/Arial.ttf",50)

        volume = fontGlitch.render("OPTIONS", True, (255, 255, 255))
        self.screen.blit(volume, (self.screenWidth/2-300, self.screenHeight / 2 - 350))

        volume = fontArial.render("Volume du jeux", True, (255,255,255))
        self.screen.blit(volume, (100, self.screenHeight/2-250))

        luminosité = fontArial.render("Luminosite", True, (255,255,255))
        self.screen.blit(luminosité, (100, self.screenHeight / 2-150))

        animation = fontArial.render("Activer les animations", True, (255,255,255))
        self.screen.blit(animation, (100, self.screenHeight / 2-50))

        pygame.display.update()
        pygame.font.quit()

        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0

        continuer=True

        while continuer:

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            self.testAffichage()

            pygame.display.update()

        pygame.quit()

    def show(self):
        self.screen.blit(self.fondLogo, (self.screenWidth/10, self.screenHeight/2-249))

    def testAffichage(self):

        if len(self.detection.leftHand)>0:
            #print("right", self.rightHand[0], "  ", self.rightHand[1])
            pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.leftHand[0], self.detection.leftHand[1]), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 0, 0), (self.detection.rightHand[0],  self.detection.rightHand[1]), 10)