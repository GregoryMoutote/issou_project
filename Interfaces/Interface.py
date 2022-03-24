import pygame

class Interface:

    def __init__(self, screen_data, screen):
        self.screen = screen
        self.screen_data = screen_data
        self.screen_width = screen_data.GetSystemMetrics(0)
        self.screen_height = screen_data.GetSystemMetrics(1)

    """
    affiche tout les composant dans le screen
    """
    def update_interface(self):
        pygame.display.update()