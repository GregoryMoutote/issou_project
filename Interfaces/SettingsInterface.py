import pygame.draw

from Buttons.ColorButton import *
from Buttons.MultipleButton import *
from Interfaces.CalibrationInterface import *

class SettingsInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings):
        self.settings = settings
        self.detection = detection

        super().__init__(screen_data, screen)

        self.background = pygame.image.load("./Pictures/Interfaces/fond.png")
        self.background_logo = pygame.image.load("./Pictures/Interfaces/fondLogo.png")

        self.buttons = [(ColorButton(100, self.screen_height / 2 + 120, self.screen_width * 0.85, 70, self.screen,
                                     (0, 172, 240), "Recalibrer", 50, self.screen_width * 0.5 - 230,
                                    "Arial.ttf", (255, 255, 255)))]
        self.buttons.append(ColorButton(100, self.screen_height / 2 + 190, self.screen_width * 0.85, 70, self.screen,
                                        (0, 112, 192), "Aide", 50, self.screen_width * 0.5 - 180,
                                       "Arial.ttf", (255, 255, 255)))
        self.buttons.append(ColorButton(100, self.screen_height / 2 + 260, self.screen_width * 0.85, 70, self.screen,
                                        (120, 120, 120), "Quitter", 50, self.screen_width * 0.5 - 180,
                                       "Arial.ttf", (255, 255, 255)))

        self.volume_button = MultipleButton(225, self.screen_height / 2 - 217, 1350, 100, self.screen,
                                           "soundOn.png", "soundOff.png", 10, self.settings.volume)

        if self.settings.volume == 0:
            self.mute_button = CheckButton(100, self.screen_height / 2 - 217, 100, 100, self.screen,
                                          "SoundMute.png", "SoundActive.png", True)
        else:
            self.mute_button = CheckButton(100, self.screen_height / 2 - 217, 100, 100, self.screen,
                                          "SoundMute.png", "SoundActive.png", False)

        self.animation_button = CheckButton(700, self.screen_height / 2 - 92, 100, 100, self.screen,
                                           "checkedOn.png", "checkedOff.png", self.settings.animation)

        self.reset_coo()
        self.loop()


    def loop(self):
        go_on = True

        while go_on:


            if len(self.detection.media_pipe.right_hand) > 0:
                self.right_x = self.detection.media_pipe.right_hand[0]
                self.right_y = self.detection.media_pipe.right_hand[1]

            if len(self.detection.media_pipe.left_hand) > 0:
                self.leftX = self.detection.media_pipe.left_hand[0]
                self.leftY = self.detection.media_pipe.left_hand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        go_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.media_pipe.is_fist_closed = 1

            self.show_hand()

            if self.detection.media_pipe.is_fist_closed == 1:
                if self.animation_button.x < self.right_x < (self.animation_button.x + self.animation_button.width) and \
                        self.animation_button.y < self.right_y < (self.animation_button.y + self.animation_button.height):
                    self.settings.animation = self.animation_button.change_stat()
                    self.reset_coo()

                elif self.mute_button.x < self.right_x < (self.mute_button.x + self.mute_button.width) and \
                        self.mute_button.y < self.right_y < (self.mute_button.y + self.mute_button.height):
                    self.mute_button.change_stat()

                    if self.mute_button.active :
                        self.settings.set_volume(0)
                        self.volume_button.change_stat(0)
                    else:
                        self.settings.set_volume(1)
                        self.volume_button.change_stat(1)
                    self.reset_coo()

                elif self.buttons[0].x < self.right_x < (self.buttons[0].x + self.buttons[0].width) and \
                        self.buttons[0].y < self.right_y < (self.buttons[0].y + self.buttons[0].height):
                    CalibrationInterface(self.screen_data, self.screen, self.detection)
                    self.reset_coo()
                    self.show()

                elif (self.buttons[2].x) < self.right_x < (self.buttons[2].x + self.buttons[2].width) and \
                        (self.buttons[2].y) < self.right_y < (self.buttons[2].y + self.buttons[2].height):
                    self.settings.save_change()
                    go_on = False

                for i in range(0, self.volume_button.nb_button):
                    if self.volume_button.check[i].x < self.right_x < (self.volume_button.check[i].x + self.volume_button.check[i].width) and \
                            self.volume_button.check[i].y < self.right_y < (self.volume_button.check[i].y + self.volume_button.check[i].height):
                        self.volume_button.change_stat(i + 1)
                        self.settings.set_volume(i + 1)
                        if(self.mute_button.active == True):
                            self.mute_button.change_stat()

    def show(self):
        pygame.font.init()
        font_glitch = pygame.font.Font("./Fonts/Glitch.otf", 100)
        font_arial = pygame.font.Font("./Fonts/Arial.ttf", 56)

        text = font_glitch.render("OPTIONS", True, (255, 255, 255))
        text2 = font_arial.render("Activer les animations", True, (255, 255, 255))
        pygame.font.quit()

        self.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.show_button()

        self.screen.blit(text, (self.screen_width / 2 - 250, self.screen_height / 2 - 350))
        self.screen.blit(text2, (100, self.screen_height / 2 - 75))

        # text = font_arial.render("Volume", True, (255, 255, 255))
        # self.screen.blit(text, (100, self.screenHeight / 2 - 200))

        self.volume_button.show_button()
        self.mute_button.show_button()
        self.animation_button.show_button()


    def show_hand(self):
        self.show()
        if len(self.detection.media_pipe.left_hand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.media_pipe.right_hand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.right_x - 5, self.right_y - 5), 10)
        pygame.display.update()


    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.leftX = 0
        self.leftY = 0