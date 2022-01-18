from calibration import CalibrationTool
import cv2


calibr_util = CalibrationTool.CalibrationTool()
#calibr_util.initCamera()
calibr_util.getPoints()
calibr_util.calcMatrix()
#calibr_util.closeCamera()
pointInitial = (92,15)
pointCalibre = calibr_util.calibratePoint(pointInitial)
print("Point Initial = " + str(pointInitial))
print("Point Calibre = " + str(pointCalibre))

#cap = cv2.VideoCapture(0)
#_, img = cap.read()
#cap.release()

img = cv2.imread("calibration/table2.png")


img_calibr = calibr_util.calibratePicture(img, True)
