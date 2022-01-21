from Coordinates import Coordinates
import pygame
import os
import ctypes

from Constants import Constants

class Target:
    def __init__(self, targetData,screen):
        if isinstance(targetData, list) and len(targetData) >= 7:
            self.screen=screen
            screen = ctypes.windll.user32
            self.coordinates = Coordinates(targetData[1] * screen.GetSystemMetrics(0),
                                           targetData[2] * screen.GetSystemMetrics(1))
            self.duration = float(targetData[3])
            self.delay = float(targetData[4])
            self.value = int(targetData[5])
            not_found = False
            if isinstance(targetData[6], str):
                if os.path.isfile("picture/targets/basics/" + targetData[6] + ".png"):
                    self.picture = pygame.image.load("picture/targets/basics/" + targetData[6] + ".png")
                    self.picture = pygame.transform.scale(self.picture,
                                                          (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
                elif os.path.isfile("picture/targets/imported/" + targetData[6] + ".png"):
                    self.picture = pygame.image.load("picture/targets/imported/" + targetData[6] + ".png")
                    self.picture = pygame.transform.scale(self.picture,
                                                          (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
                else:
                    not_found = True
            else:
                not_found = True
            if not_found:
                self.picture = pygame.image.load("picture/targets/basic_blue.png")
                self.picture = pygame.transform.scale(self.picture,
                                                      (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value)

    def update(self):
        pass

    def showTarget(self):
        self.screen.blit(self.picture, (self.coordinates.x - Constants.TARGET_RADIUS ,self.coordinates.y - Constants.TARGET_RADIUS))