from Interfaces.MainMenuInterface import *
from Model.Settings.Settings import *
import pygame
from PlayerDetection.MediapipeTool import *

detection = MediapipeTool()


screen_data = ctypes.windll.user32

pygame.init()

screen = pygame.display.set_mode((screen_data.GetSystemMetrics(0), screen_data.GetSystemMetrics(1)), pygame.NOFRAME)
settings = Settings()

CalibrationInterface(screen_data, screen, detection)
MainMenuInterface(screen_data, screen, detection, settings)