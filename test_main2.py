from calibration import CalibrationTool

calibr_util = CalibrationTool.CalibrationTool()
#calibr_util.initCamera()
calibr_util.calibrate()
calibr_util.showCalibratedPic()
#calibr_util.closeCamera()