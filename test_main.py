import keyboard

from MediaPipeTool import *
from calibration import ShapeDetection

test_util = ShapeDetection.ShapeDetection()
test_util.initCamera()
test_util.detectBoard()
test_util.closeCamera()