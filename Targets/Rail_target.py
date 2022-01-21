import pygame

from Targets.Target import Target
from Model.Stage.Coordinates import  Coordinates
from Model.Constants import *
import ctypes

class Rail_target(Target):
    def __init__(self, targetData,screen,levelName):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.screen=screen
            super(Rail_target, self).__init__(targetData,self.screen,levelName)
            self.transparentPicture = pygame.image.load("Pictures/Targets/Transparent/" + self.pictureName + "_transparent.png")
            self.transparentPicture = pygame.transform.scale(self.transparentPicture,(2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
            iterator = 7
            self.steps = []
            screen = ctypes.windll.user32
            while iterator < len(targetData) - 1:
                self.steps.append(Coordinates(targetData[iterator] * screen.GetSystemMetrics(1),
                                              targetData[iterator + 1] * screen.GetSystemMetrics(1)))
                iterator += 2
            self.is_achieved = False

    def display(self):
        print(self.coordinates, self.steps, self.duration, self.delay, self.value)

    def showTarget(self):
        beginx=0
        beginy=0
        endx=0
        endy=0
        for point in self.steps:
            beginx=endx
            beginy=endy
            endx=point.x
            endy=point.y
            if(beginx!=0 and beginy!=0):
                pygame.draw.line(self.screen,(255,0,0),(beginx+Constants.TARGET_RADIUS,beginy+Constants.TARGET_RADIUS),(endx+Constants.TARGET_RADIUS,endy+Constants.TARGET_RADIUS),10)
        for i in range(0,len(self.steps)):
            if i==0:
                self.screen.blit(self.picture, (self.steps[i].x, self.steps[i].y))
            else:
                self.screen.blit(self.transparentPicture, (self.steps[i].x, self.steps[i].y))

        
    def actualise(self, actual_coordinates: Coordinates):
        if actual_coordinates == None:
            return
        self.coordinates = actual_coordinates
        if int(self.coordinates.x - self.steps[0][0]) ** 2 + \
            int(self.coordinates.y - self.steps[0][1]) ** 2 <= (Constants.TARGET_RADIUS * 2) ** 2:
            self.steps.pop(0)
        if len(self.steps) == 0:
            self.is_achieved = True
