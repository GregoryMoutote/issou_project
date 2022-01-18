import cv2
from calibration.CalibrationTool import *

random_image =  cv2.imread("calibration/table3.jpg")

print(type(random_image))

calibr_util = CalibrationTool()
calibr_util.setup(random_image)

calibr_util.calibratePicture(True)