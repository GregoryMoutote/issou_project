import pygame.draw

from Interface.Interface import *
from bottun.NavigationBottoun import *
from bottun.MultipleBottun import *

class InterfaceSettings(Interface):

    def __init__(self,detection,screendata,screen,settings):
        self.settings=settings
        self.detection=detection
        self.detection.initHandCapture()
        self.screenData=screendata
        self.screen=screen

        super().__init__(self.screenData, self.screen)

        self.background = pygame.image.load("./picture/interface/fond.png")
        self.fondLogo=pygame.image.load("./picture/interface/fondLogo.png")

        self.screen.blit(self.background, (0, 0))

        self.bottun = [navigationBottun(100, self.screenHeight/2+50, self.screenWidth*0.85, 70,self.screen, (0, 112, 192), "Faire le calibrage", 50,self.screenWidth*0.5-300, "Arial.ttf", (255, 255, 255))]
        self.bottun.append(navigationBottun(100, self.screenHeight/2+120, self.screenWidth*0.85, 70,self.screen, (0, 172, 240), "Recalibrer", 50, self.screenWidth*0.5-230, "Arial.ttf", (255, 255, 255)))
        self.bottun.append(navigationBottun(100, self.screenHeight/2+190, self.screenWidth*0.85, 70,self.screen, (0, 112, 192), "Aide", 50,self.screenWidth*0.5-180, "Arial.ttf", (255, 255, 255)))
        self.bottun.append(navigationBottun(100, self.screenHeight/2+260, self.screenWidth*0.85, 70,self.screen, (120, 120, 120), "Quitter", 50,self.screenWidth*0.5-180, "Arial.ttf", (255, 255, 255)))

        pygame.font.init()
        fontGlitch=pygame.font.Font("./font/Glitch.otf",100)
        fontArial=pygame.font.Font("./font/Arial.ttf",55)

        text = fontGlitch.render("OPTIONS", True, (255, 255, 255))
        self.screen.blit(text, (self.screenWidth/2-250, self.screenHeight / 2 - 350))

        text = fontArial.render("Volume", True, (255,255,255))
        self.screen.blit(text, (100, self.screenHeight/2-200))

        self.volumeBottun = multipleBottun(400,self.screenHeight / 2-205,1100,88,self.screen,"soundOn.png","soundOff.png",10,self.settings.volume)

        if(self.settings.volume==0):
            self.muteBottun = cocheBottun(345,self.screenHeight / 2-160, 45, self.screen, "SoundMute.png", "SoundActive.png",True)
        else:
            self.muteBottun = cocheBottun(345,self.screenHeight / 2-160, 45, self.screen, "SoundMute.png","SoundActive.png", False)

        text = fontArial.render("Activer les animations", True, (255,255,255))
        self.screen.blit(text, (100, self.screenHeight / 2-75))

        self.animationBottun = cocheBottun(730, self.screenHeight / 2 - 45, 40, self.screen, "checkedOn.png", "checkedOff.png",self.settings.animation)

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

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            if self.rightX>(self.animationBottun.x-self.animationBottun.radius) and self.rightX<(self.animationBottun.x+self.animationBottun.radius) and self.rightY>(self.animationBottun.y-self.animationBottun.radius) and self.rightY<(self.animationBottun.y+self.animationBottun.radius):
                self.settings.animation=self.animationBottun.changeStat()

            if self.rightX>(self.muteBottun.x-self.muteBottun.radius) and self.rightX<(self.muteBottun.x+self.muteBottun.radius) and self.rightY>(self.muteBottun.y-self.muteBottun.radius) and self.rightY<(self.muteBottun.y+self.muteBottun.radius):
                self.muteBottun.changeStat()
                if(self.muteBottun.actif):
                    self.settings.volume=0
                    self.volumeBottun.changeStat(0)
                else:
                    self.settings.volume = 1
                    self.volumeBottun.changeStat(1)


            if self.rightX>(self.bottun[3].x) and self.rightX<(self.bottun[3].x+self.bottun[3].width) and self.rightY>(self.bottun[3].y) and self.rightY<(self.bottun[3].y+self.bottun[3].height):
                continuer=False

            for i in range(0, self.volumeBottun.nbBottun):
                if self.rightX>(self.volumeBottun.coche[i].x-self.volumeBottun.coche[i].radius) and self.rightX<(self.volumeBottun.coche[i].x+self.volumeBottun.coche[i].radius) and self.rightY>(self.volumeBottun.coche[i].y-self.volumeBottun.coche[i].radius) and self.rightY<(self.volumeBottun.coche[i].y+self.volumeBottun.coche[i].radius):
                    self.volumeBottun.changeStat(i+1)
                    self.settings.volume = i+1
                    if(self.muteBottun.actif==True):
                        self.muteBottun.changeStat()


            self.testAffichage()

            pygame.display.update()

    def testAffichage(self):

        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.detection.leftHand[0]-5, self.detection.leftHand[1]-5), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.rightHand[0]-5,  self.detection.rightHand[1]-5), 10)