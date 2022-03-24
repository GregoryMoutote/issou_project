import pygame
from Buttons.Button import *

class InputCreationLevelButton(Button):

    def __init__(self, x, y, width, height, screen, value, font, text_color,text, text_size,):
        super().__init__(x,y,width,height,screen)
        picture = pygame.image.load("Pictures/Interfaces/inputCreationLevel.png")
        self.picture = pygame.transform.scale(picture, (width, height))
        self.value = value
        self.show_input_value=False
        self.font = "./Fonts/" + font
        self.text_color = text_color
        self.nb_size=int(height*0.8)
        self.text = text
        self.text_size = text_size
        self.show_button()


    def show_button(self): #affiche le bouton
        self.screen.blit(self.picture, (self.x, self.y))

    def show_value(self): #affiche le bouton avec la nouvelle valeur
        pygame.font.init()
        my_font = pygame.font.Font(self.font, self.nb_size)
        if self.show_input_value:
            if self.value < 10:
                text_surface = my_font.render("0"+str(self.value), True, self.text_color)
            else:
                text_surface = my_font.render(str(self.value), True, self.text_color)
        else:
            text_surface = my_font.render("--", True, self.text_color)
        self.screen.blit(text_surface,(self.x+(self.width-text_surface.get_width())*0.5,self.y+(self.height-text_surface.get_height())*0.5))
        my_font = pygame.font.Font(self.font, self.text_size)
        text_surface = my_font.render(self.text, True, self.text_color)
        self.screen.blit(text_surface,(self.x + self.width / 2 - (len(self.text)*self.text_size) /5 , self.y +self.height+ 5))
        pygame.font.quit()

    def click(self,x): #incrémente ou décrémente la valeur du bouton
        if self.show_input_value:
            if(x<self.x+self.width*0.32 and self.value>1):
                self.value -= 1
            elif (x>self.x+self.width*0.68 and self.value<99):
                self.value += 1