import pygame

from Targets.Target import Target
from Model.Stage.Coordinates import  Coordinates
from Model.Constants import *
import ctypes

class RailTarget(Target):
    def __init__(self, target_data, screen, level_name):
        if isinstance(target_data, list) and len(target_data) >= 9:
            self.screen = screen
            super(RailTarget, self).__init__(target_data, self.screen, level_name)
            self.transparent_picture = pygame.image.load("Pictures/Targets/Transparent/" + self.pictureName + "_transparent.png")
            self.transparent_picture = pygame.transform.scale(self.transparent_picture, (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
            iterator = 7
            self.steps = []
            screen = ctypes.windll.user32
            while iterator < len(target_data) - 1:
                self.steps.append(Coordinates(target_data[iterator] * screen.GetSystemMetrics(0),
                                              target_data[iterator + 1] * screen.GetSystemMetrics(1)))
                iterator += 2
            self.is_achieved = False

    def display(self):
        print(self.coordinates, self.steps, self.duration, self.delay, self.value)

    def show_target(self):
        endx = self.coordinates.x- Constants.TARGET_RADIUS
        endy = self.coordinates.y- Constants.TARGET_RADIUS
        for point in self.steps:
            beginx = endx
            beginy = endy
            endx = point.x
            endy = point.y
            pygame.draw.line(self.screen, (255, 0, 0), (beginx+ Constants.TARGET_RADIUS,
                                                            beginy+ Constants.TARGET_RADIUS),
                                                            (endx + Constants.TARGET_RADIUS,
                                                            endy+Constants.TARGET_RADIUS), 10)

        self.screen.blit(self.picture, (self.coordinates.x- Constants.TARGET_RADIUS, self.coordinates.y- Constants.TARGET_RADIUS))
        for i in range(0, len(self.steps)):
                self.screen.blit(self.transparent_picture, (self.steps[i].x, self.steps[i].y))

        
    def actualise(self, actual_coordinates: Coordinates):
        if actual_coordinates == None:
            return
        self.coordinates = actual_coordinates
        if int(self.coordinates.x - self.steps[0].x) ** 2 + \
            int(self.coordinates.y - self.steps[0].y) ** 2 <= (Constants.TARGET_RADIUS * 2) ** 2:
            self.steps.pop(0)
        if len(self.steps) == 0:
            self.is_achieved = True
