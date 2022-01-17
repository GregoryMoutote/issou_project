from calibration import CalibrationTool
import cv2


calibr_util = CalibrationTool.CalibrationTool()
calibr_util.initCamera()
calibr_util.getPoints()
calibr_util.calcMatrix()
calibr_util.closeCamera()
print(calibr_util.calibratePoint((276.0,150.0)))

cap = cv2.VideoCapture(0)
_, img = cap.read()
img_calibr = calibr_util.calibratePicture(img, True)
cap.release()