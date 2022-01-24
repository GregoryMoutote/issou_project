from Targets.Target import *
import time
import ctypes

class DynamicTarget(Target):
    def __init__(self, target_data, screen, level_name):
        if isinstance(target_data, list) and len(target_data) >= 8:
            self.begin_time = 0
            self.screen = screen
            super(DynamicTarget, self).__init__(target_data, self.screen, level_name)
            self.begin_value = self.value
            self.end_value = int(target_data[7])

    def display(self):
        print(self.coordinates, self.duration, self.delay, self.value, self.end_value)

    def update(self):
        if self.begin_time == 0:
            self.begin_time = time.time()
        self.value =int(self.begin_value - (self.begin_value - self.end_value) * (
                (time.time() - self.begin_time) / self.duration))