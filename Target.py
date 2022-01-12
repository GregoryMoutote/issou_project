from Coordinates import Coordinates

class Target:
    def __init__(self, targetData):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.coordinates = Coordinates(targetData[1], targetData[2])
            self.duration = float(targetData[3])
            self.delay = float(targetData[4])
            self.value = int(targetData[5])
            self.color = [int(targetData[6]), int(targetData[7]), int(targetData[8])]

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value, self.color)