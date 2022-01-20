import pygame.draw

from Buttons.PictureButton import *
from Interface.SettingsInterface import *
from Interface.Interface import *

class EndInterface(Interface):

    def __init__(self,screenData,screen,detection,settings,parent):
        self.parent=parent
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        background=pygame.image.load("./picture/interface/parameterBackground.png")
        self.background = pygame.transform.scale(background, (450, 600))

        self.button=[pictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 +50, 400, 100, self.screen, "button2.png","REDEMARRER", 30, 50, "Glitch.otf", (255, 255, 255))]
        self.button.append(pictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 + 170, 400, 100, self.screen, "button2.png","QUITTER", 30, 50, "Glitch.otf", (255, 255, 255)))

        self.show()
        self.resetCoo()
        self.loop()


    def loop(self):
        continuer=True

        while continuer:

            self.detection.hand_detection()

            if len(self.detection.rightHand) > 0:
                self.rightX = self.screenWidth-self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.parent.continuer = False
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.isFistClosed = 1

            self.showHand()

            if self.detection.isFistClosed == 1:
                if self.rightX > self.button[0].x and self.rightX < (self.button[0].x + self.button[0].width) and self.rightY > self.button[0].y and self.rightY < (self.button[0].y + self.button[0].height):
                    self.parent.stage.load()
                    self.resetCoo()
                    self.show()
                    continuer = False

                elif self.rightX > self.button[1].x and self.rightX < (self.button[1].x + self.button[1].width) and self.rightY > self.button[1].y and self.rightY < (self.button[1].y + self.button[1].height):
                    self.parent.continuer = False
                    continuer = False

    def show(self):
        self.screen.blit(self.background, (self.screenWidth/2-225,self.screenHeight/2-300))
        for c in self.button:
            c.showButton()
        pygame.font.init()
        myfont = pygame.font.Font("./font/lemonmilk.otf", 150)
        myfont2 = pygame.font.Font("./font/lemonmilk.otf", 40)
        myfont3=pygame.font.Font("./font/lemonmilk.otf", 30)
        textsurface = myfont2.render("Fin du niveau", True, (255, 255, 255))
        textscore=myfont3.render("Votre score est:", True, (255, 255, 255))
        score = myfont.render(str(self.parent.stage.score), True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(textsurface, (self.screenWidth / 2 - 150, self.screenHeight/2-270))
        self.screen.blit(textscore, (self.screenWidth / 2 - 160, self.screenHeight / 2 - 200))
        self.screen.blit(score, (self.screenWidth / 2 - 100, self.screenHeight / 2 - 175 ))


    def showHand(self):
        self.parent.show()
        self.show()
        if len(self.detection.leftHand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)
        pygame.display.update()

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0