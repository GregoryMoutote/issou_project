from mainMenuInterface import *
from MediaPipeThread import MediaPipeThread

detection = MediaPipeThread()
detection.start()

MainMenuInterface(detection)