import pygame.draw

from Interfaces.PlayInterface import *
from Model.Stage.Level import *
from random import *
from Model.Stage.Stage import *
import os

class Level_Selection_Interface(Interface):

    def __init__(self, screen_data, screen, detection, settings):
        self.detection = detection
        self.settings = settings
        self.stages = []
        self.index = 2

        super().__init__(screen_data, screen)
        self.pre_load_all_stages()

        self.background = pygame.image.load("./Pictures/Interfaces/levelSelectionBackground.png")

        self.levels = []
        for stage in self.stages:
            self.levels.append(Level(stage.name, 3, stage.name, stage.stage_music.description,
                                     stage.difficulty, stage.stage_music.duration))

        self.random_button = PictureButton(self.screen_width * 0.8, self.screen_height * 0.86,
                                           self.screen_height * 0.13, self.screen_height * 0.13,
                                           self.screen, "dice.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.up_button = PictureButton(self.screen_width * 0.9, self.screen_height * 0.86,
                                       self.screen_height * 0.13, self.screen_height * 0.13,
                                       self.screen, "arrowUp.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.down_button = PictureButton(self.screen_width * 0.7, self.screen_height * 0.86,
                                         self.screen_height * 0.13, self.screen_height * 0.13,
                                         self.screen, "arrowDown.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.quit_button = PictureButton(0, self.screen_height * 0.9, self.screen_width * 0.25,
                                         self.screen_height * 0.08, self.screen, "button1.png", "retour",
                                         50, 50, "Glitch.otf", (255, 255, 255))
        self.play_button = PictureButton(self.screen_width / 5, self.screen_height / 2 - 100, 200, 200,
                                         self.screen, "play.png", "", 0, 0, "", (0, 0, 0))

        self.show()
        self.reset_coo()
        self.loop()


    def loop(self):
        go_on = True

        while go_on:


            if len(self.detection.media_pipe.right_hand) > 0:
                self.right_x = self.detection.media_pipe.right_hand[0]
                self.right_y = self.detection.media_pipe.right_hand[1]

            if len(self.detection.media_pipe.left_hand) > 0:
                self.left_x = self.detection.media_pipe.left_hand[0]
                self.left_y = self.detection.media_pipe.left_hand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        go_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.media_pipe.is_fist_closed = 1

            self.show_hand()

            if self.detection.media_pipe.is_fist_closed == 1:
                if self.quit_button.x < self.right_x < (self.quit_button.x + self.quit_button.width) and \
                        self.quit_button.y < self.right_y < (self.quit_button.y + self.quit_button.height):
                   go_on = False

                elif self.play_button.x < self.right_x < (self.play_button.x + self.play_button.width) and \
                        self.play_button.y < self.right_y < (self.play_button.y + self.play_button.height):
                    PlayInterface(self.screen_data, self.screen, self.detection, self.settings, self.stages[self.index])
                    self.show()
                    self.reset_coo()

                elif self.down_button.x < self.right_x < (self.down_button.x + self.down_button.width) and \
                        self.down_button.y < self.right_y < (self.down_button.y + self.down_button.height):
                    self.levels.append(self.levels[0])
                    del self.levels[0]
                    self.show()
                    self.reset_coo()
                    if self.index == len(self.levels) - 1:
                        self.index = 0
                    else:
                        self.index += 1

                elif self.up_button.x < self.right_x < (self.up_button.x + self.up_button.width) and \
                        self.up_button.y < self.right_y < (self.up_button.y + self.up_button.height):
                    self.levels.insert(0, self.levels[len(self.levels) - 1])
                    del self.levels[len(self.levels) - 1]
                    self.show()
                    self.reset_coo()
                    if self.index == 0:
                        self.index = len(self.levels) - 1
                    else:
                        self.index -= 1

                elif self.random_button.x < self.right_x < (self.random_button.x + self.random_button.width) and \
                        self.random_button.y < self.right_y < (self.random_button.y + self.random_button.height):
                    for i in range(0, int(random() * len(self.levels))):
                        self.levels.append(self.levels[0])
                        del self.levels[0]
                        if self.index == len(self.levels) - 1:
                            self.index = 0
                        else:
                            self.index += 1
                    self.reset_coo()
                    self.show()


    def show_description(self, name, picture, difficulty, description, duration, nbStars):

        self.banner_top_picture = pygame.image.load("./Pictures/Interfaces/bannerTop.png")
        self.banner_top_picture = pygame.transform.scale(self.banner_top_picture, (self.screen_width, self.screen_height / 4.5))
        self.screen.blit(self.banner_top_picture, (0, 0))

        self.music_picture = pygame.image.load("Stages/" + picture + "/" + picture + ".png")
        self.music_picture = pygame.transform.scale(self.music_picture, (self.screen_height / 5 - 20, self.screen_height / 5 - 20))
        self.screen.blit(self.music_picture, (10, 10))

        self.star_unchecked = pygame.image.load("./Pictures/Interfaces/starUnchecked.png")
        self.star_unchecked = pygame.transform.scale(self.star_unchecked, (60, 60))

        self.star_checked = pygame.image.load("./Pictures/Interfaces/starChecked.png")
        self.star_checked = pygame.transform.scale(self.star_checked, (60, 60))

        for i in range(0,5):
            if i < nbStars :
                self.screen.blit(self.star_checked, (self.screen_width * 0.75 + 70 * i, 10))
            else:
                self.screen.blit(self.star_unchecked, (self.screen_width * 0.75 + 70 * i, 10))

        pygame.font.init()
        font_glitch=pygame.font.Font("./Fonts/Glitch.otf",70)
        font_arial=pygame.font.Font("./Fonts/Arial.ttf",30)
        font_big_arial = pygame.font.Font("./Fonts/Arial.ttf", 40)

        if len(name) > 15:
            name = name[0:15] + "..."

        self.title = font_glitch.render(name, True, (255, 255, 255))
        self.screen.blit(self.title, (self.screen_height / 5, 10))

        if difficulty == 0:
            self.difficulty = font_big_arial.render("EASY", True, (0, 255, 0))
        elif difficulty == 1:
            self.difficulty = font_big_arial.render("MEDIUM", True, (255, 128, 0))
        else:
            self.difficulty = font_big_arial.render("HARD", True, (255, 0, 0))
        self.screen.blit(self.difficulty, (self.screen_width * 0.64, 25))

        for i in range(0, len(description), 80):
            text = font_arial.render(description[i:i + 80], True, (255, 255, 255))
            if i == 0:
                self.screen.blit(text, (self.screen_height / 5, 70, 1000, 100))
            elif i == 80:
                self.screen.blit(text, (self.screen_height / 5, 100, 1000, 100))
            else:
                self.screen.blit(text, (self.screen_height / 5, 130, 1000, 100))

        min = str(int(duration / 60))
        sec = str(int(duration % 60))

        duration_text = font_big_arial.render("Durée: " + min + ":" + sec, True, (255, 255, 255))
        self.screen.blit(duration_text, (self.screen_width / 5 * 4.2, self.screen_height / 10))
        pygame.font.quit()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.play_button.show_button()

        if len(self.levels) > 5 :
            for i in range(0, 6):
                if i == 2:
                    self.levels[i].show(self.screen, self.screen_width * 0.60, self.screen_height * 0.164 * i,
                                        self.screen_width * 0.40, self.screen_height * 0.167)
                else:
                    self.levels[i].show(self.screen, self.screen_width * 0.65, self.screen_height * 0.164 * i,
                                        self.screen_width * 0.35, self.screen_height * 0.167)
        else:
            for i in range(0, len(self.levels)):
                if i == 2:
                    self.levels[i].show(self.screen, self.screen_width * 0.60, self.screen_height * 0.164 * i,
                                        self.screen_width * 0.40, self.screen_height * 0.167)
                else:
                    self.levels[i].show(self.screen, self.screen_width * 0.65, self.screen_height * 0.164 * i,
                                        self.screen_width * 0.35, self.screen_height * 0.167)

        if len(self.levels) > 2:
            self.show_description(self.levels[2].name, self.levels[2].picture, self.levels[2].difficulty,
                                  self.levels[2].description, self.levels[2].duration, self.levels[2].mark)

        self.up_button.show_button()
        self.down_button.show_button()
        self.quit_button.show_button()
        self.random_button.show_button()


    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.left_x = 0
        self.left_y = 0


    def show_hand(self):
        self.show()
        if len(self.detection.media_pipe.left_hand) > 0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.left_x - 5, self.left_y - 5), 10)

        if len(self.detection.media_pipe.right_hand) > 0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.right_x - 5, self.right_y - 5), 10)
        pygame.display.update()

    def pre_load_all_stages(self):
        self.file = os.listdir("Stages")
        for file in self.file:
            self.stages.append(Stage("Stages/" + file + "/" + file + ".issou", self.screen))
