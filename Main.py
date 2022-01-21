from Interface.MainMenuInterface import *
from Settings import *
import pygame
from playerDetection.MediaPipeThread import MediaPipeThread

detection = MediaPipeThread()


screenData = ctypes.windll.user32

settings = Settings()

pygame.init()
screen = pygame.display.set_mode((screenData.GetSystemMetrics(0),screenData.GetSystemMetrics(1)),pygame.NOFRAME)

InterfaceCalibrage(screenData,screen,detection)
MainMenuInterface(screenData,screen,detection,settings)