import pygame.draw

from Interface.secondInterface import *
from Interface.InterfaceSettings import *
from MainMenuGIF import *

class MainMenuInterface(Interface):

    def __init__(self,detection,screendata,screen,settings):
        self.settings=settings
        self.detection=detection
        self.screenData=screendata
        self.screen=screen

        super().__init__(self.screenData, self.screen)

        self.background=pygame.image.load("./picture/interface/fond.png")

        #clock = pygame.time.Clock()
        #pygame.display.set_caption("Sprite Animation")
        #moving_sprites = pygame.sprite.Group()
        #ISSOUlaod = MenuGIF(self.screenWidth/2-300,self.screenHeight/2,self.screen)
        #moving_sprites.add(ISSOUlaod)

        self.fondLogo=pygame.image.load("./picture/interface/fondLogo.png")

        self.screen.blit(self.background, (0, 0))

        self.botton=[navigationBotton(self.screenWidth/6*3+5,self.screenHeight/2-187,self.screenWidth/2.4,75,self.screen,(0,112,192),"JOUER",40,290,"Glitch.otf",(255,255,255))]
        self.botton.append(navigationBotton(self.screenWidth/6*3+5,self.screenHeight/2-112,self.screenWidth/2.4,75,self.screen,(0,172,240),"TUTORIAL",40,260,"Glitch.otf",(255,255,255)))
        self.botton.append(navigationBotton(self.screenWidth/6*3+5,self.screenHeight/2-37,self.screenWidth/2.4,75,self.screen,(0,112,192),"PARAMETRE",40,230,"Glitch.otf",(255,255,255)))
        self.botton.append(navigationBotton(self.screenWidth/6*3+5,self.screenHeight/2+38,self.screenWidth/2.4,75,self.screen,(0,172,240),"CREER UN NIVEAU",40,160,"Glitch.otf",(255,255,255)))
        self.botton.append(navigationBotton(self.screenWidth/6*3+5,self.screenHeight/2+113,self.screenWidth/2.4,75,self.screen,(0,112,192),"QUITTER",40,275,"Glitch.otf",(255,255,255)))

        self.screen.blit(self.fondLogo, (self.screenWidth/10, self.screenHeight/2-249))

        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0

        continuer=True

        while continuer:

            detection.hand_detection()

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            self.testAffichage()

            pygame.display.update()

            if self.rightX>self.botton[0].x and self.rightX<(self.botton[0].x+self.botton[0].width) and self.rightY>self.botton[0].y and self.rightY<(self.botton[0].y+self.botton[0].height):
               SecondInterface(self.screenData, self.screen)
               self.rightX = 0
               self.rightY = 0
               self.leftX = 0
               self.leftY = 0
               self.show()

            if self.rightX>self.botton[2].x and self.rightX<(self.botton[2].x+self.botton[2].width) and self.rightY>self.botton[2].y and self.rightY<(self.botton[2].y+self.botton[2].height):
                InterfaceSettings(self.detection,self.screenData, self.screen,self.settings)
                self.rightX = 0
                self.rightY = 0
                self.leftX = 0
                self.leftY = 0
                self.show()

            if self.rightX>self.botton[4].x and self.rightX<(self.botton[4].x+self.botton[4].width) and self.rightY>self.botton[4].y and self.rightY<(self.botton[4].y+self.botton[4].height):
               self.detection.closeCamera()
               continuer=False

        pygame.quit()


    def toucheCible(left,top,radius,x,y):

        if(x>left-radius and x<left+radius):
            hypotenuse=(radius)**2
            adjacent=(left-x)**2
            if(adjacent<=hypotenuse):
                axeY=sqrt(hypotenuse-adjacent)

                if(y>top-axeY and y<top+axeY):
                    return True
        return False


    def show(self):
        self.screen.blit(self.background, (0, 0))
        for c in self.botton:
            c.showBotton()
        self.screen.blit(self.fondLogo, (self.screenWidth/10, self.screenHeight/2-249))


    def testAffichage(self):

        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.detection.leftHand[0], self.detection.leftHand[1]), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.rightHand[0],  self.detection.rightHand[1]), 10)