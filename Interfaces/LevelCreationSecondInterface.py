import pygame.draw

from Buttons import CheckButton
from Interfaces.Interface import *
from Buttons.TimelineButton import *
from Buttons.CheckButton import *
from Buttons.MenuLevelCreationButton import *
from Buttons.PictureButton import *
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

        self.play_button = CheckButton(self.screen_width * 0.05, self.screen_height * 0.81,
                                       self.screen_height * 0.12, self.screen_height * 0.12, self.screen,
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

        self.move_button=PictureButton(self.screen_width*0.32,self.screen_height*0.81,self.screen_height * 0.1, self.screen_height * 0.1,self.screen,"move.png","",0,"Arial.ttf",(255,255,255))


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
            #print(len(self.stage.stage.active_targets))

            if self.detection.is_fist_closed == 1:
                #bouton play
                if self.play_button.x < self.right_x < (self.play_button.x + self.play_button.width) and \
                        self.play_button.y < self.right_y < (self.play_button.y + self.play_button.height):
                    print("press play button")
                    self.play_button.change_stat()
                    self.newScreen()

                #bouton input
                if self.inputValueTarget.x < self.right_x < (self.inputValueTarget.x + self.inputValueTarget.width) and \
                        self.inputValueTarget.y < self.right_y < (self.inputValueTarget.y + self.inputValueTarget.height):
                    print("press input value target")
                    if self.stage.active_target_index != -1:
                        self.inputValueTarget.click(self.right_x)
                        self.stage.stage.active_targets[self.stage.active_target_index][0].value=self.inputValueTarget.value
                    self.show()

                elif self.inputDurationTarget.x < self.right_x < (self.inputDurationTarget.x + self.inputDurationTarget.width) and \
                        self.inputDurationTarget.y < self.right_y < (self.inputDurationTarget.y + self.inputDurationTarget.height):
                    print("press input duration target")
                    if self.stage.active_target_index!=-1:
                        self.inputDurationTarget.click(self.right_x)
                        self.stage.stage.active_targets[self.stage.active_target_index][0].duration=self.inputDurationTarget.value
                    self.show()

                elif self.screen_width * 0.05<self.right_x<self.screen_width*0.95 and self.screen_height*0.95<self.right_y<self.screen_height*0.97:
                    self.timeline.change_stat((self.right_x-self.screen_width * 0.05)/(self.screen_width*0.9))

                #déplacement
                elif self.move_button.x < self.right_x < (self.move_button.x + self.move_button.width) and \
                        self.move_button.y < self.right_y < (self.move_button.y + self.move_button.height):
                    print("move button")
                    self.move_target()

                #choix d'un nouveau type de cible
                for target in self.basic_targets_list:
                    if target.x < self.right_x < (target.x + target.width) and \
                            target.y < self.right_y < (target.y + target.height):
                        print("press choix d'un nouveau type de cible basic")
                        self.selected_picture = target.picture
                        self.selected_picture_name=target.picture_name
                        self.is_selected_target = True
                        self.import_delete_button.active = False

                #choix d'un nouveau type de cible importé
                for target in self.import_targets_list:
                    if target.x < self.right_x < (target.x + target.width) and \
                            target.y < self.right_y < (target.y + target.height):
                        print("press choix d'un nouveau type de cible import")
                        self.selected_picture = target.picture
                        self.selected_picture_name=target.picture_name
                        self.is_selected_target = True
                        self.import_delete_button.active = False

                #print("actvie target selected "+str(self.stage.active_target_index))
                #print("target selected " + str(self.stage.targets_index))
                #print(len(self.stage.stage.active_targets))

                #gestion du bouton d'import et de suppression
                self.sup_import_target()

                #sélection de cible
                self.select_target()

                #placer les cibles
                self.place_target()
                self.reset_coo()

    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.import_delete_button.show_button()

        for target,delay in self.stage.stage.active_targets:
            if (target != None and len(self.stage.stage.active_targets) > self.stage.moving_target_index >= 0 and target != self.stage.stage.active_targets[self.stage.moving_target_index][0]) or self.stage.moving_target_index==-1:
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

        self.move_button.show_button()
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
        #print("reset co")
        self.right_x = 0
        self.right_y = 0
        self.left_x = 0
        self.left_y = 0

    def delete(self):
        self.is_selected_target = False
        self.selected_picture = None
        self.selected_picture_name = None

    def select_target(self):
        for target,delay in self.stage.stage.active_targets:
            if int(target.coordinates.x - self.right_x) ** 2 + int(target.coordinates.y - self.right_y) ** 2 <= Constants.TARGET_RADIUS ** 2:
                self.stage.set_target_to_modify(self.right_x, self.right_y)
                print("select target // active target index",self.stage.active_target_index,"               target index",self.stage.targets_index)
                self.inputValueTarget.value=int(self.stage.stage.active_targets[self.stage.active_target_index][0].value)
                self.inputDurationTarget.value=int(self.stage.stage.active_targets[self.stage.active_target_index][0].duration)
                self.inputDurationTarget.show_input_value = True
                self.inputValueTarget.show_input_value = True
                self.import_delete_button.active = False
                return

        # if not self.is_selected_target:
        #     self.stage.moving_target_index=-1
        #     self.stage.active_target_index=-1
        #     self.stage.targets_index=-1

        if self.right_x < self.screen_width * 0.8 and self.right_y < self.screen_height * 0.8:
            self.inputDurationTarget.show_input_value = False
            self.inputValueTarget.show_input_value = False
            self.import_delete_button.active = True


    def move_target(self):
        # print("press deplacement de cible")
        if self.stage.active_target_index != -1:
            self.is_selected_target = True
            self.stage.moving_target_index=self.stage.active_target_index
            self.selected_picture_name = self.stage.stage.active_targets[self.stage.moving_target_index][0].pictureName
            self.selected_picture = self.stage.stage.active_targets[self.stage.moving_target_index][0].picture

            self.selected_picture = pygame.transform.scale(self.selected_picture,
                                                           (Constants.TARGET_RADIUS * 0.8,
                                                            Constants.TARGET_RADIUS * 0.8))
            self.show()


    def place_target(self):

        if Constants.TARGET_RADIUS < self.right_x < self.screen_width * 0.8 - Constants.TARGET_RADIUS and \
             Constants.TARGET_RADIUS < self.right_y < self.screen_height * 0.8 - Constants.TARGET_RADIUS and \
              self.is_selected_target and time.time() - self.last_click > 1:
            # print("press place cible")
            self.inputDurationTarget.show_input_value = True
            self.inputValueTarget.show_input_value = True

            if self.stage.moving_target_index != -1:
                #print("placé après le déplacement")
                self.stage.targets[self.stage.targets_index].coordinates.x = self.right_x
                self.stage.targets[self.stage.targets_index].coordinates.y = self.right_y
                self.stage.stage.active_targets[self.stage.moving_target_index][0].coordinates.x = self.right_x
                self.stage.stage.active_targets[self.stage.moving_target_index][0].coordinates.y = self.right_y
                self.stage.moving_target_index=-1

            else:
                self.stage.add_target(Target([0, ((self.right_x) / (self.screen_width * 0.8)) * 0.8,
                                              ((self.right_y) / (self.screen_height * 0.8)) * 0.8, 99,
                                              self.timeline.percent * self.stage.stage.stage_music.duration, 25,
                                              self.selected_picture_name], self.screen, self.stage.stage_name))
                self.stage.stage.play()
                self.stage.active_target_index=len(self.stage.stage.active_targets)-1
                self.stage.targets_index=len(self.stage.targets)-1

            self.last_click = time.time()
            self.is_selected_target = False
            self.import_delete_button.active = True
            #print("active_target",self.stage.active_target_index)
            self.inputValueTarget.value=int(self.stage.stage.active_targets[self.stage.active_target_index][0].value)
            self.inputDurationTarget.value=int(self.stage.stage.active_targets[self.stage.active_target_index][0].duration)
            self.show()
            self.stage.stage.play()



    def sup_import_target(self):
        if self.import_delete_button.x < self.right_x < (self.import_delete_button.x + self.import_delete_button.width) and \
             self.import_delete_button.y < self.right_y < (self.import_delete_button.y + self.import_delete_button.height):
        #print("press import/suppression")
            if (time.time()-self.last_click)>1:
                self.last_click=time.time()
                if not self.import_delete_button.active:  # suppression
                    print("supréssion")
                    self.import_delete_button.active = True
                    self.stage.remove_traget()
                    self.delete()
                    self.inputDurationTarget.show_input_value = False
                    self.inputValueTarget.show_input_value = False
                else:  # import
                    print("import")
                    target = easygui.fileopenbox(title="Chosir une cible", default='*.png')
                    if target is not None:
                        self.stage.add_special_target(target)
                        while target.find("\\") != -1:
                            target = target[target.find("\\") + 1:]
                        if (len(self.import_targets_list) == 0):
                            self.import_targets_list.append(MenuLevelCreationButton(self.screen_width * 0.9,
                                                                                    self.screen_height * 0.1,
                                                                                    self.screen_width * 0.1,
                                                                                    Constants.TARGET_RADIUS * 1.6,
                                                                                    self.screen, target, target[:-4], 35, 10,
                                                                                    "arial.ttf", (255, 255, 255),
                                                                                    self.stage.stage_name))
                        else:
                            self.import_targets_list.append(MenuLevelCreationButton(self.screen_width * 0.9,
                                                                                    self.screen_height * 0.1 * (
                                                                                                len(self.import_targets_list) + 1),
                                                                                    self.screen_width * 0.1,
                                                                                    Constants.TARGET_RADIUS * 1.6,
                                                                                    self.screen, target, target[:-4], 35, 10,
                                                                                    "arial.ttf",
                                                                                    (255, 255, 255), self.stage.stage_name))
                    self.newScreen()
            self.show()
