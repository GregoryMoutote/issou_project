import pygame
from Button.Button import *

class pictureButton(Button):

    def __init__(self, x, y, width, height, screen,picture, text, textSize, textLeftSpace, font,textColor):
        super().__init__(x,y,width,height,screen)
        picture = pygame.image.load("picture/interface/" + picture)
        self.picture = pygame.transform.scale(picture, (width, height))
        self.text = text
        self.textSize = textSize
        self.textLeftSpace = textLeftSpace
        self.font = "./font/" + font
        self.textColor = textColor
        self.showButton()


    def showButton(self):
        self.screen.blit(self.picture, (self.x, self.y))
        if(self.text!=""):
            pygame.font.init()
            myfont = pygame.font.Font(self.font, self.textSize)
            textsurface = myfont.render(self.text, True, self.textColor)
            self.screen.blit(textsurface, (self.x + self.textLeftSpace, self.y + (self.height - self.textSize) / 2))
            pygame.font.quit()

