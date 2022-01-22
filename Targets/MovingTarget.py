from Targets.Target import Target
from Model.Stage.Coordinates import Coordinates
from Model.Constants import *
import time
import ctypes

class MovingTarget(Target):
    def __init__(self, target_data, screen, level_name):
        if isinstance(target_data, list) and len(target_data) >= 9:
            self.begin_time = 0
            self.screen=screen
            #super(target_data, screen, level_name)
            super(MovingTarget, self).__init__(target_data, screen, level_name)
            self.begin_coordinates = Coordinates(self.coordinates.x, self.coordinates.y)
            screen = ctypes.windll.user32
            self.end_coordinates = Coordinates(float(target_data[7] * screen.GetSystemMetrics(1)),
                                               float(target_data[8] * screen.GetSystemMetrics(1)))

    def display(self):
        print(self.coordinates, self.end_coordinates, self.duration, self.delay, self.value)

    def update(self):
        if self.begin_time == 0:
            self.begin_time = time.time()
        self.coordinates.x = self.begin_coordinates.x + (self.end_coordinates.x - self.begin_coordinates.x) * (
                (time.time() - self.begin_time) / self.duration)
        self.coordinates.y = self.begin_coordinates.y + (self.end_coordinates.y - self.begin_coordinates.y) * (
                (time.time() - self.begin_time) / self.duration)

        #problème quand on met en pose le time avant donc quand on revient en jeux la différence de entre startTime et time à augmenter donc la cible ce tp en avant
        #il faut faire comme dans stage et soustraire le temps de pause
