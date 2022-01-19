from Targets.Target import Target

class Dynamic_target(Target):
    def __init__(self, targetData,screen):
        if isinstance(targetData, list) and len(targetData) >= 8:
            self.screen=screen
            super(Dynamic_target, self).__init__(targetData,self.screen)
            self.end_value = int(targetData[7])

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value, self.end_value)