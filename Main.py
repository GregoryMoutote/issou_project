from Interface.MainMenuInterface import *
from Settings import *
import pygame
from playerDetection.MediaPipeThread import MediaPipeThread

detection = MediaPipeThread()


screenData = ctypes.windll.user32

settings = Settings()

pygame.init()
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN,pygame.NOFRAME)

InterfaceCalibrage(screenData,screen,detection)
MainMenuInterface(screenData,screen,detection,settings)