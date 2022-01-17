import pygame.draw

from Interface.Interface import *
from Buttons.PictureButton import *

class pauseInterface(interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        background=pygame.image.load("./picture/interface/parameterBackground.png")
        self.background = pygame.transform.scale(background, (450, 600))

        self.bottun=[pictureButton(self.screenWidth/2-200,self.screenHeight/2-160,400,100,self.screen,"button2.png","REPRENDRE",30,50,"Glitch.otf", (255, 255, 255))]
        self.bottun.append(pictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 -50, 400, 100, self.screen, "button2.png","RECALIBRER", 30, 50, "Glitch.otf", (255, 255, 255)))
        self.bottun.append(pictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 + 60, 400, 100, self.screen, "button2.png","PARAMETRE", 30, 50, "Glitch.otf", (255, 255, 255)))
        self.bottun.append(pictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 + 170, 400, 100, self.screen, "button2.png","QUITTER", 30, 50, "Glitch.otf", (255, 255, 255)))

        self.show()
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

            self.showHand()


    def show(self):
        self.screen.blit(self.background, (self.screenWidth/2-225,self.screenHeight/2-300))
        for c in self.bottun:
            c.showButton()


        pygame.display.update()


    def showHand(self):
        self.show()
        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0