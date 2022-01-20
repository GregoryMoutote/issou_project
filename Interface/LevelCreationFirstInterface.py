import pygame.draw

from Interface.Interface import *
from Buttons.PictureButton import *
from Interface.LevelCreationSecondInterface import *

class LevelCreationFirstInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection


        super().__init__(screenData, screen)

        ##TEXT INPUT
        self.defautX = self.screenWidth / 2 - 175
        self.input_rect = pygame.Rect(self.defautX, self.screenHeight/2-200, 1000, 50)
        self.isInputActive = False
        self.userText = ""
        self.color = (0,0,0)
        self.activeColor = (100,100,100)
        self.inactiveColor = (50,50,50)

        self.background=pygame.image.load("./picture/interface/levelBuilderBackground.png")

        self.button = [PictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 - 25, 400, 75, self.screen, "button2.png", "Voir mes fichiers", 30, 40, "Glitch.otf", (255, 255, 255))]
        self.button.append(PictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 + 125, 400, 75, self.screen, "button2.png", "Voir mes fichiers", 30, 40, "Glitch.otf", (255, 255, 255)))
        self.button.append(PictureButton(self.screenWidth / 2 - 200, self.screenHeight / 2 + 250, 400, 75, self.screen, "button3.png", "Valider", 30, 120, "Glitch.otf", (255, 255, 255)))

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
                    if self.isInputActive:
                        if event.key == pygame.K_BACKSPACE:
                            self.userText = self.userText[:-1]
                        else:
                            self.userText += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.mediaPipe.isFistClosed=1

            self.showHand()

            if self.isInputActive:
                self.color = self.activeColor
            else:
                self.color = self.inactiveColor

            if self.detection.mediaPipe.isFistClosed==1:
                if self.rightX>self.button[0].x and self.rightX<(self.button[0].x+self.button[0].width) and self.rightY>self.button[0].y and self.rightY<(self.button[0].y+self.button[0].height):
                   self.resetCoo()
                   self.show()
                   self.isInputActive = False

                elif self.rightX>self.button[1].x and self.rightX<(self.button[1].x+self.button[1].width) and self.rightY>self.button[1].y and self.rightY<(self.button[1].y+self.button[1].height):
                    self.resetCoo()
                    self.show()
                    self.isInputActive = False

                elif self.rightX>self.button[2].x and self.rightX<(self.button[2].x+self.button[2].width) and self.rightY>self.button[2].y and self.rightY<(self.button[2].y+self.button[2].height):
                    LevelCreationSecondInterface(self.screenData, self.screen, self.detection, self.settings)
                    self.resetCoo()
                    self.show()
                    self.isInputActive = False

                elif self.rightX>self.input_rect.x and self.rightX<(self.input_rect.x+self.input_rect.w) and self.rightY>self.input_rect.y and self.rightY<(self.input_rect.y+self.input_rect.h):
                    self.isInputActive = True
                    pass
                else:
                    self.isInputActive = False



    def show(self):
        self.screen.blit(self.background, (0, 0))

        pygame.font.init()
        glitchFont = pygame.font.Font("./font/glitch.otf", 80)
        littleglitchFont=pygame.font.Font("./font/glitch.otf",40)
        titleText = glitchFont.render("Cre ation de niveau", True, (255, 255, 255))
        text1=littleglitchFont.render("Nom du niveau", True, (255, 255, 255))
        text2 = littleglitchFont.render("Image de fond", True, (255, 255, 255))
        text3 = littleglitchFont.render("Musique", True, (255, 255, 255))
        pygame.draw.rect(self.screen, self.color , self.input_rect)
        text_surface = littleglitchFont.render(self.userText, True, (255, 255, 255))
        pygame.font.quit()


        self.screen.blit(titleText, (self.screenWidth / 2 - 500, 30))
        self.screen.blit(text1, (self.screenWidth / 2 - 175, self.screenHeight/2-250))
        self.screen.blit(text2, (self.screenWidth / 2 - 175, self.screenHeight/2-75))
        self.screen.blit(text3, (self.screenWidth / 2 - 105, self.screenHeight/2+75))
        self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width() + 10)


        if len(self.userText) <= 2:
            self.input_rect.x = (self.screenWidth / 2) - (self.input_rect.w/2)
        else:
            self.input_rect.x = self.screenWidth / 2 - text_surface.get_width() / 2


        for bottun in self.button:
            bottun.showButton()




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