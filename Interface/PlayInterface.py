import pygame.draw

from Button.PictureButton import *
from Interface.InterfaceCalibrage import *
from pygame.locals import *

class playInterface(interface):

    def __init__(self,screenData,screen,detection,settings,levelName):
        self.levelName=levelName
        self.settings=settings
        self.detection=detection
        self.detection.initHandCapture()

        super().__init__(screenData, screen)

        self.background=pygame.image.load("./levels/"+levelName+"/background.png")
        self.background = pygame.transform.scale(self.background, (width, height))
        self.pauseButton= pictureButton(20,20,100,100,self.screen,"pause.png","",0,0,"",(0,0,0))
        un=pygame.image.load("./picture/interface/nb_1.png")
        deux = pygame.image.load("./picture/interface/nb_2.png")
        self.trois = pygame.image.load("./picture/interface/nb_3.png")
        self.clock = pygame.time.Clock()
        #self.timer=pygame.time.timer(USEREVENT+0,1000)

        pygame.font.init()
        self.font=pygame.font.SysFont('Cambria',12)
        self.fps_label=self.font.render('FPS: {}'.format(self.clock.get_fps()),True,(255,255,255))
        fenetre=(1920,1080)
        self.fps_rect=self.fps_label.get_rect(bottomright=fenetre)
        pygame.font.quit()

        self.show()
        self.resetCoo()
        self.loop()


    def loop(self):
        continuer=True

        while continuer:

            self.detection.hand_detection()

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()

            self.showHand()


    def showHand(self):
        self.show()
        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)
        pygame.display.update()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.pauseButton.showButton()
        self.screen.blit(self.trois, (self.screenWidth / 2 - 150, self.screenHeight / 2 - 150))
        self.screen.blit(self.fps_label,self.fps_rect)
        pygame.display.update()

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0