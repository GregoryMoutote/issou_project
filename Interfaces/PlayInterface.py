import pygame.draw

from Interfaces.CalibrationInterface import *
from Interfaces.PauseInterface import *
from Interfaces.EndInterface import *

class PlayInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings, stage):
        self.stage = stage
        self.settings = settings
        self.detection = detection
        self.detection.full_detection = True
        super().__init__(screen_data, screen)

        self.stage.load()
        self.background = pygame.image.load("./Stages/" + self.stage.name + "/background.png")
        self.background = pygame.transform.scale(self.background, (width, height))
        self.pause_button = PictureButton(20, 20, 100, 100, self.screen, "pause.png", "", 0, 0, "", (0, 0, 0))

        self.show()
        self.reset_coo()
        self.loop()


    def loop(self):
        self.go_on = True

        while self.go_on:

            if len(self.detection.media_pipe.hand_points) > 0:
                self.right_x = int(self.detection.media_pipe.hand_points[0][0])
                self.right_y = int(self.detection.media_pipe.hand_points[0][1])

            for x, y in self.detection.media_pipe.hand_points:
                self.stage.test_collision(x, y)
            self.stage.test_collision(self.right_x, self.right_y)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.go_on = False
                        pygame.mixer.music.stop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.media_pipe.is_fist_closed = 1

            self.stage.update_targets()
            self.stage.play()
            self.show_hand()


            if self.stage.is_end():
                self.detection.full_detection = False
                self.stage.save_best_score()
                pygame.mixer.music.stop()
                EndInterface(self.screen_data, self.screen, self.detection, self.settings, self)

            if self.detection.media_pipe.is_fist_closed == 1:
                if self.pause_button.x < self.right_x < (self.pause_button.x + self.pause_button.width) and \
                        self.pause_button.y < self.right_y < (self.pause_button.y + self.pause_button.height):
                    self.stage.pause()
                    self.detection.full_detection = False
                    PauseInterface(self.screen_data, self.screen, self.detection, self.settings, self)
                    self.detection.full_detection = True
                    self.stage.resume()
                    self.reset_coo()
                    self.detection.media_pipe.hand_points.clear()
                    self.show()

        self.detection.full_detection = False


    def show_hand(self):
        self.show()
        if len(self.detection.media_pipe.hand_points) > 0:
            pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.media_pipe.hand_points[0][0] - 10,
                                                              self.detection.media_pipe.hand_points[0][1] - 10), 20)
        pygame.display.update()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.pause_button.show_button()
        self.stage.show_targets()
        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 80)
        text_surface = my_font.render("score: " + str(self.stage.score), True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(text_surface, (self.screen_width / 2 - 200, 30))

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.leftX = 0
        self.leftY = 0