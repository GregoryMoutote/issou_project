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


        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 60)
        self.text_surface = my_font.render(self.err_message, True, (0,0,0))
        pygame.font.quit()

        self.popup_area = pygame.Rect(self.screen_width / 2 - 250, self.screen_height / 2 - 250, self.text_surface.get_width()*2, 500)

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
        pygame.draw.rect(self.screen, (255, 255, 255), self.popup_area)
        pygame.draw.rect(self.screen,(255,255,255),self.popup_area,2,3)
        self.screen.blit(self.text_surface, (self.screen_width / 2 - 110, self.screen_height / 2 - 270))


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