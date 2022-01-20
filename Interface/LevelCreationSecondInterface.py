import pygame.draw

from Buttons import CocheButton
from Interface.Interface import *
from Buttons.TimelineButton import *
from Buttons.PictureButton import *
from Buttons.CocheButton import *

class LevelCreationSecondInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        self.background=pygame.image.load("./picture/interface/levelBuilderBackground.png")
        self.background=pygame.transform.scale(self.background, (self.screenWidth*0.80+1, self.screenHeight*0.80+1))

        self.rightMenu=pygame.image.load("./picture/interface/menuBackground.png")
        self.rightMenu=pygame.transform.scale(self.rightMenu, (self.screenWidth, self.screenHeight*0.20))

        self.bottomMenu=pygame.image.load("./picture/interface/menuBackground.png")
        self.bottomMenu=pygame.transform.scale(self.bottomMenu, (self.screenWidth*0.20,self.screenHeight ))

        self.playButton=CocheButton(self.screenWidth*0.05, self.screenHeight*0.82, self.screenHeight*0.1, self.screenHeight*0.1, self.screen,"levelCreationPlay.png","levelCreationPause.png",True)
        self.fullscreenButton=CocheButton(self.screenWidth*0.26, self.screenHeight*0.82, self.screenHeight*0.1, self.screenHeight*0.1, self.screen,"maximiser.png","minimiser.png",True)


        self.bottuns = [PictureButton(self.screenWidth * 0.12, self.screenHeight * 0.82, self.screenHeight * 0.1, self.screenHeight * 0.1, self.screen, "minusTen.png", "", 0, 0, "", (255, 255, 255))]
        self.bottuns.append(PictureButton(self.screenWidth * 0.19, self.screenHeight * 0.82, self.screenHeight * 0.1, self.screenHeight * 0.1, self.screen, "plusTen.png", "", 0, 0, "", (255, 255, 255)))

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
                if self.rightX > self.bottuns[0].x and self.rightX < (self.bottuns[0].x + self.bottuns[0].width) and self.rightY > self.bottuns[0].y and self.rightY < (self.bottuns[0].y + self.bottuns[0].height):
                    self.resetCoo()
                    self.show()

                elif self.rightX > self.bottuns[1].x and self.rightX < (self.bottuns[1].x + self.bottuns[1].width) and self.rightY > self.bottuns[1].y and self.rightY < (self.bottuns[1].y + self.bottuns[1].height):
                    self.resetCoo()
                    self.show()

                elif self.rightX > self.playButton.x and self.rightX < (self.playButton.x + self.playButton.width) and self.rightY > self.playButton.y and self.rightY < (self.playButton.y + self.playButton.height):
                    self.playButton.changeStat()
                    self.resetCoo()
                    self.show()

                elif self.rightX > self.fullscreenButton.x and self.rightX < (self.fullscreenButton.x + self.fullscreenButton.width) and self.rightY > self.fullscreenButton.y and self.rightY < (self.fullscreenButton.y + self.fullscreenButton.height):
                    self.fullscreenButton.changeStat()
                    self.resetCoo()
                    self.show()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.bottomMenu,(self.screenWidth*0.8,0))
        self.screen.blit(self.rightMenu,(0,self.screenHeight*0.8))
        self.playButton.showButton()
        self.fullscreenButton.showButton()
        for button in self.bottuns:
            button.showButton()
        self.timeline.changeStat(0.25)
        self.timeline.showButton()
        pygame.font.init()
        myfont = pygame.font.Font("./font/arial.ttf", 30)
        textsurface = myfont.render("Choix des cibles", True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(textsurface,(self.screenWidth*0.85,self.screenHeight*0.05))


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