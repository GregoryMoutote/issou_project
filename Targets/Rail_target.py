from Targets.Target import Target
from Coordinates import  Coordinates

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