import pygame.draw

from Interface.Interface import *
from Buttons.TimelineButton import *

class LevelCreationSecondInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        self.background=pygame.image.load("./picture/interface/levelBuilderBackground.png")
        self.background=pygame.transform.scale(self.background, (self.screenWidth*0.80+1, self.screenHeight*0.80+1))

        #self.rightMenu=pygame.image.load("./picture/interface/menuCreationLevel.png")
        #self.rightMenu=pygame.transform.scale(self.rightMenu, (self.screenWidth*0.20, self.screenHeight))

        #self.bottomMenu=pygame.image.load("./picture/interface/menuCreationLevel.png")
        #self.bottomMenu=pygame.transform.scale(self.bottomMenu, (self.screenWidth, self.screenHeight*0.20))

        self.timeline=TimelineButton(self.screenWidth*0.05,self.screenHeight*0.95,self.screenWidth*0.9,self.screenHeight*0.02,self.screen,"timelineGray.png","timelineRed.png")

        self.show()
        self.resetCoo()
        self.loop()


    def loop(self):
        continuer=True

        while continuer:


            if len(self.detection.mediaPipe.rightHand) > 0:
                self.rightX = self.detection.mediaPipe.rightHand[0]
                self.rightY = self.detection.mediaPipe.rightHand[1]

            if len(self.detection.mediaPipe.leftHand) > 0:
                self.leftX = self.detection.mediaPipe.leftHand[0]
                self.leftY = self.detection.mediaPipe.leftHand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.mediaPipe.isFistClosed=1

            self.showHand()

            if self.detection.mediaPipe.isFistClosed==1:
                pass


    def show(self):
        self.screen.blit(self.background, (0, 0))
        #self.screen.blit(self.bottomMenu,(0,self.screenHeight*0.8))
        #self.screen.blit(self.rightMenu,(self.screenWidth*0.8,0))
        self.timeline.changeStat(0.25)
        self.timeline.showButton()


    def showHand(self):
        self.show()
        if len(self.detection.mediaPipe.leftHand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.mediaPipe.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)
        pygame.display.update()

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0