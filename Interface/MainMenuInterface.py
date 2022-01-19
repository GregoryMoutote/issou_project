import pygame.draw

from Interface.LevelSelectionInterface import *
from Interface.InterfaceSettings import *
from Interface.GIF.MainMenuGIF import *
from playerDetection.MediaPipeThread import *
from Interface.LevelCreationFirstInterface import *
import math

class MainMenuInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings

        super().__init__(screenData, screen)

        self.background=pygame.image.load("./picture/interface/fond.png")

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Sprite Animation")
        self.moving_sprites = pygame.sprite.Group()
        ISSOUlaod = MenuGIF(self.screenWidth*0.17,self.screenHeight/2-75,self.screen)
        self.moving_sprites.add(ISSOUlaod)

        self.fondLogo=pygame.image.load("./picture/interface/fondLogo.png")
        self.fondLogo= pygame.transform.scale(self.fondLogo, (787, 500))

        self.bottun=[colorButton(self.screenWidth*0.4, self.screenHeight / 2 - 250, self.screenWidth / 2, 100, self.screen, (0, 112, 192), "JOUER", 50, 450, "Glitch.otf", (255, 255, 255))]
        self.bottun.append(colorButton(self.screenWidth*0.4, self.screenHeight / 2 - 150, self.screenWidth / 2, 100, self.screen, (0, 172, 240), "TUTORIEL", 50, 420, "Glitch.otf", (255, 255, 255)))
        self.bottun.append(colorButton(self.screenWidth*0.4, self.screenHeight / 2 - 50, self.screenWidth / 2, 100, self.screen, (0, 112, 192), "PARAMETRE", 50, 380, "Glitch.otf", (255, 255, 255)))
        self.bottun.append(colorButton(self.screenWidth*0.4, self.screenHeight / 2 + 50, self.screenWidth / 2, 100, self.screen, (0, 172, 240), "CREER UN NIVEAU", 50, 300, "Glitch.otf", (255, 255, 255)))
        self.bottun.append(colorButton(self.screenWidth*0.4, self.screenHeight / 2 + 150, self.screenWidth / 2, 100, self.screen, (0, 112, 192), "QUITTER", 50, 450, "Glitch.otf", (255, 255, 255)))

        self.detection= MediaPipeThread()

        self.show()
        self.resetCoo()
        self.detection.start()
        self.loop()


        pygame.quit()

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
                    if event.key == pygame.K_SPACE:
                        continuer = False
                        self.detection.endDetection()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.isFistClosed=1

            self.showHand()

            if self.detection.mediaPipe.isFistClosed==1:
                if self.rightX>self.bottun[0].x and self.rightX<(self.bottun[0].x+self.bottun[0].width) and self.rightY>self.bottun[0].y and self.rightY<(self.bottun[0].y+self.bottun[0].height):
                   LevelSelectionInterface(self.screenData, self.screen,self.detection,self.settings)
                   self.resetCoo()
                   self.show()

                elif self.rightX>self.bottun[2].x and self.rightX<(self.bottun[2].x+self.bottun[2].width) and self.rightY>self.bottun[2].y and self.rightY<(self.bottun[2].y+self.bottun[2].height):
                    InterfaceSettings(self.screenData, self.screen,self.detection,self.settings)
                    self.resetCoo()
                    self.show()

                elif self.rightX>self.bottun[3].x and self.rightX<(self.bottun[3].x+self.bottun[3].width) and self.rightY>self.bottun[3].y and self.rightY<(self.bottun[3].y+self.bottun[3].height):
                    LevelCreationFirstInterface(self.screenData, self.screen,self.detection,self.settings)
                    self.resetCoo()
                    self.show()

                elif self.rightX>self.bottun[4].x and self.rightX<(self.bottun[4].x+self.bottun[4].width) and self.rightY>self.bottun[4].y and self.rightY<(self.bottun[4].y+self.bottun[4].height):
                   self.detection.endDetection()
                   continuer=False


    def toucheCible(left,top,radius,x,y):

        if(x>left-radius and x<left+radius):
            hypotenuse=(radius)**2
            adjacent=(left-x)**2
            if(adjacent<=hypotenuse):
                axeY=math.sqrt(hypotenuse-adjacent)

                if(y>top-axeY and y<top+axeY):
                    return True
        return False


    def show(self):
        self.screen.blit(self.background, (0, 0))
        for c in self.bottun:
            c.showButton()
        self.screen.blit(self.fondLogo, (self.screenWidth*0.13, self.screenHeight / 2 - 250))
        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update(1)
        self.clock.tick(60)


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