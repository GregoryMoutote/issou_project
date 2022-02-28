import pygame.draw
from Interfaces.LevelCreationSecondInterface import *
from Buttons.PictureButton import *
from Interfaces.PopupInterface import *

class LevelCreationFirstInterface(Interface):

    def __init__(self, screen_data, screen, detection, settings):
        self.settings = settings
        self.detection = detection


        super().__init__(screen_data, screen)

        ##TEXT INPUT
        self.default_x = self.screen_width / 2 - 175
        self.input_rect = pygame.Rect(self.default_x, self.screen_height / 2 - 200, 1000, 50)
        self.is_input_active = False
        self.user_text = ""
        self.color = (0,0,0)
        self.active_color = (100, 100, 100)
        self.inactive_color = (50, 50, 50)

        self.background_path = ""
        self.music_path = ""
        self.icon_path = ""

        self.buttons = [PictureButton(self.screen_width / 2 - 200, self.screen_height / 2 - 75, 400, 75,
                                      self.screen, "button2.png", "Voir mes fichiers", 0.5, "Glitch.otf",
                                      (255, 255, 255))]
        self.buttons.append(PictureButton(self.screen_width / 2 - 200, self.screen_height / 2 + 75, 400, 75,
                                          self.screen, "button2.png", "Voir mes fichiers", 0.5, "Glitch.otf",
                                          (255, 255, 255)))

        self.buttons.append(PictureButton(self.screen_width / 2 - 200, self.screen_height / 2 + 225, 400, 75,
                                          self.screen, "button2.png", "Voir mes fichiers", 0.5, "Glitch.otf",
                                          (255, 255, 255)))


        self.buttons.append(PictureButton(self.screen_width / 2 - 200, self.screen_height / 2 + 325, 400, 75,
                                          self.screen, "button3.png", "Valider", 0.5, "Glitch.otf",
                                          (255, 255, 255)))



        self.newScreen()
        self.reset_coo()
        self.loop()

    def loop(self):
        try :
            go_on=True

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
                        if self.is_input_active:
                            if event.key == pygame.K_BACKSPACE:
                                self.user_text = self.user_text[:-1]
                            else:
                                self.user_text += event.unicode

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.right_x, self.right_y = pygame.mouse.get_pos()
                        self.detection.is_fist_closed=1

                self.show_hand()

                if self.is_input_active:
                    self.color = self.active_color
                else:
                    self.color = self.inactive_color

                if self.detection.is_fist_closed==1:
                    if self.buttons[0].x < self.right_x < (self.buttons[0].x + self.buttons[0].width) and \
                            self.buttons[0].y < self.right_y < (self.buttons[0].y + self.buttons[0].height):
                       self.reset_coo()
                       self.show()
                       self.is_input_active = False


                       tmp_path = easygui.fileopenbox(title="Chosir une image",default='*.jpg',
                                                     filetypes=[['*.png','*.jpg','*.jpeg',"Image File"]], multiple=False)
                       if tmp_path  is not None:
                           tmp_extension = self.get_extension(tmp_path)
                           if tmp_extension== '.jpg' or tmp_extension== '.png' or tmp_extension== '.jpeg':
                                self.background_path = tmp_path
                                self.buttons[0].text = "..." + self.background_path[-16:]
                                self.newScreen()


                    elif self.buttons[1].x < self.right_x < (self.buttons[1].x + self.buttons[1].width) and \
                            self.buttons[1].y < self.right_y < (self.buttons[1].y + self.buttons[1].height):
                        self.reset_coo()
                        self.show()
                        self.is_input_active = False
                        tmp_path = easygui.fileopenbox(title="Chosir une musique",
                                                       default='*.mp3', filetypes=[['*.mp3','*.wav','Music File']])
                        if tmp_path is not None:
                            tmp_extension = self.get_extension(tmp_path)
                            if tmp_extension == '.mp3' or tmp_extension == '.wav':
                                self.music_path = tmp_path
                                self.buttons[1].text = "..." + self.music_path[-16:]
                                self.newScreen()

                    elif self.buttons[2].x < self.right_x < (self.buttons[2].x + self.buttons[2].width) and \
                            self.buttons[2].y < self.right_y < (self.buttons[2].y + self.buttons[2].height):
                        self.reset_coo()
                        self.show()
                        self.is_input_active = False
                        tmp_path = easygui.fileopenbox(title="Chosir une icone", default='*.jpg',
                                                       filetypes=[['*.png', '*.jpg', '*.jpeg', "Image File"]],
                                                       multiple=False)
                        if tmp_path is not None:
                            tmp_extension = self.get_extension(tmp_path)
                            if tmp_extension== '.jpg' or tmp_extension== '.png' or tmp_extension== '.jpeg':
                                self.icon_path = tmp_path
                                self.buttons[2].text = "..." + self.icon_path[-16:]
                                self.newScreen()

                    elif self.buttons[3].x < self.right_x < (self.buttons[3].x + self.buttons[3].width) and \
                            self.buttons[3].y < self.right_y < (self.buttons[3].y + self.buttons[3].height):

                        if not (self.music_path == "" or self.background_path == "" or self.icon_path == "" or self.user_text == ""):
                            LevelCreationSecondInterface(self.screen_data, self.screen, self.detection, self.settings,self.user_text,"./Pictures/Interfaces/testPicture.jpg",self.background_path,self.music_path)
                            self.reset_coo()
                            self.show()
                            self.is_input_active = False
                        else :
                            PopupInterface(self.screen_data, self.screen, self.detection, self.settings, self, "INFORMATION",
                                           "Certains champs sont vides")
                            self.detection.is_fist_closed=0

                    elif self.input_rect.x < self.right_x < (self.input_rect.x + self.input_rect.w) and \
                            self.input_rect.y < self.right_y < (self.input_rect.y + self.input_rect.h):
                        self.is_input_active = True
                        pass
                    else:
                        self.is_input_active = False
        except Exception:
            PopupInterface(self.screen_data, self.screen, self.detection, self.settings, self, "ERREUR",
                           traceback.format_exc())

    def show(self):
        self.screen.blit(self.background, (0, 0))
        pygame.font.init()
        littleglitch_font = pygame.font.Font("./Fonts/glitch.otf", 40)
        text_surface = littleglitch_font.render(self.user_text, True, (255, 255, 255))
        pygame.font.quit()

        self.input_rect.w = max(100, text_surface.get_width() + 10)
        if len(self.user_text) <= 2:
            self.input_rect.x = (self.screen_width / 2) - (self.input_rect.w / 2)
        else:
            self.input_rect.x = self.screen_width / 2 - text_surface.get_width() / 2

        pygame.draw.rect(self.screen, self.color, self.input_rect)
        self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))



    def show_hand(self):
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

    def newScreen(self):
        self.screen.blit(pygame.image.load("./Pictures/Interfaces/levelBuilderBackground.png"), (0, 0))

        pygame.font.init()
        glitch_font = pygame.font.Font("./Fonts/glitch.otf", 80)
        littleglitch_font = pygame.font.Font("./Fonts/glitch.otf", 40)
        title_text = glitch_font.render("Creation de niveau", True, (255, 255, 255))
        text1 = littleglitch_font.render("Nom du niveau", True, (255, 255, 255))
        text2 = littleglitch_font.render("Image de fond", True, (255, 255, 255))
        text3 = littleglitch_font.render("Musique", True, (255, 255, 255))
        text4 = littleglitch_font.render("Icone du niveau", True, (255, 255, 255))

        pygame.font.quit()

        self.screen.blit(title_text, ((self.screen_width-title_text.get_width())/2 , 30))
        self.screen.blit(text1, ((self.screen_width-text1.get_width())/2 , self.screen_height / 2 - 250))
        self.screen.blit(text2, ((self.screen_width-text2.get_width())/2 , self.screen_height / 2 - 125))
        self.screen.blit(text3, ((self.screen_width-text3.get_width())/2 , self.screen_height / 2 +25))
        self.screen.blit(text4, ((self.screen_width-text4.get_width())/2 , self.screen_height / 2 + 175))

        for button in self.buttons:
            button.show_button()
        pygame.image.save(self.screen,"background.jpg")
        self.background=pygame.image.load("background.jpg")
        self.show()


    def get_extension(self, file_name):
        return file_name[file_name.find('.'):]
