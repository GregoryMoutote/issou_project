from Targets.Target import Target
from Coordinates import  Coordinates

class Moving_target(Target):
    def __init__(self, targetData,screen):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.screen=screen
            super(Moving_target, self).__init__(targetData,screen)
            self.end_coordinates = Coordinates(float(targetData[7]), float(targetData[8]))

    def display(self):
        print(self.coordinates, self.end_coordinates, self.duration, self.delay, self.value)