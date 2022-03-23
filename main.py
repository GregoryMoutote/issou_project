from Interfaces.MainMenuInterface import *
from Model.Settings.Settings import *
import pygame
from PlayerDetection.MediapipeTool import *
from Model.ScreenData import ScreenData


detection = MediapipeTool()


screen_data = ScreenData()

pygame.init()

screen = pygame.display.set_mode((screen_data.width, screen_data.height), pygame.NOFRAME)
settings = Settings()

CalibrationInterface(screen_data, screen, detection)
MainMenuInterface(screen_data, screen, detection, settings)
pygame.quit()