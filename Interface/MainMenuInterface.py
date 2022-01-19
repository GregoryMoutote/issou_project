import pygame.draw

from Interface.LevelSelectionInterface import *
from Interface.SettingsInterface import *
from Interface.GIF.MainMenuGIF import *
from Interface.LevelCreationFirstInterface import *

class MainMenuInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        self.background=pygame.image.load("./picture/interface/fond.png")

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Sprite Animation")
        self.moving_sprites = pygame.sprite.Group()
        ISSOUlaod = MenuGIF(self.screenWidth/2-525,self.screenHeight/2-75,self.screen)
        self.moving_sprites.add(ISSOUlaod)

        self.fondLogo=pygame.image.load("./picture/interface/fondLogo.png")

        self.button=[colorButton(self.screenWidth / 6 * 3 + 5, self.screenHeight / 2 - 187, self.screenWidth / 2.4, 75, self.screen, (0, 112, 192), "JOUER", 40, 290, "Glitch.otf", (255, 255, 255))]
        self.button.append(colorButton(self.screenWidth / 6 * 3 + 5, self.screenHeight / 2 - 112, self.screenWidth / 2.4, 75, self.screen, (0, 172, 240), "TUTORIEL", 40, 260, "Glitch.otf", (255, 255, 255)))
        self.button.append(colorButton(self.screenWidth / 6 * 3 + 5, self.screenHeight / 2 - 37, self.screenWidth / 2.4, 75, self.screen, (0, 112, 192), "PARAMETRE", 40, 230, "Glitch.otf", (255, 255, 255)))
        self.button.append(colorButton(self.screenWidth / 6 * 3 + 5, self.screenHeight / 2 + 38, self.screenWidth / 2.4, 75, self.screen, (0, 172, 240), "CREER UN NIVEAU", 40, 160, "Glitch.otf", (255, 255, 255)))
        self.button.append(colorButton(self.screenWidth / 6 * 3 + 5, self.screenHeight / 2 + 113, self.screenWidth / 2.4, 75, self.screen, (0, 112, 192), "QUITTER", 40, 275, "Glitch.otf", (255, 255, 255)))

        self.show()
        self.resetCoo()
        self.loop()

        pygame.quit()

    def loop(self):
        continuer=True

        while continuer:

            self.detection.hand_detection()

            if len(self.detection.rightHand) > 0:
                self.rightX = self.screenWidth-self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.screenWidth-self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.isFistClosed=1

            self.showHand()

            if self.detection.isFistClosed==1:
                if (self.rightX > self.button[0].x and self.rightX < (self.button[0].x + self.button[0].width) and self.rightY > self.button[0].y and self.rightY < (self.button[0].y + self.button[0].height)) or(
                    self.leftX > self.button[0].x and self.leftX < (self.button[0].x + self.button[0].width) and self.leftY > self.button[0].y and self.leftY < (self.button[0].y + self.button[0].height)):
                    LevelSelectionInterface(self.screenData, self.screen,self.detection,self.settings)
                    self.resetCoo()
                    self.show()

                elif (self.rightX > self.button[2].x and self.rightX < (self.button[2].x + self.button[2].width) and self.rightY > self.button[2].y and self.rightY < (self.button[2].y + self.button[2].height)) or(
                    self.leftX > self.button[2].x and self.leftX < (self.button[2].x + self.button[2].width) and self.leftY > self.button[2].y and self.leftY < (self.button[2].y + self.button[2].height)):
                    SettingsInterface(self.screenData, self.screen, self.detection, self.settings)
                    self.resetCoo()
                    self.show()

                elif (self.rightX > self.button[3].x and self.rightX < (self.button[3].x + self.button[3].width) and self.rightY > self.button[3].y and self.rightY < (self.button[3].y + self.button[3].height)) or(
                    self.leftX > self.button[3].x and self.leftX < (self.button[3].x + self.button[3].width) and self.leftY > self.button[3].y and self.leftY < (self.button[3].y + self.button[3].height)):
                    LevelCreationFirstInterface(self.screenData, self.screen, self.detection, self.settings)
                    self.resetCoo()
                    self.show()

                elif (self.rightX > self.button[4].x and self.rightX < (self.button[4].x + self.button[4].width) and self.rightY > self.button[4].y and self.rightY < (self.button[4].y + self.button[4].height)) or(
                    self.leftX > self.button[4].x and self.leftX < (self.button[4].x + self.button[4].width) and self.leftY > self.button[4].y and self.leftY < (self.button[4].y + self.button[4].height)):
                    self.detection.closeCamera()
                    continuer=False


    def show(self):
        self.screen.blit(self.background, (0, 0))
        for c in self.button:
            c.showButton()
        self.screen.blit(self.fondLogo, (self.screenWidth/10, self.screenHeight/2-249))
        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update(1)
        self.clock.tick(60)


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