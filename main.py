from Interface.MainMenuInterface import *
from Settings import *
import pygame
from playerDetection.MediaPipeThread import MediaPipeThread

detection = MediaPipeThread()


screenData = ctypes.windll.user32

pygame.init()

screen = pygame.display.set_mode((screenData.GetSystemMetrics(0),screenData.GetSystemMetrics(1)),pygame.NOFRAME)
settings = Settings()

InterfaceCalibrage(screenData,screen,detection)
MainMenuInterface(screenData,screen,detection,settings)