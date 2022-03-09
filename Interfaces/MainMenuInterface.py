import pygame.draw

from Interfaces.LevelSelectionInterface import *
from Interfaces.SettingsInterface import *
from Interfaces.GIF.MainMenuGIF import *
from Interfaces.LevelCreationFirstInterface import *

class MainMenuInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings):
        self.settings = settings
        self.detection = detection

        super().__init__(screen_data, screen)

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("ISSOU")
        self.moving_sprites = pygame.sprite.Group()
        ISSOU_laod = MenuGIF(self.screen_width * 0.17, self.screen_height / 2 - 75, self.screen)
        self.moving_sprites.add(ISSOU_laod)

        self.buttons = [ColorButton(self.screen_width * 0.4, self.screen_height * 0.25, self.screen_width / 2,
                                    self.screen_height * 0.1, self.screen, (20, 40, 80), "JOUER", 0.7,
                                    "Glitch.otf", (65,105,225))]
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.35, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (14, 70, 140), "TUTORIEL", 0.7,
                                        "Glitch.otf", (65,105,225)))
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.45, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (20, 40, 80), "PARAMETRE", 0.7,
                                        "Glitch.otf", (65,105,225)))
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.55, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (14, 70, 140), "CREER UN NIVEAU",
                                        0.7, "Glitch.otf", (65,105,225)))
        self.buttons.append(ColorButton(self.screen_width * 0.4, self.screen_height * 0.65, self.screen_width / 2,
                                        self.screen_height * 0.1, self.screen, (20, 40, 80), "QUITTER", 0.7,
                                        "Glitch.otf",(65,105,225)))

        self.newScreen()
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
                   LevelSelectionInterface(self.screen_data, self.screen, self.detection, self.settings)

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
                    popup = PopupInterface(self.screen_data,self.screen,self.detection,self.settings,self,"Information","Voulez vous quitter ?")
                    popup.set_return(0,False)
                    popup.set_button_text(0,"Oui")
                    popup.add_button("Non",False)

                    go_on = popup.start()
                    self.reset_coo()
                    self.show()


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
        background=pygame.image.load("./Pictures/Interfaces/background.jpg")
        background=pygame.transform.scale(background, (self.screen_width, self.screen_height))
        self.screen.blit(background, (0, 0))
        for button in self.buttons:
            button.show_button()
        fond_logo = pygame.image.load("./Pictures/Interfaces/fondLogo.png")
        fond_logo = pygame.transform.scale(fond_logo, (self.screen_height * 0.5 * 1.57, self.screen_height * 0.5))
        self.screen.blit(fond_logo, (self.screen_width * 0.10, self.screen_height * 0.25))
        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")
        self.show()

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.left_x = 0
        self.left_y = 0
