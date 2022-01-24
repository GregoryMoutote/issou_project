import pygame.draw

from Buttons import CheckButton
from Interfaces.Interface import *
from Buttons.TimelineButton import *
from Buttons.PictureButton import *
from Buttons.CheckButton import *
from Buttons.MenuLevelCreationButton import *
from Targets.Target import *
from Model.Constants import *
import time
import os

class LevelCreationSecondInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings):
        self.settings = settings
        self.detection = detection

        super().__init__(screen_data, screen)

        self.is_selected_target=False
        self.selected_picture=None
        self.selected_picture_name=None
        self.last_click=time.time()

        self.background = pygame.image.load("./Pictures/Interfaces/levelBuilderBackground.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width * 0.80 + 1,
                                                                   self.screen_height * 0.80 + 1))

        self.right_menu = pygame.image.load("./Pictures/Interfaces/menuBackground.png")
        self.right_menu = pygame.transform.scale(self.right_menu, (self.screen_width,
                                                                   self.screen_height * 0.20))

        self.bottom_menu = pygame.image.load("./Pictures/Interfaces/menuBackground.png")
        self.bottom_menu = pygame.transform.scale(self.bottom_menu, (self.screen_width * 0.20,
                                                                     self.screen_height))

        self.play_button = CheckButton(self.screen_width * 0.05, self.screen_height * 0.82,
                                       self.screen_height * 0.1, self.screen_height * 0.1, self.screen,
                                       "levelCreationPlay.png", "levelCreationPause.png", True)
        self.fullscreen_button = CheckButton(self.screen_width * 0.26, self.screen_height * 0.82,
                                             self.screen_height * 0.1, self.screen_height * 0.1, self.screen,
                                             "maximiser.png", "minimiser.png", True)
        self.import_delete_button = CheckButton(self.screen_width * 0.8, self.screen_height * 0.8,
                                                self.screen_width * 0.2, self.screen_height * 0.1, self.screen,
                                                "deleteButton.png", "importButton.png", False)

        self.buttons = [PictureButton(self.screen_width * 0.12, self.screen_height * 0.82,
                                      self.screen_height * 0.1, self.screen_height * 0.1, self.screen,
                                       "minusTen.png", "", 0, 0, "", (255, 255, 255))]
        self.buttons.append(PictureButton(self.screen_width * 0.19, self.screen_height * 0.82,
                                          self.screen_height * 0.1, self.screen_height * 0.1, self.screen,
                                           "plusTen.png", "", 0, 0, "", (255, 255, 255)))

        self.timeline = TimelineButton(self.screen_width * 0.05, self.screen_height * 0.95,
                                       self.screen_width * 0.9, self.screen_height * 0.02,
                                       self.screen, "timelineGray.png", "timelineRed.png")

        self.placed_target = []

        self.basic_targets_list = []
        i = 1;
        for file in os.listdir("Pictures/Targets"):
            if file != "Transparent":
                self.basic_targets_list.append(MenuLevelCreationButton(self.screen_width * 0.8,
                                                                       self.screen_height * 0.1 * i,
                                                                       self.screen_width * 0.1,
                                                                       Constants.TARGET_RADIUS * 1.6,
                                                                       self.screen, file, file[6:-4], 35, 10,
                                                                       "arial.ttf", (255, 255, 255)))
                i += 1

        self.import_targets_list=[]

        self.show()
        self.reset_coo()
        self.loop()


    def loop(self):
        go_on=True

        while go_on:

            if len(self.detection.media_pipe.right_hand) > 0:
                self.right_x = self.detection.media_pipe.right_hand[0]
                self.right_y = self.detection.media_pipe.right_hand[1]

            if len(self.detection.media_pipe.left_hand) > 0:
                self.left_x = self.detection.media_pipe.left_hand[0]
                self.left_y = self.detection.media_pipe.left_hand[1]


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.timeline.change_stat(self.timeline.percent + 1)
                    if event.key == pygame.K_ESCAPE:
                        go_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.media_pipe.is_fist_closed = 1

            self.show_hand()

            if self.detection.media_pipe.is_fist_closed == 1:
                #bouton -10 sec
                if self.buttons[0].x < self.right_x < (self.buttons[0].x + self.buttons[0].width) and \
                        self.buttons[0].y < self.right_y < (self.buttons[0].y + self.buttons[0].height):
                    self.reset_coo()
                    self.show()

                # bouton +10 sec
                elif self.buttons[1].x < self.right_x < (self.buttons[1].x + self.buttons[1].width) and \
                        self.buttons[1].y < self.right_y < (self.buttons[1].y + self.buttons[1].height):
                    self.reset_coo()
                    self.show()

                #bouton play
                elif self.play_button.x < self.right_x < (self.play_button.x + self.play_button.width) and \
                        self.play_button.y < self.right_y < (self.play_button.y + self.play_button.height):
                    self.play_button.change_stat()
                    self.reset_coo()
                    self.show()

                #bouton pleine écran
                elif self.fullscreen_button.x < self.right_x < (self.fullscreen_button.x + self.fullscreen_button.width) and \
                        self.fullscreen_button.y < self.right_y < (self.fullscreen_button.y + self.fullscreen_button.height):
                    self.fullscreen_button.change_stat()
                    self.reset_coo()
                    self.show()

                #gestion du bouton d'import et de suppréssion
                elif self.import_delete_button.x < self.right_x < (self.import_delete_button.x + self.import_delete_button.width) and \
                        self.import_delete_button.y < self.right_y < (self.import_delete_button.y + self.import_delete_button.height):
                    if self.is_selected_target:
                        self.import_delete_button.active=True
                        self.delete()
                    else:
                        self.import_delete_button.active = False
                    self.reset_coo()
                    self.show()

                #placer les cibles
                elif Constants.TARGET_RADIUS < self.right_x < self.screen_width*0.8-Constants.TARGET_RADIUS and \
                        Constants.TARGET_RADIUS < self.right_y < self.screen_height * 0.8 - Constants.TARGET_RADIUS:
                    if self.is_selected_target:
                        if time.time() - self.last_click > 1:
                            self.last_click=time.time()
                            print(self.selected_picture_name[:-4])
                            self.placed_target.append(Target([0, self.right_x, self.right_y, 10, 10, 25,
                                                            self.selected_picture_name[:-4]], self.screen,
                                                           self.selected_picture_name[:-4]))
                            self.is_selected_target = False
                            self.import_delete_button.active = False
                            self.reset_coo()
                            self.show()

                #choix d'un nouveau type de cible
                for target in self.basic_targets_list:
                    if target.x < self.right_x < (target.x + target.width) and \
                            target.y < self.right_y < (target.y + target.height):
                        self.selected_picture = target.picture
                        self.selected_picture_name=target.picture_name
                        self.is_selected_target = True

                        if self.is_selected_target:
                            self.import_delete_button.active = True
                        else:
                            self.import_delete_button.active = False
                        self.show()

                #déplacement de cible
                for target in self.placed_target:
                    if target.coordinates.x < self.right_x < (target.coordinates.x + Constants.TARGET_RADIUS) and \
                            target.coordinates.y < self.right_y < (target.coordinates.y + Constants.TARGET_RADIUS):
                        if(time.time()-self.last_click>1):
                            self.last_click=time.time()
                            self.is_selected_target = True
                            picture = pygame.image.load("Pictures/Targets/" + str(target.pictureName) + ".png")
                            self.selected_picture = pygame.transform.scale(picture, (Constants.TARGET_RADIUS * 0.8,
                                                                                     Constants.TARGET_RADIUS * 0.8))
                            self.selected_picture_name = target.pictureName
                            self.placed_target.remove(target)

                            if self.is_selected_target:
                                self.import_delete_button.active = True
                            else:
                                self.import_delete_button.active = False
                            self.show()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.bottom_menu, (self.screen_width * 0.8, 0))
        self.screen.blit(self.right_menu, (0, self.screen_height * 0.8))
        self.play_button.show_button()
        self.fullscreen_button.show_button()
        self.import_delete_button.show_button()

        for button in self.buttons:
            button.show_button()
        for target in self.basic_targets_list:
            target.show_button()
        for placed in self.placed_target:
            if placed != None:
                placed.show_target()

        if self.is_selected_target:
            self.screen.blit(self.selected_picture, (self.right_x - Constants.TARGET_RADIUS * 0.8,
                                                     self.right_y - Constants.TARGET_RADIUS * 0.8))

        self.timeline.show_button()
        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/arial.ttf", 50)
        text_surface = my_font.render("Choix des cibles", True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(text_surface, (self.screen_width * 0.82, self.screen_height * 0.02))


    def show_hand(self):
        self.show()
        if len(self.detection.media_pipe.left_hand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.left_x - 5, self.left_y - 5), 10)

        if len(self.detection.media_pipe.right_hand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.right_x - 5, self.right_y - 5), 10)
        pygame.display.update()

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.left_x = 0
        self.left_y = 0

    def delete(self):
        self.is_selected_target = False
        self.selected_picture = None
        self.selected_picture_name = None