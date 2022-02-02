import pygame.draw

from Interfaces.Level_Selection_Interface import *
from Interfaces.SettingsInterface import *
from Interfaces.GIF.MainMenuGIF import *
from PlayerDetection.MediapipeThread import *
from Interfaces.LevelCreationFirstInterface import *
import math
from Interfaces.RefreshThread import *

class MainMenuInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings):
        self.settings = settings

        super().__init__(screen_data, screen)

        self.background = pygame.image.load("./Pictures/Interfaces/fond.png")

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("ISSOU")
        self.moving_sprites = pygame.sprite.Group()
        ISSOU_laod = MenuGIF(self.screen_width * 0.17, self.screen_height / 2 - 75, self.screen)
        self.moving_sprites.add(ISSOU_laod)

        self.fond_logo = pygame.image.load("./Pictures/Interfaces/fondLogo.png")
        self.fond_logo = pygame.transform.scale(self.fond_logo, (self.screen_height * 0.5 * 1.57, self.screen_height * 0.5))

        self.buttons = [ColorButton(self.screen_width * 0.4, self.screen_height * 0.25, self.screen_width / 2,
                                    self.screen_height * 0.1, self.screen, (20, 40, 80), "JOUER", 50, 450,
                                    "Glitch.otf", (65,105,225))]
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.35, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (14, 70, 140), "TUTORIEL", 50, 420,
                                        "Glitch.otf", (65,105,225)))
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.45, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (20, 40, 80), "PARAMETRE", 50, 380,
                                        "Glitch.otf", (65,105,225)))
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.55, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (14, 70, 140), "CREER UN NIVEAU",
                                        50, 300, "Glitch.otf", (65,105,225)))
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.65, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (20, 40, 80), "QUITTER", 50, 450,
                                        "Glitch.otf",(65,105,225)))

        self.detection = detection

        self.newScreen()
        self.show()
        self.reset_coo()
        self.detection.init_hand_capture()


        self.loop()

        pygame.quit()


    def loop(self):
        go_on = True

        while go_on:
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
                        go_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.is_fist_closed=1

            self.show_hand()

            if self.detection.is_fist_closed == 1:
                if self.buttons[0].x < self.right_x < (self.buttons[0].x + self.buttons[0].width) and \
                        self.buttons[0].y < self.right_y < (self.buttons[0].y + self.buttons[0].height):
                   Level_Selection_Interface(self.screen_data, self.screen, self.detection, self.settings)

                   self.reset_coo()
                   self.show()

                elif self.buttons[2].x < self.right_x < (self.buttons[2].x + self.buttons[2].width) and \
                        self.buttons[2].y < self.right_y < (self.buttons[2].y + self.buttons[2].height):
                    SettingsInterface(self.screen_data, self.screen, self.detection, self.settings)
                    self.reset_coo()
                    self.show()

                elif self.buttons[3].x < self.right_x < (self.buttons[3].x + self.buttons[3].width) and \
                        self.buttons[3].y < self.right_y < (self.buttons[3].y + self.buttons[3].height):
                    LevelCreationFirstInterface(self.screen_data, self.screen, self.detection, self.settings)
                    self.reset_coo()
                    self.show()

                elif self.buttons[4].x < self.right_x < (self.buttons[4].x + self.buttons[4].width) and \
                        self.buttons[4].y < self.right_y < (self.buttons[4].y + self.buttons[4].height):
                   go_on = False


    def show(self):
        self.screen.blit(self.background,(0,0))
        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update(1)
        self.clock.tick(60)


    def show_hand(self):
        self.show()
        if len(self.detection.left_hand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.left_x - 5, self.left_y - 5), 10)

        if len(self.detection.right_hand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.right_x - 5, self.right_y - 5), 10)
        pygame.display.update()

    def newScreen(self):
        self.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.show_button()
        self.screen.blit(self.fond_logo, (self.screen_width * 0.10, self.screen_height * 0.25))
        print("screen")
        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.left_x = 0
        self.left_y = 0
