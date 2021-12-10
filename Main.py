from InterfaceCalibrage import *
from playerDetection.MediaPipeThread import MediaPipeThread

detection = MediaPipeThread()
detection.start()

InterfaceCalibrage(detection)