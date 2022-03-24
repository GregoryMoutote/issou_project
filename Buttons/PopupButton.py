import pygame.draw


class PopupButton:
    def __init__(self, screen, text):
        self.screen = screen

        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 40)
        self.text_surface = my_font.render(text, True, (0, 0, 0))
        pygame.font.quit()


        #Button Size
        self.button_width = self.text_surface.get_width()
        self.button_height = self.text_surface.get_height()

    def displayButton(self, x, y): #affiche le bouton
        button = pygame.Rect(x,y,self.button_width, self.button_height)
        pygame.draw.rect(self.screen, (255,255,255),button)
        self.screen.blit(self.text_surface, (x,y))




