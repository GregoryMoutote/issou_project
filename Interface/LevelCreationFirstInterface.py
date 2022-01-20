import pygame.draw

from Interface.Interface import *
from Buttons.PictureButton import *
from Interface.LevelCreationSecondInterface import *

class LevelCreationFirstInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        self.background=pygame.image.load("./picture/interface/levelBuilderBackground.png")

        self.button = [pictureButton(self.screenWidth / 2 -200, self.screenHeight / 2-25 , 400, 75, self.screen, "button2.png","Voir mes fichiers", 30, 40, "Glitch.otf", (255, 255, 255))]
        self.button.append(pictureButton(self.screenWidth / 2 -200, self.screenHeight / 2 + 125, 400, 75, self.screen, "button2.png","Voir mes fichiers", 30, 40, "Glitch.otf", (255, 255, 255)))
        self.button.append(pictureButton(self.screenWidth / 2 -200, self.screenHeight / 2 + 250, 400, 75, self.screen, "button3.png","Valider", 30, 120, "Glitch.otf", (255, 255, 255)))

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
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.isFistClosed=1

            self.showHand()

            if self.detection.isFistClosed==1:
                if self.rightX>self.button[0].x and self.rightX<(self.button[0].x+self.button[0].width) and self.rightY>self.button[0].y and self.rightY<(self.button[0].y+self.button[0].height):
                   self.resetCoo()
                   self.show()

                elif self.rightX>self.button[1].x and self.rightX<(self.button[1].x+self.button[1].width) and self.rightY>self.button[1].y and self.rightY<(self.button[1].y+self.button[1].height):
                    self.resetCoo()
                    self.show()

                elif self.rightX>self.button[2].x and self.rightX<(self.button[2].x+self.button[2].width) and self.rightY>self.button[2].y and self.rightY<(self.button[2].y+self.button[2].height):
                    LevelCreationSecondInterface(self.screenData, self.screen, self.detection, self.settings)
                    self.resetCoo()
                    self.show()


    def show(self):
        self.screen.blit(self.background, (0, 0))

        pygame.font.init()
        glitchFont = pygame.font.Font("./font/glitch.otf", 80)
        littleglitchFont=pygame.font.Font("./font/glitch.otf",40)
        titleText = glitchFont.render("Cre ation de niveau", True, (255, 255, 255))
        text1=littleglitchFont.render("Nom du niveau", True, (255, 255, 255))
        text2 = littleglitchFont.render("Image de fond", True, (255, 255, 255))
        text3 = littleglitchFont.render("Musique", True, (255, 255, 255))
        pygame.font.quit()

        self.screen.blit(titleText, (self.screenWidth / 2 - 500, 30))
        self.screen.blit(text1, (self.screenWidth / 2 - 175, self.screenHeight/2-250))
        self.screen.blit(text2, (self.screenWidth / 2 - 175, self.screenHeight/2-75))
        self.screen.blit(text3, (self.screenWidth / 2 - 105, self.screenHeight/2+75))

        for bottun in self.button:
            bottun.showButton()




    def showHand(self):
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