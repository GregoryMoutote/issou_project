from Interfaces.Interface import *
import ctypes
from Interfaces.GIF.CalibrageGIF import *

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)

class InterfaceCalibrage(Interface):

    def __init__(self,screenData,screen,detection):

        super().__init__(screenData, screen)
        self.detection=detection

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Sprite Animation")
        self.moving_sprites = pygame.sprite.Group()
        ISSOUlaodGIF = loadGIF(self.screenWidth/2-299,self.screenHeight/2-88,self.screen)
        self.moving_sprites.add(ISSOUlaodGIF)

        self.loop()


    def loop(self):
        result=False

        while result==False:
            result=self.detection.setUpCalibration()
            self.show()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        result = True


    def show(self):

        self.screen.fill((255, 255, 255))
        pygame.font.init()
        arialFont = pygame.font.Font("./Fonts/lemonmilk.otf", 70)
        arialFont2 = pygame.font.Font("./Fonts/arial.ttf", 50)
        text = arialFont.render("Calibrage en cours...", True, (0, 0, 0))
        text2 = arialFont2.render("Espace pour passer", True, (0, 0, 0))
        pygame.font.quit()

        self.screen.blit(text, (self.screenWidth / 2 - 500, self.screenHeight*0.3))
        self.screen.blit(text2, (self.screenWidth / 2 - 250, self.screenHeight*0.8))

        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update(0.25)
        self.clock.tick(60)
        pygame.display.update()