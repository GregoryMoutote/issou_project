import threading
import time
from test_color import color_util

class colorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.colorClass = color_util()

    def run(self):
        self.colorClass.detect_color()
        print(self.colorClass.colorPoint)

