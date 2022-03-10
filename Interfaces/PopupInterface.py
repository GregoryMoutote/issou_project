import traceback

import pygame.draw

from Buttons.PictureButton import *
from Interfaces.SettingsInterface import *
from Buttons.PopupButton import *


def split_lines(max_width,max_height, text,font, color=pygame.Color('white')):
    words = text.split(' ')

    line = ""
    line_length = 0
    line_height = font.render("cc",0,color).get_height()
    line_surface = []
    line_index = 0

    for word in words:
        line_length += font.render(word, 0, color).get_width()
        line += word + ' '
        if line_length > max_width:
            line_surface.append(font.render(line, 0, color))
            line = ""
            line_length = 0
            line_index += 1

            if max_height < line_height*(line_index+1):
                line_surface.append(font.render("...",0,color))
                break


    line_surface.append(font.render(line, 0, color))

    return line_surface

class PopupInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings, parent, error_message, subtext):

        #COLORS
        self.DARK_BLUE = (12, 7, 99)
        self.LIGHT_GRAY = (113, 113, 113)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)


        #TECHNIC PARAM
        self.parent = parent
        self.settings = settings
        self.detection = detection


        self.err_message = error_message

        super().__init__(screen_data, screen)

        #TEXT
        pygame.font.init()
        my_font = pygame.font.Font("./Fonts/lemonmilk.otf", 50)


        self.text_surface = my_font.render(self.err_message, True, (255,255,255))

        my_smaller_font = pygame.font.Font("./Fonts/lemonmilk.otf", 20)

        self.sub_text = my_smaller_font.render("Texte explicatif", True, (255,255,255))


        self.buttons = []
        self.return_values = []


        try:
            self.background = pygame.image.load("./Pictures/Interfaces/popup_background.png")
            self.popup_width = 549
            self.popup_height = 544
            self.background = pygame.transform.scale(self.background,(self.popup_width, self.popup_height))

            my_smaller_font = pygame.font.Font("./Fonts/lemonmilk.otf", 20)

            self.text_surfaces = split_lines(self.popup_width-140,150,subtext,my_smaller_font)
            print(subtext)

            pygame.font.quit()

            self.popup_x = (self.screen_width - self.popup_width) / 2
            self.popup_y = (self.screen_height - self.popup_height) / 2

            self.button_width = self.popup_width - 100

            self.popup_button = PictureButton(self.popup_x+(self.popup_width-self.button_width)/2,
                                              self.popup_y+self.popup_height-60*1.5,
                                              self.button_width, 60,
                                              self.screen, "popup_button.png", "OK", 0.5,"lemonmilk.otf",
                                              (255,255,255) )

            self.buttons.append(self.popup_button)
            self.return_values.append(0)
            self.is_image_loaded = True
        except Exception:
            print(traceback.format_exc())
            self.popup_width = self.text_surface.get_width() * 2
            self.popup_height = self.text_surface.get_height() * 3
            self.popup_ratio = 0.6
            self.popup_ratio = self.text_surface.get_height() / self.popup_height


            self.upper_popup = pygame.Rect(self.popup_x, self.popup_y, self.popup_width,
                                           self.popup_height * self.popup_ratio)
            self.lower_popup = pygame.Rect(self.popup_x, self.popup_y - 1 + (self.popup_height * self.popup_ratio),
                                           self.popup_width, self.popup_height * (1 - self.popup_ratio))
            self.is_image_loaded = False

        self.button = PopupButton(self.screen, "OK")


        self.popup_x = (self.screen_width - self.popup_width) / 2
        self.popup_y = (self.screen_height - self.popup_height) / 2






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
                for i in range (len(self.buttons)):
                    if self.buttons[i].x < self.right_x and (self.buttons[i].x+self.buttons[i].width) > self.right_x and \
                        self.buttons[i].y < self.right_y and (self.buttons[i].y+self.buttons[i].height) >self.right_y:
                        go_on = False
                        return self.return_values[i]


    def show(self):
        if self.is_image_loaded:
            self.screen.blit(self.background, ((self.screen_width-self.popup_width)/2,
                                               (self.screen_height-self.popup_height)/2))
            self.screen.blit(self.text_surface, (self.popup_x+(self.popup_width-self.text_surface.get_width())/2,
                                                 (self.popup_y+self.text_surface.get_height()*2)))

            coordinate_y = self.popup_y+self.text_surface.get_height()*3.75
            for i in self.text_surfaces :
                self.screen.blit(i, (self.popup_x+30, coordinate_y))
                coordinate_y += i.get_height()

            for button in self.buttons:
                button.show_button()



        else:
            pygame.draw.rect(self.screen, self.DARK_BLUE, self.upper_popup)
            pygame.draw.rect(self.screen, self.LIGHT_GRAY, self.lower_popup)
            self.screen.blit(self.text_surface, (self.popup_x, self.popup_y))
            self.button.displayButton(self.popup_x + 40, self.popup_y + 60)


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

    def add_button(self, text, return_value=0):
        nb_button = len(self.buttons)
        new_width = (self.popup_width - 100)/(nb_button+1)
        for i in range (len(self.buttons)):
            self.buttons[i].set_width(new_width)
            self.buttons[i].x = self.popup_x + (i*new_width) + (self.popup_width*0.1)
        added_popup_button = PictureButton(self.popup_x + (nb_button*new_width)+ (self.popup_width*0.1),
                                          self.popup_y + self.popup_height - 60 * 1.5,
                                          new_width, 60,
                                          self.screen, "popup_button.png", text, 0.5, "lemonmilk.otf",
                                          (255, 255, 255))
        self.return_values.append(return_value)
        self.buttons.append(added_popup_button)


    def start(self):
        self.show()
        self.reset_coo()
        return self.loop()

    def set_return(self,index, value):
        if len(self.return_values)>index:
            self.return_values[index] = value

    def set_button_text(self, index, text):
        if len(self.buttons)>index:
            self.buttons[index].text = text





