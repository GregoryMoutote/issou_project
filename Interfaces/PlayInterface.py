import pygame.draw,threading

from Interfaces.PauseInterface import *
from Interfaces.EndInterface import *

class PlayInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings, stage):

        self.stage = stage
        self.settings = settings
        self.detection = detection
        super().__init__(screen_data, screen)

        self.stage.load()

        self.pause_button = PictureButton(20, 20, self.screen_height*0.1, self.screen_height*0.1, self.screen, "pause.png", "",0, "", (0, 0, 0))

        self.newScreen()
        self.reset_coo()

        self.thread = PlayInterfaceThread(screen,stage,detection,self)  # crée le thread
        self.thread.start()

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

            self.stage.test_collision(self.right_x, self.right_y)

            self.stage.update_targets()
            self.stage.play()


            if self.stage.is_end():
                self.stage.save_best_score()
                pygame.mixer.music.stop()
                EndInterface(self.screen_data, self.screen, self.detection, self.settings, self)

            if self.detection.is_fist_closed == 1:
                if self.pause_button.x < self.right_x < (self.pause_button.x + self.pause_button.width) and \
                        self.pause_button.y < self.right_y < (self.pause_button.y + self.pause_button.height):
                    self.thread.end()
                    self.stage.pause()
                    PauseInterface(self.screen_data, self.screen, self.detection, self.settings, self)
                    self.stage.resume()
                    if(self.go_on):
                        self.newScreen()
                        self.thread = PlayInterfaceThread(self.screen,self.stage,self.detection,self)
                        self.thread.start()
                    self.detection.hand_points.clear()
                    self.reset_coo()


    def newScreen(self):
        background = pygame.image.load("./Stages/" + self.stage.name + "/background.png")
        background = pygame.transform.scale(background, (width, height))
        self.screen.blit(background, (0, 0))
        self.pause_button.show_button()
        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")


    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.leftX = 0
        self.leftY = 0



class PlayInterfaceThread(Interface,threading.Thread):

    def __init__(self,screen,stage,detection,interface):
        threading.Thread.__init__(self)
        self.background = pygame.image.load("background.jpg")
        pygame.font.init()
        self.my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 80)
        self.screen=screen
        self.stage=stage
        self.detection=detection
        self.interface=interface
        self.continuer=True

    def end(self):
        self.continuer = False

    def run(self):
        while (self.continuer):
            self.screen.blit(self.background, (0, 0))
            self.stage.show_targets()
            text_surface = self.my_font.render("score: " + str(self.stage.score), True, (255, 255, 255))
            self.screen.blit(text_surface, ((self.interface.screen_width - text_surface.get_width()) * 0.5, 30))
            if len(self.detection.right_hand) > 0:
                pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.right_hand[0] - 10,
                                                                  self.detection.right_hand[1] - 10), 20)
            pygame.display.update()
        del self.my_font
        pygame.font.quit()