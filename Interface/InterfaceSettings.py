import pygame.draw

from Interface.Interface import *

from botton.CocheBotton import *
from botton.NavigationBotton import *
from botton.MultipleBotton import *


class InterfaceSettings(Interface):

    def __init__(self,detection,screendata,screen):
        self.detection=detection
        self.detection.initHandCapture()
        self.screenData=screendata
        self.screen=screen

        super().__init__(self.screenData, self.screen)

        self.background = pygame.image.load("./picture/fond.png")
        self.fondLogo=pygame.image.load("./picture/fondLogo.png")

        self.screen.blit(self.background, (0, 0))
        #self.screen.fill((0, 0, 0))

        self.botton = [navigationBotton(100, self.screenHeight/2+50, self.screenWidth*0.85, 100,self.screen, (0, 112, 192,0), "Faire le calibrage", 50,self.screenWidth*0.5-300, "Arial.ttf", (255, 255, 255))]
        self.botton.append(navigationBotton(100, self.screenHeight/2+150, self.screenWidth*0.85, 100,self.screen, (0, 172, 240,0), "Recalibrer", 50, self.screenWidth*0.5-230, "Arial.ttf", (255, 255, 255)))
        self.botton.append(navigationBotton(100, self.screenHeight/2+250, self.screenWidth*0.85, 100,self.screen, (0, 112, 192,0), "Aide", 50,self.screenWidth*0.5-180, "Arial.ttf", (255, 255, 255)))

        self.animation = cocheBotton(650, self.screenHeight/2 -25, 35, self.screen, (255, 0, 0), (0, 255, 0), True)

        pygame.font.init()
        fontGlitch=pygame.font.Font("./font/Glitch.otf",100)
        fontArial=pygame.font.Font("./font/Arial.ttf",50)

        volume = fontGlitch.render("OPTIONS", True, (255, 255, 255))
        self.screen.blit(volume, (self.screenWidth/2-200, self.screenHeight / 2 - 350))

        volume = fontArial.render("Volume du jeux", True, (255,255,255))
        self.screen.blit(volume, (100, self.screenHeight/2-250))

        self.volumeBotton = multipleBotton(100,self.screenHeight / 2-175,1500,100,self.screen,(120, 120, 120), (0, 255, 0),10,settings.getVolume())

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

            detection.hand_detection()

            self.testAffichage()

            pygame.display.update()

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            if self.rightX>(self.animation.x-self.animation.radius) and self.rightX<(self.animation.x+self.animation.radius) and self.rightY>(self.animation.y-self.animation.radius) and self.rightY<(self.animation.y+self.animation.radius):
               self.animation.changeStat()

            for i in range(0, self.volumeBotton.nbBotton):
                if self.rightX>(self.volumeBotton.coche[i].x-self.volumeBotton.coche[i].radius) and self.rightX<(self.volumeBotton.coche[i].x+self.volumeBotton.coche[i].radius) and self.rightY>(self.volumeBotton.coche[i].y-self.volumeBotton.coche[i].radius) and self.rightY<(self.volumeBotton.coche[i].y+self.volumeBotton.coche[i].radius):
                    self.volumeBotton.changeStat(i)

            self.testAffichage()

            pygame.display.update()

        pygame.quit()

    def show(self):
        self.screen.blit(self.fondLogo, (self.screenWidth/10, self.screenHeight/2-249))

    def testAffichage(self):

        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.detection.leftHand[0], self.detection.leftHand[1]), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.rightHand[0],  self.detection.rightHand[1]), 10)