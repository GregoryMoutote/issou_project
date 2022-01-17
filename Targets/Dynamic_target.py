from Target import Target

class Dynamic_target(Target):
    def __init__(self, targetData):
        if isinstance(targetData, list) and len(targetData) >= 10:
            super(Dynamic_target, self).__init__(targetData)
            self.end_value = int(targetData[9])

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value, self.end_value, self.color)