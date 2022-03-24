import pygame

from Targets.Target import Target
from Model.Stage.Coordinates import  Coordinates
from Model.Constants import *
from Model.ScreenData import *
import math

class RailTarget(Target):
    def __init__(self, target_data, screen, level_name):
        if isinstance(target_data, list) and len(target_data) >= 9:
            self.screen = screen
            self.step_active=0
            self.is_active=False
            self.actual_coordinates=Coordinates(1,1)
            super(RailTarget, self).__init__(target_data, self.screen, level_name)
            self.picture_position=pygame.image.load("Pictures/Targets/" + self.pictureName + ".png")
            self.picture_position = pygame.transform.scale(self.picture_position, (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
            self.transparent_picture = pygame.image.load("Pictures/Targets/Transparent/" + self.pictureName + "_transparent.png")
            self.transparent_picture = pygame.transform.scale(self.transparent_picture, (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
            iterator = 7
            self.steps = []
            screen = ScreenData()
            self.steps.append(Coordinates(self.coordinates.x,self.coordinates.y))
            while iterator < len(target_data) - 1:
                self.steps.append(Coordinates(target_data[iterator] * screen.width,
                                              target_data[iterator + 1] * screen.width))
                iterator += 2
            self.is_achieved = False

    """
    Affiche la cible et les étapes qui la composent
    """
    def show_target(self):
        endx = self.steps[self.step_active].x
        endy = self.steps[self.step_active].y
        for i in range(self.step_active,len(self.steps)):
            beginx = endx
            beginy = endy
            endx = self.steps[i].x
            endy = self.steps[i].y
            pygame.draw.line(self.screen, (100, 0, 0), (beginx+ Constants.TARGET_RADIUS,
                                                            beginy+ Constants.TARGET_RADIUS),
                                                            (endx + Constants.TARGET_RADIUS,
                                                            endy+Constants.TARGET_RADIUS), 10)

        for i in range(self.step_active,len(self.steps)):
            if i==self.step_active:
                self.screen.blit(self.picture, (self.steps[i].x, self.steps[i].y))
            else:
                self.screen.blit(self.transparent_picture, (self.steps[i].x, self.steps[i].y))
        if self.step_active < len(self.steps) - 1:
            if(((self.steps[self.step_active].x<self.actual_coordinates.x<self.steps[self.step_active+1].x) or (self.steps[self.step_active+1].x<self.actual_coordinates.x<self.steps[self.step_active].x))and self.is_active):
                self.screen.blit(self.picture_position, (self.actual_coordinates.x,self.actual_coordinates.y))

    """
    Met à jour la cible en fonction de l'étape à laquelle le joueur se trouve
    """
    def actualise(self, actual_coordinates: Coordinates):
        if actual_coordinates == None:
            return
        if self.step_active==len(self.steps)-1:
            self.is_achieved = True

        elif self.is_active:
            if self.step_active<len(self.steps)-1:
                if ( self.steps[self.step_active + 1].x - self.steps[self.step_active].x)!=0:
                    angle = math.atan((self.steps[self.step_active + 1].y - self.steps[self.step_active].y) / ( self.steps[self.step_active + 1].x - self.steps[self.step_active].x))
                    self.actual_coordinates = Coordinates(actual_coordinates.x - Constants.TARGET_RADIUS, self.steps[self.step_active].y +
                                (actual_coordinates.x - self.steps[self.step_active].x - Constants.TARGET_RADIUS) * math.tan(angle))

                if self.steps[self.step_active+1].x+Constants.TARGET_RADIUS/8<actual_coordinates.x and actual_coordinates.x<(self.steps[self.step_active+1].x+Constants.TARGET_RADIUS*2)-Constants.TARGET_RADIUS/8 \
                        and self.steps[self.step_active+1].y+Constants.TARGET_RADIUS/8<actual_coordinates.y and actual_coordinates.y<(self.steps[self.step_active+1].y+Constants.TARGET_RADIUS*2)+Constants.TARGET_RADIUS/8:
                    self.step_active += 1

        elif self.steps[0].x<actual_coordinates.x<self.steps[0].x+Constants.TARGET_RADIUS*2 \
                        and self.steps[0].y<actual_coordinates.y<self.steps[0].y+Constants.TARGET_RADIUS*2:
                self.is_active=True