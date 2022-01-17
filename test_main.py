import keyboard


##THIS FILE IS TEMPORARY, DO NOT DELETE IT !

from calibration import ShapeDetection

test_util = ShapeDetection.ShapeDetection()
test_util.isDisplaying = True
test_util.initCamera()
test_util.detectFromPicture()
print("FOUND 1 SHAPE(S) WITH "+str(len(test_util.corners))+" DIMENSIONS...")
print (test_util.corners)
test_util.closeCamera()