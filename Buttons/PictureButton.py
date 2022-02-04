import pygame
from Buttons.Button import *

class PictureButton(Button):

    def __init__(self, x, y, width, height, screen, picture,  text, porcent, font, text_color):
        super().__init__(x,y,width,height,screen)
        picture = pygame.image.load("Pictures/Interfaces/" + picture)
        self.picture = pygame.transform.scale(picture, (width, height))
        self.text = text
        self.text_size = int(height*0.5)
        self.porcent=porcent
        self.font = "./Fonts/" + font
        self.text_color = text_color
        self.show_button()


    def show_button(self):
        self.screen.blit(self.picture, (self.x, self.y))
        if self.text != "" :
            pygame.font.init()
            my_font = pygame.font.Font(self.font, self.text_size)
            text_surface = my_font.render(self.text, True, self.text_color)
            pygame.font.quit()
            self.screen.blit(text_surface,(self.x + (self.width-text_surface.get_width())*0.5+self.width*0.5*(self.porcent-0.5) , self.y+(self.height-text_surface.get_height())*0.5))


