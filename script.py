from test_color import color_util
from color_thread import colorThread
import pygame
import threading
import keyboard
import cv2
import time
from MediaPipeThread import MediaPipeThread



detection = MediaPipeThread()
detection.start()
continuer = True
while continuer :
    if len(detection.mediaPipeClass.hand) != 0:
        print(detection.mediaPipeClass.hand)
    if keyboard.is_pressed("q"):
        break