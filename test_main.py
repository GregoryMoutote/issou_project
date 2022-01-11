import keyboard

from MediaPipeTool import *

mediapipeClass = MediaPipeTool()
mediapipeClass.initHandCapture()
while 1:
    mediapipeClass.hand_detection()
    if mediapipeClass.leftHand:
        print("Left hand", mediapipeClass.leftHand)
    if mediapipeClass.rightHand:
        print("Right hand", mediapipeClass.rightHand)
    if keyboard.is_pressed('q'):
        break

mediapipeClass.closeCamera()