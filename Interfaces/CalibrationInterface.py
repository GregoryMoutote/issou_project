from Interfaces.Interface import *
import ctypes
from Interfaces.GIF.CalibrageGIF import *

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)

class CalibrationInterface(Interface):

    def __init__(self, screen_data, screen, detection):

        super().__init__(screen_data, screen)
        self.detection = detection

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Sprite Animation")
        self.moving_sprites = pygame.sprite.Group()
        ISSOU_laod_gif = load_gif(self.screen_width / 2 - 299, self.screen_height / 2 - 88, self.screen)
        self.moving_sprites.add(ISSOU_laod_gif)

        self.loop()


    def loop(self):
        result = False

        while result == False:
            result = self.detection.media_pipe.set_up_calibration()
            self.show()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        result = True


    def show(self):

        self.screen.fill((255, 255, 255))
        pygame.font.init()
        arial_font = pygame.font.Font("./Fonts/lemonmilk.otf", 70)
        arial_font2 = pygame.font.Font("./Fonts/arial.ttf", 50)
        text = arial_font.render("Calibrage en cours...", True, (0, 0, 0))
        text2 = arial_font2.render("Espace pour passer", True, (0, 0, 0))
        pygame.font.quit()

        self.screen.blit(text, (self.screen_width / 2 - 500, self.screen_height * 0.3))
        self.screen.blit(text2, (self.screen_width / 2 - 250, self.screen_height * 0.8))

        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update(0.25)
        self.clock.tick(60)
        pygame.display.update()