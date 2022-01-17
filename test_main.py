import keyboard

from MediaPipeTool import *
from calibration import ShapeDetection

test_util = ShapeDetection.ShapeDetection()
test_util.isDisplaying = True
test_util.initCamera()
test_util.detectBoard()
print("FOUND " + str(len(test_util.corners))+" SHAPE(S) WITH "+str(len(test_util.corners[0]))+" DIMENSIONS...")
test_util.closeCamera()