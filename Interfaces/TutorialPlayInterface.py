import pygame.draw,threading

from Interfaces.EndInterface import *
from Model.Constants import Constants
from Targets.DynamicTarget import DynamicTarget
from Targets.MovingTarget import MovingTarget
from Targets.RailTarget import RailTarget
from Targets.Target import Target


class TutorialPlayInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings):

        self.settings = settings
        self.detection = detection
        super().__init__(screen_data, screen)


        self.target_index=0

        self.targets=[Target([1,0.5, 0.5, 0, 0, 0, "basic_red"], self.screen, "")]
        self.targets.append(MovingTarget([2,0.1, 0.5, 10, 10, 10, "basic_green", 0.9, 0.5], self.screen, ""))
        self.targets.append(DynamicTarget([3,0.5, 0.5, 10, 0, 100, "basic_green", 0], self.screen, ""))
        self.targets.append(RailTarget([4,0.2, 0.2, 0, 0, 100, "basic_green", 0.5, 0.2, 0.7, 0.4, 0.8, 0.6], self.screen, ""))

        self.active_target=self.targets[self.target_index]

        self.newScreen()

        self.thread = PlayInterfaceThread(screen,self.active_target,detection)  # crée le thread
        self.thread.start()

        self.reset_coo()
        self.loop()


    def loop(self):
        self.go_on = True
        while self.go_on:
            self.detection.hand_detection()

            if len(self.detection.right_hand) > 0:
                self.right_x = self.detection.right_hand[0]
                self.right_y = self.detection.right_hand[1]

            if len(self.detection.left_hand) > 0:
                self.left_x = self.detection.left_hand[0]
                self.left_y = self.detection.left_hand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.go_on = False
                        self.thread.continuer=False
                        pygame.mixer.music.stop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.is_fist_closed = 1

            if self.target_index>4:
                EndInterface(self.screen_data, self.screen, self.detection, self.settings, self)

            elif(self.active_target.coordinates.x-Constants.TARGET_RADIUS<self.right_x<self.active_target.coordinates.x+Constants.TARGET_RADIUS and
                self.active_target.coordinates.y-Constants.TARGET_RADIUS<self.right_y<self.active_target.coordinates.y+Constants.TARGET_RADIUS):
                self.target_index+=1
                if self.target_index < 4:
                    self.thread.newTarget(self.targets[self.target_index])
                else:
                    EndInterface(self.screen_data, self.screen, self.detection, self.settings, self)
                self.newScreen()
                self.thread.newScreen()

            print(self.target_index)


    def newScreen(self):
        print("./TutorialStage/tutorial/tuto"+str(self.target_index+1)+".jpg")
        backGround = pygame.image.load("./TutorialStage/tutorial/tuto"+str(self.target_index+1)+".jpg")
        backGround = pygame.transform.scale(backGround, (self.screen_width, self.screen_height))
        self.screen.blit(backGround, (0, 0))
        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")


    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.leftX = 0
        self.leftY = 0



class PlayInterfaceThread(Interface,threading.Thread):

    def __init__(self,screen,target,detection):
        threading.Thread.__init__(self)
        self.background = pygame.image.load("background.jpg")
        self.screen=screen
        self.target=target
        self.detection=detection
        self.continuer=True

        self.number_of_active_targets = 0

    def newScreen(self):
        self.background=pygame.image.load("background.jpg")

    def end(self):
        self.continuer = False

    def newTarget(self,target):
        self.target=target

    def run(self):
        while (self.continuer):
            self.target.update()
            self.screen.blit(self.background, (0, 0))
            self.target.show_target()

            if len(self.detection.right_hand) > 0:
                pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.right_hand[0] - 10,
                                                                  self.detection.right_hand[1] - 10), 20)
            pygame.display.update()