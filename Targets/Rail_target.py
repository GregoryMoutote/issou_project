import pygame

from Targets.Target import Target
from Coordinates import  Coordinates
from Constants import *

class Rail_target(Target):
    def __init__(self, targetData,screen,picture):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.screen=screen
            super(Rail_target, self).__init__(targetData,self.screen,picture)
            iterator = 9
            self.steps = []
            while iterator < len(targetData) - 1:
                self.steps.append(Coordinates(targetData[iterator], targetData[iterator + 1]))
                iterator += 2

    def display(self):
        print(self.coordinates, self.steps, self.duration, self.delay, self.value, self.color)

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
        for point in self.steps:
            self.screen.blit(self.picture, (point.x, point.y))