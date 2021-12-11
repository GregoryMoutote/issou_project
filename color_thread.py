import threading
import time
from color_util import color_util

class colorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.colorClass = color_util()

    def run(self):
        self.colorClass.detect_color()
        print(self.colorClass.colorPoint)

