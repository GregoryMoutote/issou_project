from Interface.Interface import *
import ctypes
from Interface.GIF.CalibrageGIF import *

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)

class InterfaceCalibrage(interface):

    def __init__(self,screenData,screen,detection):

        super().__init__(screenData, screen)
        self.detection=detection
        self.show()

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
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        result = True

            self.moving_sprites.draw(self.screen)
            self.moving_sprites.update(0.25)
            self.clock.tick(60)
            pygame.display.update()

    def show(self):

        self.screen.fill((255, 255, 255))
        #print(self.screenWidth,"/",self.screenHeight)
        #pygame.draw.rect(self.screen,(255,0,0),(20, 20, self.screenWidth-40, self.screenHeight-40))
        #pygame.draw.circle(self.screen, (0,255, 0), (50, 50), 50)
        #pygame.draw.circle(self.screen, (0,255, 0), (self.screenWidth - 50, 50), 50)
        #pygame.draw.circle(self.screen, (0,255, 0), (50, self.screenHeight - 50), 50)
        #pygame.draw.circle(self.screen, (0,255, 0), (self.screenWidth - 50, self.screenHeight - 50), 50)

        pygame.font.init()
        arialFont = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
        text = arialFont.render("Calibrage en cours...", True, (255, 255, 255))
        pygame.font.quit()
        #self.screen.blit(text, (self.screenWidth / 2 - 250, self.screenHeight / 2 - 100))

        pygame.display.update()