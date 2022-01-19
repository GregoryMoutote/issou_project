from Coordinates import Coordinates
import pygame

from Constants import Constants

class Target:
    def __init__(self, targetData,screen, picture):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.screen=screen
            self.picture=pygame.image.load("picture/targets/"+picture)
            self.picture = pygame.transform.scale(self.picture,
                                                  (2 * Constants.TARGET_RADIUS, 2 * Constants.TARGET_RADIUS))
            self.coordinates = Coordinates(targetData[1], targetData[2])
            self.duration = float(targetData[3])
            self.delay = float(targetData[4])
            self.value = int(targetData[5])
            self.color = [int(targetData[6]), int(targetData[7]), int(targetData[8])]

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value, self.color)

    def showTarget(self):
        self.screen.blit(self.picture, (self.coordinates.x - Constants.TARGET_RADIUS ,self.coordinates.y - Constants.TARGET_RADIUS))

    def update(self):
        pass