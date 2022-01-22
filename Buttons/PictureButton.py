import pygame
from Buttons.Button import *

class PictureButton(Button):

    def __init__(self, x, y, width, height, screen, picture, text, text_size, text_left_space, font, text_color):
        super().__init__(x,y,width,height,screen)
        picture = pygame.image.load("Pictures/Interfaces/" + picture)
        self.picture = pygame.transform.scale(picture, (width, height))
        self.text = text
        self.text_size = text_size
        self.text_left_space = text_left_space
        self.font = "./Fonts/" + font
        self.text_color = text_color
        self.show_button()


    def show_button(self):
        self.screen.blit(self.picture, (self.x, self.y))
        if self.text != "" :
            pygame.font.init()
            my_font = pygame.font.Font(self.font, self.text_size)
            text_surface = my_font.render(self.text, True, self.text_color)
            self.screen.blit(text_surface, (self.x + self.text_left_space, self.y + (self.height - self.text_size) / 2))
            pygame.font.quit()

