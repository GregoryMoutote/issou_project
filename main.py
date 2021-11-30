from mainMenuInterface import *
from playerDetection.MediaPipeThread import MediaPipeThread

detection = MediaPipeThread()
detection.start()

MainMenuInterface(detection)