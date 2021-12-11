import keyboard

from MediaPipeThread import MediaPipeThread
from MediaPipeTool import MediaPipeTool
from multiprocessing import *

from color_util import color_util
import multitasking

multitasking.set_engine("process")
multitasking.set_max_threads(multitasking.config["CPU_CORES"] * 5)


detection = MediaPipeTool()
detection.body_detection()
tmp = ""
while 1:

    if tmp != detection.hand:
        tmp = detection.hand
        print(detection.hand)
    if keyboard.is_pressed("q"):
        break
