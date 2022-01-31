from Targets.Target import Target
from Model.Stage.Coordinates import Coordinates
from Model.Constants import *
import time
import ctypes

class Moving_target(Target):
    def __init__(self, targetData,screen,levelName):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.beginTime =0
            self.screen=screen
            #super(targetData,screen,levelName)
            super(Moving_target, self).__init__(targetData,screen,levelName)
            self.begin_coordinates = Coordinates(self.coordinates.x, self.coordinates.y)
            screen = ctypes.windll.user32
            self.end_coordinates = Coordinates(float(targetData[7] * screen.GetSystemMetrics(1)),
                                               float(targetData[8] * screen.GetSystemMetrics(1)))

    def display(self):
        print(self.coordinates, self.end_coordinates, self.duration, self.delay, self.value)

    def update(self):
        if self.beginTime == 0:
            self.beginTime = time.time()
        self.coordinates.x = self.begin_coordinates.x + (self.end_coordinates.x - self.begin_coordinates.x) * (
                    (time.time() - self.beginTime) / self.duration)
        self.coordinates.y = self.begin_coordinates.y + (self.end_coordinates.y - self.begin_coordinates.y) * (
                    (time.time() - self.beginTime) / self.duration)

        #problème quand on met en pose le time avant donc quand on revient en jeux la différence de entre startTime et time à augmenter donc la cible ce tp en avant
        #il faut faire comme dans stage et soustraire le temps de pause