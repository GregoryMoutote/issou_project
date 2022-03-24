from Targets.Target import Target
from Model.Stage.Coordinates import Coordinates
from Model.Constants import *
import time
from Model.ScreenData import ScreenData

class MovingTarget(Target):
    def __init__(self, target_data, screen, level_name):
        if isinstance(target_data, list) and len(target_data) >= 9:
            self.begin_time = 0
            self.screen=screen
            super(MovingTarget, self).__init__(target_data, screen, level_name)
            self.begin_coordinates = Coordinates(self.coordinates.x, self.coordinates.y)
            screen = ScreenData()
            self.end_coordinates = Coordinates(float(target_data[7] * screen.height),
                                               float(target_data[8] * screen.height))


    """
    Affiche la cible à l'écran
    """
    def show_target(self):
        self.screen.blit(self.picture, (self.coordinates.x - Constants.TARGET_RADIUS ,self.coordinates.y - Constants.TARGET_RADIUS))

    """
    Met à jour la position de la cible en fonction du temps
    """
    def update(self):
        if self.begin_time == 0:
            self.begin_time = time.time()
        self.coordinates.x = self.begin_coordinates.x + (self.end_coordinates.x - self.begin_coordinates.x) * (
                (time.time() - self.begin_time) / self.duration)
        self.coordinates.y = self.begin_coordinates.y + (self.end_coordinates.y - self.begin_coordinates.y) * (
                (time.time() - self.begin_time) / self.duration)
