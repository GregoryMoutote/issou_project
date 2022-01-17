import numpy as np

class CalibrationTool:
    def __init__(self):
        print("pass")
        #self.colorFinder = ColorDetection()

    def calibrate(self):
        self.colorFinder.detect_color()
        pts1 = np.float32([self.colorFinder.colorPoint[0], self.colorFinder.colorPoint[1],
                           self.colorFinder.colorPoint[3], self.colorFinder.colorPoint[4]])