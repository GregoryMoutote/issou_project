import pygame.draw

from Buttons import CheckButton
from Interfaces.Interface import *
from Buttons.TimelineButton import *
from Buttons.CheckButton import *
from Buttons.MenuLevelCreationButton import *
from Targets.Target import *
from Model.Constants import *
from Model.Stage.StageCreator import StageCreator
from Buttons.InputCreationLevelButton import *
import time
import os
import easygui
import shutil

class LevelCreationSecondInterface(Interface):

    def __init__(self,screen_data,screen, detection, settings, stage_name, illustration_path, background_path, music_path):
        self.settings = settings
        self.detection = detection

        super().__init__(screen_data, screen)

        self.is_selected_target=False
        self.selected_picture=None
        self.selected_picture_name=None
        self.last_click=time.time()

        self.stage=StageCreator(self.screen,stage_name, illustration_path, background_path, music_path,settings)
        if not self.stage.is_usable:
            return

        self.play_button = CheckButton(self.screen_width * 0.05, self.screen_height * 0.82,
                                       self.screen_height * 0.1, self.screen_height * 0.1, self.screen,
                                       "levelCreationPlay.png", "levelCreationPause.png", True)

        self.import_delete_button = CheckButton(self.screen_width * 0.8, self.screen_height * 0.8,
                                                self.screen_width * 0.2, self.screen_height * 0.1, self.screen,
                                                "importButton.png", "deleteButton.png", True)

        self.timeline = TimelineButton(self.screen_width * 0.05, self.screen_height * 0.95,
                                       self.screen_width * 0.9, self.screen_height * 0.02,
                                       self.screen, "timelineGray.png", "timelineRed.png")

        self.inputValueTarget= InputCreationLevelButton(self.screen_width * 0.6, self.screen_height * 0.81,
                                                self.screen_width * 0.18, self.screen_height * 0.1, self.screen,
                                                 15,"Arial.ttf",(255,255,255),"Valeur",20)

        self.inputDurationTarget= InputCreationLevelButton(self.screen_width * 0.4, self.screen_height * 0.81,
                                                self.screen_width * 0.18, self.screen_height * 0.1, self.screen,
                                                 5,"Arial.ttf",(255,255,255),"Durée d'apparition",20)


        self.basic_targets_list = []
        self.import_targets_list = []

        i = 1
        for file in os.listdir("Pictures/Targets"):
            if file != "Transparent":
                self.basic_targets_list.append(MenuLevelCreationButton(self.screen_width * 0.8,
                                                                       self.screen_height * 0.1 * i,
                                                                       self.screen_width * 0.1,
                                                                       Constants.TARGET_RADIUS * 1.6,
                                                                       self.screen, file, file[6:-4], 35, 10,
                                                                       "arial.ttf", (255, 255, 255),""))
                i += 1

        self.newScreen()
        self.reset_coo()
        self.loop()


    def loop(self):
        go_on=True

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
                    if event.key == pygame.K_SPACE:
                        self.timeline.change_stat(self.timeline.percent + 1)
                    if event.key == pygame.K_ESCAPE:
                        shutil.rmtree("Stages/"+self.stage.stage_name)
                        go_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.is_fist_closed = 1

            self.show_hand()
            print(len(self.stage.stage.active_targets))

            if self.detection.is_fist_closed == 1:
                #bouton play
                if self.play_button.x < self.right_x < (self.play_button.x + self.play_button.width) and \
                        self.play_button.y < self.right_y < (self.play_button.y + self.play_button.height):
                    self.play_button.change_stat()
                    self.reset_coo()
                    self.newScreen()

                #bouton input
                if self.inputValueTarget.x < self.right_x < (self.inputValueTarget.x + self.inputValueTarget.width) and \
                        self.inputValueTarget.y < self.right_y < (self.inputValueTarget.y + self.inputValueTarget.height):
                    self.inputValueTarget.click(self.right_x)
                    self.reset_coo()
                    self.show()

                if self.inputDurationTarget.x < self.right_x < (self.inputDurationTarget.x + self.inputDurationTarget.width) and \
                        self.inputDurationTarget.y < self.right_y < (self.inputDurationTarget.y + self.inputDurationTarget.height):
                    self.inputDurationTarget.click(self.right_x)
                    self.reset_coo()
                    self.show()

                #gestion du bouton d'import et de suppression
                elif self.import_delete_button.x < self.right_x < (self.import_delete_button.x + self.import_delete_button.width) and \
                        self.import_delete_button.y < self.right_y < (self.import_delete_button.y + self.import_delete_button.height):
                    if self.is_selected_target:#suppression
                        self.import_delete_button.active=True
                        self.stage.remove_traget()
                        self.delete()
                        self.inputDurationTarget.show_input_value=False
                        self.inputValueTarget.show_input_value=False
                    else:#import
                        self.import_delete_button.active = False
                        target= easygui.fileopenbox(title="Chosir une cible",default='*.png')
                        if target is not None:
                            self.stage.add_special_target(target)
                            while target.find("\\") != -1:
                                target = target[target.find("\\") + 1:]
                            if(len(self.import_targets_list)==0):
                                self.import_targets_list.append(MenuLevelCreationButton(self.screen_width * 0.9,
                                                                    self.screen_height * 0.1,
                                                                    self.screen_width * 0.1,
                                                                    Constants.TARGET_RADIUS * 1.6,
                                                                    self.screen, target, target[:-4], 35, 10,
                                                                    "arial.ttf", (255, 255, 255),self.stage.stage_name))
                            else:
                                self.import_targets_list.append(MenuLevelCreationButton(self.screen_width * 0.9,
                                                                                       self.screen_height * 0.1 *(len(self.import_targets_list)+1),
                                                                                       self.screen_width * 0.1,
                                                                                       Constants.TARGET_RADIUS * 1.6,
                                                                                       self.screen, target,target[:-4], 35, 10,
                                                                                       "arial.ttf",
                                                                                       (255, 255, 255),self.stage.stage_name))
                        self.newScreen()
                    self.reset_coo()
                    self.show()

                #placer les cibles
                elif Constants.TARGET_RADIUS < self.right_x < self.screen_width*0.8-Constants.TARGET_RADIUS and \
                        Constants.TARGET_RADIUS < self.right_y < self.screen_height * 0.8 - Constants.TARGET_RADIUS:

                    self.inputDurationTarget.show_input_value = True
                    self.inputValueTarget.show_input_value = True

                    if self.is_selected_target and time.time() - self.last_click > 1:
                        if self.stage.active_target_index!=-1:
                            self.stage.targets[self.stage.targets_index].x = self.right_x
                            self.stage.targets[self.stage.targets_index].y = self.right_y

                        else:
                            self.stage.add_target(Target([0, ((self.right_x) / (self.screen_width * 0.8)) * 0.8,
                                                          ((self.right_y) / (self.screen_height * 0.8)) * 0.8, 10,
                                                          self.timeline.percent * self.stage.stage.stage_music.duration, 25,
                                                         self.selected_picture_name], self.screen, self.stage.stage_name))
                    self.last_click = time.time()
                    self.is_selected_target = False
                    self.import_delete_button.active = True
                    self.reset_coo()
                    self.show()
                    self.stage.stage.play()


                elif self.screen_width * 0.05<self.right_x<self.screen_width*0.95 and self.screen_height*0.95<self.right_y<self.screen_height*0.97:
                    self.timeline.change_stat((self.right_x-self.screen_width * 0.05)/(self.screen_width*0.9))
                    self.reset_coo()

                #choix d'un nouveau type de cible
                for target in self.basic_targets_list:
                    if target.x < self.right_x < (target.x + target.width) and \
                            target.y < self.right_y < (target.y + target.height):
                        self.selected_picture = target.picture
                        self.selected_picture_name=target.picture_name
                        self.is_selected_target = True
                        self.import_delete_button.active = False

                #choix d'un nouveau type de cible importé
                for target in self.import_targets_list:
                    if target.x < self.right_x < (target.x + target.width) and \
                            target.y < self.right_y < (target.y + target.height):
                        self.selected_picture = target.picture
                        self.selected_picture_name=target.picture_name
                        self.is_selected_target = True
                        self.import_delete_button.active = False

                #déplacement de cible
                for target in self.stage.stage.active_targets:
                    if target[0].coordinates.x < self.right_x < (target[0].coordinates.x + Constants.TARGET_RADIUS*2) and \
                       target[0].coordinates.y < self.right_y < (target[0].coordinates.y + Constants.TARGET_RADIUS*2):
                        print("test:" + str(target[0].coordinates) + "  " + str(self.right_x) + "   " + str(self.right_y))

                        if(time.time()-self.last_click>1):
                            self.last_click=time.time()
                            self.is_selected_target = True

                            if os.path.isfile("Pictures/Targets/" + str(target.pictureName)):
                                picture = pygame.image.load("Pictures/Targets/" + str(target.pictureName))

                            elif os.path.isfile("Stages/" + self.stage.stage_name + "/specialTargets/" + target.pictureName):
                                picture = pygame.image.load("Stages/" + self.stage.stage_name + "/specialTargets/" + target.pictureName)

                            self.selected_picture = pygame.transform.scale(picture, (Constants.TARGET_RADIUS * 0.8,
                                                                                  Constants.TARGET_RADIUS * 0.8))
                            self.selected_picture_name = target.pictureName
                            self.stage.set_target_to_modify(self.right_x,self.right_y)
                            self.import_delete_button.active =not self.is_selected_target
                            self.show()
                            print("déplacer")


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.import_delete_button.show_button()

        for target,delay in self.stage.stage.active_targets:
            if (target != None and len(self.stage.stage.active_targets)>self.stage.active_target_index>=0 and target!=self.stage.stage.active_targets[self.stage.active_target_index][0]) or self.stage.active_target_index==-1:
                target.show_target()

        if self.is_selected_target:
            self.screen.blit(self.selected_picture, (self.right_x - Constants.TARGET_RADIUS * 0.8,
                                                     self.right_y - Constants.TARGET_RADIUS * 0.8))
        self.inputValueTarget.show_value()
        self.inputDurationTarget.show_value()
        self.timeline.show_button()


    def show_hand(self):
        self.show()
        if len(self.detection.left_hand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.left_x - 5, self.left_y - 5), 10)

        if len(self.detection.right_hand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.right_x - 5, self.right_y - 5), 10)
        pygame.display.update()

    def newScreen(self):
        background = pygame.image.load("./Stages/"+self.stage.stage_name+"/background."+self.stage.background_path)
        background = pygame.transform.scale(background, (self.screen_width * 0.80 + 1,self.screen_height * 0.80 + 1))
        self.screen.blit(background, (0, 0))

        bottom_menu = pygame.image.load("./Pictures/Interfaces/menuBackground.png")
        bottom_menu = pygame.transform.scale(bottom_menu, (self.screen_width * 0.20, self.screen_height))
        self.screen.blit(bottom_menu, (self.screen_width * 0.8, 0))

        right_menu = pygame.image.load("./Pictures/Interfaces/menuBackground.png")
        right_menu = pygame.transform.scale(right_menu, (self.screen_width,self.screen_height * 0.20))
        self.screen.blit(right_menu, (0, self.screen_height * 0.8))

        self.play_button.show_button()
        self.inputValueTarget.show_button()
        self.inputDurationTarget.show_button()

        for target in self.basic_targets_list:
            target.show_button()
        for target in self.import_targets_list:
            target.show_button()

        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/arial.ttf", 40)
        text_surface = my_font.render("Choix des cibles", True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(text_surface, (self.screen_width * 0.80, self.screen_height * 0.02))

        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")
        self.show()

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.left_x = 0
        self.left_y = 0

    def delete(self):
        self.is_selected_target = False
        self.selected_picture = None
        self.selected_picture_name = None