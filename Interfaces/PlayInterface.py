import pygame.draw

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
                        pygame.mixer.music.stop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.is_fist_closed = 1

            self.stage.test_collision(self.right_x, self.right_y)

            self.stage.update_targets()
            self.stage.play()
            self.show_hand()


            if self.stage.is_end():
                self.stage.save_best_score()
                pygame.mixer.music.stop()
                EndInterface(self.screen_data, self.screen, self.detection, self.settings, self)

            if self.detection.is_fist_closed == 1:
                if self.pause_button.x < self.right_x < (self.pause_button.x + self.pause_button.width) and \
                        self.pause_button.y < self.right_y < (self.pause_button.y + self.pause_button.height):
                    self.stage.pause()
                    PauseInterface(self.screen_data, self.screen, self.detection, self.settings, self)
                    self.stage.resume()
                    self.reset_coo()
                    self.detection.hand_points.clear()
                    self.show()



    def show_hand(self):
        self.show()
        if len(self.detection.right_hand) > 0:
            pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.right_hand[0]- 10,
                                                              self.detection.right_hand[1] - 10), 20)
        pygame.display.update()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.stage.show_targets()
        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 80)
        text_surface = my_font.render("score: " + str(self.stage.score), True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(text_surface, (self.screen_width / 2 - 200, 30))

    def newScreen(self):
        background = pygame.image.load("./Stages/" + self.stage.name + "/background.png")
        background = pygame.transform.scale(background, (width, height))
        self.screen.blit(background, (0, 0))
        self.pause_button.show_button()
        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")
        self.show()

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.leftX = 0
        self.leftY = 0