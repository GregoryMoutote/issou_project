from Model.Stage.Coordinates import Coordinates
from Model.Constants import Constants
import pygame
import os
from Model.ScreenData import ScreenData

class Target:
    def __init__(self, target_data, screen, level_name):
        if isinstance(target_data, list) and len(target_data) >= 7:
            self.screen = screen
            self.pictureName = target_data[6]
            screen = ScreenData()
            self.coordinates = Coordinates(target_data[1] * screen.width,
                                           target_data[2] * screen.height)
            self.duration = float(target_data[3])
            self.delay = float(target_data[4])
            self.value = int(target_data[5])
            not_found = False

            if isinstance(target_data[6], str):
                if target_data[6].find(".")!=-1:
                    target_data[6]=target_data[6][:target_data[6].find(".")]
                if os.path.isfile("Pictures/Targets/" + target_data[6] + ".png"):
                    self.picture = pygame.image.load("Pictures/Targets/" + target_data[6] + ".png")
                    self.picture = pygame.transform.scale(self.picture, (
                    2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
                    self.image = target_data[6]
                elif os.path.isfile("Stages/" + level_name + "/specialTargets/" + target_data[6] + ".png"):
                    self.picture = pygame.image.load(
                        "Stages/" + level_name + "/specialTargets/" + target_data[6] + ".png")
                    self.picture = pygame.transform.scale(self.picture, (
                    2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
                    self.image = target_data[6]
                else:
                    not_found = True
            else:
                not_found = True
            if not_found:
                self.picture = pygame.image.load("Pictures/Targets/basic_blue.png")
                self.picture = pygame.transform.scale(self.picture,
                                                      (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
                self.image = "basic_blue"

    def update(self):
        pass

    """
    Affiche la cible
    """
    def show_target(self):
        self.screen.blit(self.picture, (self.coordinates.x - Constants.TARGET_RADIUS ,self.coordinates.y - Constants.TARGET_RADIUS))

    def delete(self):
        pass