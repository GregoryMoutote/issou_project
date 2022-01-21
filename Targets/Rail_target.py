import pygame

from Targets.Target import Target
from Coordinates import  Coordinates
from Constants import *

class Rail_target(Target):
    def __init__(self, targetData,screen,levelName):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.screen=screen
            super(Rail_target, self).__init__(targetData,self.screen,levelName)
            self.transparentPicture = pygame.image.load("picture/targets/transparent/" + self.pictureName + "_transparent.png")
            self.transparentPicture = pygame.transform.scale(self.transparentPicture,(2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
            iterator = 7
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
        for i in range(0,len(self.steps)):
            if i==0:
                self.screen.blit(self.picture, (self.steps[i].x, self.steps[i].y))
            else:
                self.screen.blit(self.transparentPicture, (self.steps[i].x, self.steps[i].y))
