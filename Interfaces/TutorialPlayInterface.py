import pygame.draw,threading

from Interfaces.EndInterface import *
from Model.Stage.Stage import Stage
import time

class TutorialPlayInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings):

        self.stage = Stage("TutorialStage/tutorial/tutorial.issou", screen, False, settings)
        self.settings = settings
        self.detection = detection
        super().__init__(screen_data, screen)

        self.stage.pre_load_stage()
        self.stage.load()

        self.newScreen()
        self.reset_coo()

        self.thread = PlayInterfaceThread(screen,self.stage,detection,self)  # crée le thread
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

    def newScreen(self):
        background = pygame.image.load("./TutorialStage/" + self.stage.name + "/background.png")
        background = pygame.transform.scale(background, (width, height))
        self.screen.blit(background, (0, 0))
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
        self.screen=screen
        self.stage=stage
        self.detection=detection
        self.interface=interface
        self.continuer=True

        self.messages = ["", "Passez votre main au dessus de la cible", "", "Cette fois-ci la cible bouge !", "",
                         "Celle ci vous demande de la réactivité si vous voulez un maximum de point !", "",
                         "Pour celle-ce il faut suivre la route", "", ""]

        self.number_of_active_targets = 0

    def end(self):
        self.continuer = False

    def run(self):
        pygame.font.init()
        self.my_score_font = pygame.font.Font("./Fonts/lemonmilk.otf", 80)
        self.my_font = pygame.font.Font("./Fonts/Arial.ttf", 50)
        while (self.continuer):
            self.screen.blit(self.background, (0, 0))
            self.stage.show_targets()

            if len(self.stage.active_targets) != self.number_of_active_targets :
                self.number_of_active_targets = len(self.stage.active_targets)
                self.messages.pop(0)

            text_surface = self.my_score_font.render("score: " + str(self.stage.score), True, (255, 255, 255))
            message_surface = self.my_font.render(self.messages[0], True, (255, 255, 255))

            self.screen.blit(text_surface, ((self.interface.screen_width - text_surface.get_width()) * 0.5, 30))
            self.screen.blit(message_surface, ((self.interface.screen_width - message_surface.get_width()) * 0.5, 150))

            if len(self.detection.right_hand) > 0:
                pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.right_hand[0] - 10,
                                                                  self.detection.right_hand[1] - 10), 20)
            pygame.display.update()
        del self.my_font
        pygame.font.quit()