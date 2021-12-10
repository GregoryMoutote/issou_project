import pygame.draw
import ctypes

from secondInterface import *
from botton import *
from InterfaceCalibrage import *
from Interface import *

class MainMenuInterface(Interface):

    def __init__(self,detection,screendata,screen):
        self.detection=detection
        self.screenData=screendata
        self.screen=screen
        super().__init__(self.screenData, self.screen)

        self.background=pygame.image.load("picture/fond.png")
        self.fondLogo=pygame.image.load("picture/fondLogo.png")
        #self.screen.blit(self.background, (0, 0))
        self.screen.fill((0, 0, 0))

        self.botton=[Botton(self.screenWidth/6*3+5,self.screenHeight/2-187,self.screenWidth/2.4,75,self.screen,(0,112,192),"JOUER",40,290,"Glitch.otf",(255,255,255))]
        self.botton.append(Botton(self.screenWidth/6*3+5,self.screenHeight/2-112,self.screenWidth/2.4,75,self.screen,(0,172,240),"TUTORIAL",40,260,"Glitch.otf",(255,255,255)))
        self.botton.append(Botton(self.screenWidth/6*3+5,self.screenHeight/2-37,self.screenWidth/2.4,75,self.screen,(0,112,192),"PARAMETRE",40,230,"Glitch.otf",(255,255,255)))
        self.botton.append(Botton(self.screenWidth/6*3+5,self.screenHeight/2+38,self.screenWidth/2.4,75,self.screen,(0,172,240),"CREER UN NIVEAU",40,160,"Glitch.otf",(255,255,255)))
        self.botton.append(Botton(self.screenWidth/6*3+5,self.screenHeight/2+113,self.screenWidth/2.4,75,self.screen,(0,112,192),"QUITTER",40,275,"Glitch.otf",(255,255,255)))

        self.screen.blit(self.fondLogo, (self.screenWidth/10, self.screenHeight/2-249))
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0

        continuer=True

        while continuer:
            hand = self.detection.mediaPipeClass.hand

            if (len(hand)==1):
                self.rightX = hand[0][0]
                self.rightY = hand[0][1]
            if (len(hand)==2):
                self.rightX = hand[1][0]
                self.rightY = hand[1][1]
                self.leftX = hand[0][0]
                self.leftY = hand[0][1]

            self.testAffichage()

            pygame.display.update()

            #if self.rightX>self.botton[0].x and self.rightX<(self.botton[0].x+self.botton[0].width) and self.rightY>self.botton[0].y and self.rightY<(self.botton[0].y+self.botton[0].height):
               #SecondInterface(screenData, self.screen)
               #self.botton[0].animeBotton();
               #self.rightX = 0
               #self.rightY = 0
               #self.leftX = 0
               #self.leftY = 0
               #self.show()

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
        #print("right",self.rightX,"  ",self.rightY)
        pygame.draw.circle(self.screen, (0, 255, 0), (self.rightX, self.rightY), 10)
        pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX, self.leftY), 10)