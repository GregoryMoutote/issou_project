import pygame.draw

from Buttons.PictureButton import *
from Interface.SettingsInterface import *

class PauseInterface(Interface):

    def __init__(self,screenData,screen,detection,settings,parent):
        self.parent=parent
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        background=pygame.image.load("./picture/interface/parameterBackground.png")
        self.background = pygame.transform.scale(background, (450, 600))

        self.bottun=[PictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 - 160, 400, 100, self.screen, "button2.png", "REPRENDRE", 30, 50, "Glitch.otf", (255, 255, 255))]
        self.bottun.append(PictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 - 50, 400, 100, self.screen, "button2.png", "REDEMARRER", 30, 50, "Glitch.otf", (255, 255, 255)))
        self.bottun.append(PictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 + 60, 400, 100, self.screen, "button2.png", "PARAMETRE", 30, 50, "Glitch.otf", (255, 255, 255)))
        self.bottun.append(PictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 + 170, 400, 100, self.screen, "button2.png", "QUITTER", 30, 50, "Glitch.otf", (255, 255, 255)))

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
                    self.detection.mediaPipe.isFistClosed = 1

            self.showHand()

            if self.detection.mediaPipe.isFistClosed == 1:

                if self.rightX < self.screenWidth/2-225 and self.rightX >self.screenWidth/2+225 and self.rightY < self.screenHeight/2-300 and self.rightY > self.screenHeight/2+300:
                    continuer=False

                elif self.rightX > self.bottun[0].x and self.rightX < (self.bottun[0].x + self.bottun[0].width) and self.rightY > self.bottun[0].y and self.rightY < (self.bottun[0].y + self.bottun[0].height):
                    continuer=False

                elif self.rightX > self.bottun[1].x and self.rightX < (self.bottun[1].x + self.bottun[1].width) and self.rightY > self.bottun[1].y and self.rightY < (self.bottun[1].y + self.bottun[1].height):
                    self.parent.stage.load()
                    self.resetCoo()
                    self.show()
                    continuer=False

                elif self.rightX > self.bottun[2].x and self.rightX < (self.bottun[2].x + self.bottun[2].width) and self.rightY > self.bottun[2].y and self.rightY < (self.bottun[2].y + self.bottun[2].height):
                    SettingsInterface(self.screenData, self.screen, self.detection, self.settings)
                    self.resetCoo()
                    self.show()

                elif self.rightX > self.bottun[3].x and self.rightX < (self.bottun[3].x + self.bottun[3].width) and self.rightY > self.bottun[3].y and self.rightY < (self.bottun[3].y + self.bottun[3].height):
                    self.parent.continuer=False
                    continuer=False

    def show(self):
        self.screen.blit(self.background, (self.screenWidth/2-225,self.screenHeight/2-300))
        for c in self.bottun:
            c.showButton()
        pygame.font.init()
        myfont = pygame.font.Font("./font/lemonmilk.otf", 60)
        textsurface = myfont.render("PAUSE", True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(textsurface, (self.screenWidth / 2 - 110, self.screenHeight/2-270))


    def showHand(self):
        self.parent.show()
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