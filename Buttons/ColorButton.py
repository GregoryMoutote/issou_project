import pygame
from Buttons.Button import *

class ColorButton(Button):

    def __init__(self, x, y, width, height, screen, color, text, percent, font, text_color):
        super().__init__(x, y, width, height, screen)
        self.color = color
        self.text = text
        self.text_size = int(height*0.5)
        self.percent = percent
        self.font = "./Fonts/" + font
        self.text_color = text_color
        self.show_button()


    def show_button(self):
        if self.text != "":
            pygame.font.init()
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
            my_font = pygame.font.Font(self.font, self.text_size)
            text_surface = my_font.render(self.text, True, self.text_color)
            pygame.font.quit()
            self.screen.blit(text_surface,(self.x + (self.width-text_surface.get_width())*0.5+self.width*0.5*
                                           (self.percent-0.5) , self.y+(self.height-text_surface.get_height())*0.5))