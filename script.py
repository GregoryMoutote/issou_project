from test_color import color_util
from color_thread import colorThread
import pygame
import threading
import keyboard
import cv2
import time



coloro = colorThread()
coloro.start()
continuer = True
while continuer :
    if len(coloro.colorClass.colorPoint) != 0:
        print(coloro.colorClass.colorPoint)
    if keyboard.is_pressed("q"):
        break