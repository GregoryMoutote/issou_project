import pygame.draw

from Buttons.ColorButton import *
from Buttons.MultipleButton import *
from Interface.InterfaceCalibrage import *

class InterfaceSettings(interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection
        self.detection.initHandCapture()

        super().__init__(screenData, screen)

        self.background = pygame.image.load("./picture/interface/fond.png")
        self.fondLogo=pygame.image.load("./picture/interface/fondLogo.png")

        self.button = [(colorButton(100, self.screenHeight / 2 + 120, self.screenWidth * 0.85, 70, self.screen, (0, 172, 240), "Recalibrer", 50, self.screenWidth * 0.5 - 230, "Arial.ttf", (255, 255, 255)))]
        self.button.append(colorButton(100, self.screenHeight / 2 + 190, self.screenWidth * 0.85, 70, self.screen, (0, 112, 192), "Aide", 50, self.screenWidth * 0.5 - 180, "Arial.ttf", (255, 255, 255)))
        self.button.append(colorButton(100, self.screenHeight / 2 + 260, self.screenWidth * 0.85, 70, self.screen, (120, 120, 120), "Quitter", 50, self.screenWidth * 0.5 - 180, "Arial.ttf", (255, 255, 255)))

        self.volumeButton = multipleButton(225, self.screenHeight / 2 - 217, 1350, 100, self.screen, "soundOn.png", "soundOff.png", 10, self.settings.volume)

        if(self.settings.volume==0):
            self.muteButton = cocheButton(100, self.screenHeight / 2 - 217, 100, 100, self.screen, "SoundMute.png", "SoundActive.png", True)
        else:
            self.muteButton = cocheButton(100, self.screenHeight / 2 - 217, 100, 100, self.screen, "SoundMute.png", "SoundActive.png", False)

        self.animationButton = cocheButton(700, self.screenHeight / 2 - 92, 100, 100, self.screen, "checkedOn.png", "checkedOff.png", self.settings.animation)

        self.resetCoo()
        self.loop()


    def loop(self):
        continuer=True

        while continuer:

            self.detection.hand_detection()

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.isFistClosed = 1

            self.showHand()

            if self.detection.isFistClosed == 1:
                if self.rightX>self.animationButton.x and self.rightX<(self.animationButton.x + self.animationButton.width) and self.rightY>self.animationButton.y and self.rightY<(self.animationButton.y + self.animationButton.height):
                    self.settings.animation=self.animationButton.changeStat()
                    self.resetCoo()

                elif self.rightX>self.muteButton.x and self.rightX<(self.muteButton.x + self.muteButton.width) and self.rightY>self.muteButton.y and self.rightY<(self.muteButton.y + self.muteButton.height):
                    self.muteButton.changeStat()
                    if(self.muteButton.actif):
                        self.settings.volume=0
                        self.volumeButton.changeStat(0)
                    else:
                        self.settings.volume = 1
                        self.volumeButton.changeStat(1)
                    self.resetCoo()

                elif self.rightX > self.button[0].x and self.rightX < (self.button[0].x + self.button[0].width) and self.rightY > self.button[0].y and self.rightY < (self.button[0].y + self.button[0].height):
                    InterfaceCalibrage(self.screenData, self.screen,self.detection)
                    self.resetCoo()
                    self.show()

                elif self.rightX>(self.button[2].x) and self.rightX<(self.button[2].x + self.button[2].width) and self.rightY>(self.button[2].y) and self.rightY<(self.button[2].y + self.button[2].height):
                    self.settings.saveChange()
                    continuer=False

                for i in range(0, self.volumeButton.nbBottun):
                    if self.rightX>self.volumeButton.coche[i].x and self.rightX<(self.volumeButton.coche[i].x + self.volumeButton.coche[i].width) and self.rightY>self.volumeButton.coche[i].y and self.rightY<(self.volumeButton.coche[i].y + self.volumeButton.coche[i].height):
                        self.volumeButton.changeStat(i + 1)
                        self.settings.volume = i+1
                        if(self.muteButton.actif==True):
                            self.muteButton.changeStat()

    def show(self):
        pygame.font.init()
        fontGlitch = pygame.font.Font("./font/Glitch.otf", 100)
        fontArial = pygame.font.Font("./font/Arial.ttf", 56)

        text = fontGlitch.render("OPTIONS", True, (255, 255, 255))
        text2 = fontArial.render("Activer les animations", True, (255, 255, 255))
        pygame.font.quit()

        self.screen.blit(self.background, (0, 0))
        for c in self.button:
            c.showButton()

        self.screen.blit(text, (self.screenWidth / 2 - 250, self.screenHeight / 2 - 350))
        self.screen.blit(text2, (100, self.screenHeight / 2 - 75))

        # text = fontArial.render("Volume", True, (255, 255, 255))
        # self.screen.blit(text, (100, self.screenHeight / 2 - 200))

        self.volumeButton.showButton()
        self.muteButton.showButton()
        self.animationButton.showButton()


    def showHand(self):
        self.show()
        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)
        pygame.display.update()


    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0