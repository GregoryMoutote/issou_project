from Target import Target
from Coordinates import  Coordinates

class Rail_target(Target):
    def __init__(self, targetData):
        if isinstance(targetData, list) and len(targetData) >= 9:
            super(Rail_target, self).__init__(targetData)
            iterator = 9
            self.steps = []
            while iterator < len(targetData) - 1:
                self.steps.append(Coordinates(targetData[iterator], targetData[iterator + 1]))
                iterator += 2

    def display(self):
        print(self.coordinates, self.steps, self.duration, self.delay, self.value, self.color)