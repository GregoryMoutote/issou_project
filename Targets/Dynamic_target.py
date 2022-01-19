from Targets.Target import Target

class Dynamic_target(Target):
    def __init__(self, targetData,screen,picture):
        if isinstance(targetData, list) and len(targetData) >= 10:
            self.screen=screen
            super(Dynamic_target, self).__init__(targetData,self.screen,picture)
            self.end_value = int(targetData[9])

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value, self.end_value, self.color)