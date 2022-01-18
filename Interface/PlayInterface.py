import pygame.draw

from Interface.InterfaceCalibrage import *
from Interface.PauseInterface import *

class playInterface(interface):

    def __init__(self,screenData,screen,detection,settings,stage):
        self.stage=stage
        self.settings=settings
        self.detection=detection
        self.detection.initHandCapture()

        super().__init__(screenData, screen)

        self.stage.load()
        self.background=pygame.image.load("./stages/"+self.stage.name+"/background.png")
        self.background = pygame.transform.scale(self.background, (width, height))
        self.pauseButton= pictureButton(20,20,100,100,self.screen,"pause.png","",0,0,"",(0,0,0))
        un=pygame.image.load("./picture/interface/nb_1.png")
        deux = pygame.image.load("./picture/interface/nb_2.png")
        self.trois = pygame.image.load("./picture/interface/nb_3.png")

        self.show()
        self.resetCoo()
        self.loop()


    def loop(self):
        self.continuer=True

        while self.continuer:

            self.detection.complete_hand_detection()

            if len(self.detection.hand_points) > 0:
                self.rightX = self.screenWidth-int(self.detection.hand_points[0][0])
                self.rightY = int(self.detection.hand_points[0][1])

            for x, y in self.detection.hand_points:
                self.stage.test_collision(x, y)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.continuer = False
                        self.stage.stage_music.pause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.isFistClosed = 1

            self.stage.play()
            self.showHand()

            if self.detection.isFistClosed == 1:
                if self.rightX > self.pauseButton.x and self.rightX < (self.pauseButton.x + self.pauseButton.width) and self.rightY > self.pauseButton.y and self.rightY < (self.pauseButton.y + self.pauseButton.height):
                    self.stage.pause()
                    pauseInterface(self.screenData, self.screen, self.detection, self.settings,self)
                    self.stage.resume()
                    self.resetCoo()
                    self.show()

            self.showHand()


    def showHand(self):
        self.show()
        if len(self.detection.hand_points)>0:
            pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.hand_points[0][0]-10, self.detection.hand_points[0][1]-10), 20)
        pygame.display.update()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.pauseButton.showButton()
        self.stage.show_targets()
        pygame.font.init()
        myfont = pygame.font.Font("./font/lemonmilk.otf", 80)
        textsurface = myfont.render("score: "+ str(self.stage.score), True, (255,255,255))
        pygame.font.quit()
        self.screen.blit(textsurface, (self.screenWidth/2-200, 30))

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0