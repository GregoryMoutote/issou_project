from Targets.Target import *
import time
import ctypes

class Dynamic_target(Target):
    def __init__(self, targetData,screen,picture):
        if isinstance(targetData, list) and len(targetData) >= 8:
            self.beginTime=0
            self.screen=screen
            super(Dynamic_target, self).__init__(targetData,self.screen,picture)
            self.begin_value=self.value
            self.end_value = int(targetData[7])

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value, self.end_value)

    def update(self):
        if self.beginTime == 0:
            self.beginTime = time.time()
        self.value =int(self.begin_value - (self.begin_value - self.end_value) * (
                    (time.time() - self.beginTime) / self.duration))
