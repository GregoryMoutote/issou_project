from Targets.Target import Target
from Coordinates import  Coordinates

class Moving_target(Target):
    def __init__(self, targetData,screen,picture):
        if isinstance(targetData, list) and len(targetData) >= 11:
            self.screen=screen
            super(Moving_target, self).__init__(targetData,screen,picture)
            self.end_coordinates = Coordinates(float(targetData[9]), float(targetData[10]))

    def display(self):
        print(self.coordinates, self.end_coordinates, self.duration, self.delay, self.value, self.color)