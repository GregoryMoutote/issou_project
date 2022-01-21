import pygame.draw

from Interfaces.CalibrageInterface import *
from Interfaces.PauseInterface import *
from Interfaces.EndInterface import *

class PlayInterface(Interface):

    def __init__(self,screenData,screen,detection,settings,stage):
        self.stage=stage
        self.settings=settings
        self.detection=detection
        self.detection.fullDetection = True
        super().__init__(screenData, screen)

        self.stage.load()
        self.background=pygame.image.load("./Stages/"+self.stage.name+"/background.png")
        self.background = pygame.transform.scale(self.background, (width, height))
        self.pauseButton= PictureButton(20, 20, 100, 100, self.screen, "pause.png", "", 0, 0, "", (0, 0, 0))

        self.show()
        self.resetCoo()
        self.loop()


    def loop(self):
        self.continuer=True

        while self.continuer:

            if len(self.detection.mediaPipe.hand_points) > 0:
                self.rightX = int(self.detection.mediaPipe.hand_points[0][0])
                self.rightY = int(self.detection.mediaPipe.hand_points[0][1])

            for x, y in self.detection.mediaPipe.hand_points:
                self.stage.test_collision(x, y)
            self.stage.test_collision(self.rightX,self.rightY)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.continuer = False
                        pygame.mixer.music.stop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.mediaPipe.isFistClosed = 1

            self.stage.update_targets()
            self.stage.play()
            self.showHand()


            if self.stage.is_end():
                self.detection.fullDetection = False
                self.stage.save_best_score()
                pygame.mixer.music.stop()
                EndInterface(self.screenData, self.screen, self.detection, self.settings, self)

            if self.detection.mediaPipe.isFistClosed == 1:
                if self.rightX > self.pauseButton.x and self.rightX < (self.pauseButton.x + self.pauseButton.width) and self.rightY > self.pauseButton.y and self.rightY < (self.pauseButton.y + self.pauseButton.height):
                    self.stage.pause()
                    self.detection.fullDetection = False
                    PauseInterface(self.screenData, self.screen, self.detection, self.settings, self)
                    self.detection.fullDetection = True
                    self.stage.resume()
                    self.resetCoo()
                    self.detection.mediaPipe.hand_points.clear()
                    self.show()

        self.detection.fullDetection = False


    def showHand(self):
        self.show()
        if len(self.detection.mediaPipe.hand_points)>0:
            pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.mediaPipe.hand_points[0][0]-10, self.detection.mediaPipe.hand_points[0][1]-10), 20)
        pygame.display.update()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.pauseButton.showButton()
        self.stage.show_targets()
        pygame.font.init()
        myfont = pygame.font.Font("./Fonts/lemonmilk.otf", 80)
        textsurface = myfont.render("score: "+ str(self.stage.score), True, (255,255,255))
        pygame.font.quit()
        self.screen.blit(textsurface, (self.screenWidth/2-200, 30))

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0