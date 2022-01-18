from Interface.MainMenuInterface import *
from playerDetection.MediaPipeToolOld import MediaPipeTool
from Settings import *
import pygame

detection = MediaPipeTool()
detection.initHandCapture()

screenData = ctypes.windll.user32

settings = Settings()

pygame.init()
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN,pygame.NOFRAME)

InterfaceCalibrage(screenData,screen)
MainMenuInterface(screenData,screen,detection,settings)