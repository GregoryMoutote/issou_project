from Interface.InterfaceCalibrage import *
from Interface.MainMenuInterface import *
from playerDetection.MediaPipeTool import MediaPipeTool
import pygame

detection = MediaPipeTool()
detection.initHandCapture()

screenData = ctypes.windll.user32
pygame.init()
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN,pygame.NOFRAME)

InterfaceCalibrage(detection,screenData,screen)
MainMenuInterface(detection,screenData,screen)