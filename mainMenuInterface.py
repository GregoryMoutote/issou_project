import ctypes

import pygame.draw

from secondInterface import *
from botton import *
from interfaceCalibrage import *

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)


class MainMenuInterface:

    def __init__(self,detection):
        pygame.init()
        print("init pygame")
        self.detection=detection
        screenData = ctypes.windll.user32
        self.screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN,pygame.NOFRAME)

        self.background=pygame.image.load("picture/fond.png")
        self.fondLogo=pygame.image.load("picture/fondLogo.png")
        self.screen.blit(self.background, (0, 0))

        self.botton=[Botton(width/6*3+5,height/2-187,width/2.4,75,self.screen,(0,112,192),"JOUER",40,290,"Glitch.otf",(255,255,255))]
        self.botton.append(Botton(width/6*3+5,height/2-112,width/2.4,75,self.screen,(0,172,240),"TUTORIAL",40,260,"Glitch.otf",(255,255,255)))
        self.botton.append(Botton(width/6*3+5,height/2-37,width/2.4,75,self.screen,(0,112,192),"PARAMETRE",40,230,"Glitch.otf",(255,255,255)))
        self.botton.append(Botton(width/6*3+5,height/2+38,width/2.4,75,self.screen,(0,172,240),"CREER UN NIVEAU",40,160,"Glitch.otf",(255,255,255)))
        self.botton.append(Botton(width/6*3+5,height/2+113,width/2.4,75,self.screen,(0,112,192),"QUITTER",40,275,"Glitch.otf",(255,255,255)))

        self.screen.blit(self.fondLogo, (width/10, height/2-249))
        self.x=0
        self.y=0

        continuer=True

        while continuer:
            hand = self.detection.mediaPipeClass.hand
            if (len(hand)):
                self.x = hand[0][0]
                self.y = hand[0][1]

            pygame.display.update()

            #for event in pygame.event.get():
                #x,y=pygame.mouse.get_pos()
                #if event.type == pygame.KEYDOWN :
                 #   if event.key == pygame.K_SPACE:
                  #      continuer = False
                #if event.type == pygame.MOUSEBUTTONDOWN:
                 #   pos = pygame.mouse.get_pos()

            if self.x>self.botton[0].x and self.x<(self.botton[0].x+self.botton[0].width) and self.y>self.botton[0].y and self.y<(self.botton[0].y+self.botton[0].height):
               print("passage")
               SecondInterface(screenData, self.screen)
               self.x = 0
               self.y = 0
               self.show()

                    #if self.botton[1].botton.collidepoint(pos):
                     #   InterfaceCalibrage(screenData,self.screen,self.detection)
                      #  self.show()
                       # print("passage")
                    #if self.botton[4].botton.collidepoint(pos):
                     #   self.detection.stop()
                      #  continuer=False
                       # print("arrêt")

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
            c.showTarget()
        self.screen.blit(self.fondLogo, (width/10, height/2-249))


    def testAffichage(self):
        pygame.draw.circle(self.screen, (0, 255,0), (self.x, self.y), 10)