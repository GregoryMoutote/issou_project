from calibration import CalibrationTool
import cv2

calibr_util = CalibrationTool.CalibrationTool()
calibr_util.initCamera()
calibr_util.getPoints()
calibr_util.calcMatrix()
img = cv2.imread("calibration/tableBite.jpg")
print(calibr_util.calibratePoint((276.0,150.0)))
img_calibr = calibr_util.calibratePicture(img, True)
calibr_util.closeCamera()