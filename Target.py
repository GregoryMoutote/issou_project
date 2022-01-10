

class Target:
    def __init__(self, targetData):
        if isinstance(targetData, list) and len(targetData) >= 9:
            self.x = int(targetData[1])
            self.y = int(targetData[2])
            self.duration = float(targetData[3])
            self.delay = float(targetData[4])
            self.value = int(targetData[5])
            self.color = [int(targetData[6]), int(targetData[7]), int(targetData[8])]

    def display(self):
        print(self.x, self.y, self.duration, self.delay, self.value, self.color)