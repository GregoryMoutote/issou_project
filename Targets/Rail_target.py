from Targets.Target import Target
from Coordinates import  Coordinates
from Constants import Constants

class Rail_target(Target):
    def __init__(self, targetData,screen):
        if isinstance(targetData, list) and len(targetData) >= 7:
            self.screen=screen
            super(Rail_target, self).__init__(targetData,self.screen)
            iterator = 7
            self.steps = []
            while iterator < len(targetData) - 1:
                self.steps.append(Coordinates(targetData[iterator], targetData[iterator + 1]))
                iterator += 2
            self.is_achieved = False

    def display(self):
        print(self.coordinates, self.steps, self.duration, self.delay, self.value)

    def actualise(self, actual_coordinates: Coordinates):
        if actual_coordinates == None:
            return
        self.coordinates = actual_coordinates
        if int(self.coordinates.x - self.steps[0][0]) ** 2 + \
            int(self.coordinates.y - self.steps[0][1]) ** 2 <= (Constants.TARGET_RADIUS * 2) ** 2:
            self.steps.pop(0)
        if len(self.steps) == 0:
            self.is_achieved = True
