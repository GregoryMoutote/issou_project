import pygame.draw

from Interface.Interface import *


class InterfaceSettings(Interface):

    def __init__(self,detection,screendata,screen):
        self.detection=detection
        self.detection.initHandCapture()
        self.screenData=screendata
        self.screen=screen
        super().__init__(self.screenData, self.screen)
        self.fondLogo=pygame.image.load("./picture/fondLogo.png")

        self.screen.blit(self.fondLogo, (self.screenWidth/10, self.screenHeight/2-249))
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0

        continuer=True

        while continuer:
            hand=self.detection.hand_detection()

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