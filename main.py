from Interface.MainMenuInterface import *
from playerDetection.MediaPipeTool import MediaPipeTool
from Settings import *
import pygame

detection = MediaPipeThread()


screenData = ctypes.windll.user32

settings = Settings()

pygame.init()
screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN,pygame.NOFRAME)

InterfaceCalibrage(screenData,screen,detection)
MainMenuInterface(screenData,screen,detection,settings)