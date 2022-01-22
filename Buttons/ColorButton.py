import pygame
from Buttons.Button import *

class ColorButton(Button):

    def __init__(self, x, y, width, height, screen, color, text, text_size, text_left_space, font, text_color):
        super().__init__(x, y, width, height, screen)
        self.text = text
        self.text_size = text_size
        self.text_left_space = text_left_space
        self.font = "./Fonts/" + font
        self.text_color = text_color
        self.color = color
        self.show_button()


    def show_button(self):
        pygame.font.init()
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        my_font = pygame.font.Font(self.font, self.text_size)
        text_surface = my_font.render(self.text, True, self.text_color)
        pygame.font.quit()
        self.screen.blit(text_surface, (self.x + self.text_left_space, self.y + (self.height - self.text_size) / 2))