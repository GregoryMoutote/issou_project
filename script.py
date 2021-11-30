from test_color import color_util
from color_thread import colorThread
import pygame
import threading
import keyboard
import cv2
import time
from MediaPipeThread import MediaPipeThread



detection = colorThread()
detection.start()
"""while 1:
    if len(detection.colorClass.colorPoint) != 0:
        print(detection.colorClass.colorPoint)
    if keyboard.is_pressed("q"):
        break"""