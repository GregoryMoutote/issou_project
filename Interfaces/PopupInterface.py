import pygame.draw

from Buttons.PictureButton import *
from Interfaces.SettingsInterface import *

class PopupInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings, parent, error_message):
        self.parent = parent
        self.settings = settings
        self.detection = detection
        self.err_message = error_message

        super().__init__(screen_data, screen)

        #COLORS
        self.DARK_BLUE = (12, 7, 99)
        self.LIGHT_GRAY = (113, 113, 113)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0,0,0)


        #TEXT
        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 60)

        # Buttons


        self.text_surface = my_font.render(self.err_message, True, (0,0,0))

        pygame.font.quit()


        #POPUP ATTRIBUTE
        self.popup_width = self.text_surface.get_width() * 2
        self.popup_height = self.text_surface.get_height()*3
        self.popup_ratio = 0.6
        self.popup_ratio = self.text_surface.get_height()/self.popup_height
        self.popup_x = (self.screen_width - self.popup_width) /2
        self.popup_y = (self.screen_height - self.popup_height) /2



        self.upper_popup = pygame.Rect(self.popup_x, self.popup_y, self.popup_width,
                                       self.popup_height*self.popup_ratio)
        self.lower_popup = pygame.Rect(self.popup_x,self.popup_y-1+(self.popup_height*(self.popup_ratio)),
                                       self.popup_width, self.popup_height*(1-self.popup_ratio))

        self.button = ColorButton(self.popup_x + 50, self.popup_y + 60, self.popup_width / 3, 70, self.screen,
                                  self.WHITE, "OK", 100, "lemonmilk.otf", self.BLACK)



        self.show()
        self.reset_coo()
        self.loop()


    def loop(self):
        go_on = True

        while go_on:
            self.detection.hand_detection()

            if len(self.detection.right_hand) > 0:
                self.right_x = self.detection.right_hand[0]
                self.right_y = self.detection.right_hand[1]

            if len(self.detection.left_hand) > 0:
                self.left_x = self.detection.left_hand[0]
                self.left_y = self.detection.left_hand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        go_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.right_x, self.right_y = pygame.mouse.get_pos()
                    self.detection.is_fist_closed = 1

            self.show_hand()

            if self.detection.is_fist_closed == 1:

                if self.screen_width/2-225 > self.right_x > self.screen_width/2+225 and \
                        self.screen_height / 2 - 300 > self.right_y > self.screen_height / 2 + 300:
                    go_on = False

    def show(self):
        pygame.draw.rect(self.screen, self.DARK_BLUE, self.upper_popup)
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, self.lower_popup)
        self.screen.blit(self.text_surface, (self.popup_x+(self.text_surface.get_width()/2), self.popup_y))
        self.button.show_button()


    def show_hand(self):
        self.parent.show()
        self.show()
        if len(self.detection.left_hand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.left_x - 5, self.left_y - 5), 10)

        if len(self.detection.right_hand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.right_x - 5, self.right_y - 5), 10)
        pygame.display.update()

    def reset_coo(self):
        self.right_x = 0
        self.right_y = 0
        self.left_x = 0
        self.left_y = 0