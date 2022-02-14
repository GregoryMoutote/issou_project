import pygame.draw

from Buttons.PictureButton import *
from Interfaces.SettingsInterface import *
from Interfaces.Interface import *

class EndInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings, parent):
        self.parent = parent
        self.settings = settings
        self.detection = detection

        super().__init__(screen_data, screen)

        self.parent.stage.save_best_score()

        self.buttons=[PictureButton(self.screen_width*0.375, self.screen_height*0.55, self.screen_width*0.25, self.screen_height*0.09,
                                    self.screen, "button2.png", "REDEMARRER", 0.5, "Glitch.otf", (255, 255, 255))]
        self.buttons.append(PictureButton(self.screen_width*0.375, self.screen_height*0.65, self.screen_width*0.25, self.screen_height*0.09,
                                          self.screen, "button2.png", "QUITTER", 0.5, "Glitch.otf", (255, 255, 255)))

        self.newScreen()
        self.reset_coo()
        self.loop()


    def loop(self):
        go_on = True

        while go_on:
            self.detection.hand_detection()

            if len(self.detection.right_hand) > 0:
                self.right_x = self.detection.right_hand[0]
                self.right_y = self.detection.right_hand[1]

            if len(self.detection.left_hand) > 0:
                self.leftX = self.detection.left_hand[0]
                self.leftY = self.detection.left_hand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.parent.go_on = False
                        go_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.is_fist_closed = 1

            self.show_hand()

            if self.detection.is_fist_closed == 1:
                if self.buttons[0].x < self.right_x < (self.buttons[0].x + self.buttons[0].width) and \
                        self.buttons[0].y < self.right_y < (self.buttons[0].y + self.buttons[0].height):
                    self.parent.stage.load()
                    self.reset_coo()
                    self.show()
                    go_on = False
                    self.parent.detection.full_detection = True

                elif self.buttons[1].x < self.right_x < (self.buttons[1].x + self.buttons[1].width) and \
                        self.buttons[1].y < self.right_y < (self.buttons[1].y + self.buttons[1].height):
                    self.parent.go_on = False
                    go_on = False

    def show(self):
        self.screen.blit(self.background, (0, 0))

    def show_hand(self):
        #self.parent.show()
        self.show()
        if len(self.detection.left_hand) > 0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX - 5, self.leftY - 5), 10)

        if len(self.detection.right_hand) > 0:
            pygame.draw.circle(self.screen, (255, 255, 255), (self.right_x - 5, self.right_y - 5), 10)
        pygame.display.update()

    def newScreen(self):
        background = pygame.image.load("./Pictures/Interfaces/parameterBackground.png")
        background = pygame.transform.scale(background, (self.screen_width*0.30, self.screen_height*0.55))
        self.screen.blit(background, (self.screen_width*0.35, self.screen_height*0.225))
        for button in self.buttons:
            button.show_button()
        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 120)
        my_font2 = pygame.font.Font("./Fonts/lemonmilk.otf", 50)
        my_font3=pygame.font.Font("./Fonts/lemonmilk.otf", 40)
        my_font4 = pygame.font.Font("./Fonts/lemonmilk.otf", 30)
        text_surface = my_font2.render("Fin du niveau", True, (255, 255, 255))
        text_score=my_font3.render("Votre score est:", True, (255, 255, 255))
        score = my_font.render(str(self.parent.stage.score), True, (255, 255, 255))
        text_best_score = my_font4.render("Votre meilleur score est: "+str(self.parent.stage.best_score), True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(text_surface, ((self.screen_width-text_surface.get_width())*0.5, self.screen_height / 2 - 270))
        self.screen.blit(text_score, ((self.screen_width-text_score.get_width())*0.5, self.screen_height / 2 - 200))
        self.screen.blit(score, ((self.screen_width-score.get_width())*0.5, self.screen_height / 2 - 175))
        self.screen.blit(text_best_score, ((self.screen_width-text_best_score.get_width())*0.5, self.screen_height / 2))
        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")
        self.show()

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.leftX = 0
        self.leftY = 0