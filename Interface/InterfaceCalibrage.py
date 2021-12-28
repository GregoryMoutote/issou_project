from Interface.Interface import *
import ctypes
from CalibrageGIF import *

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)

class InterfaceCalibrage(interface):

    def __init__(self,screenData,screen):

        super().__init__(screenData, screen)

        clock = pygame.time.Clock()
        pygame.display.set_caption("Sprite Animation")
        moving_sprites = pygame.sprite.Group()
        ISSOUlaod = loadGIF(self.screenWidth/2-300,self.screenHeight/2,self.screen)
        moving_sprites.add(ISSOUlaod)

        self.screen.fill((0,0,0))
        pygame.draw.circle(self.screen, (200,0,0), (50,50), 50)
        pygame.draw.circle(self.screen, (200,0,0), (self.screenWidth-50, 50), 50)
        pygame.draw.circle(self.screen, (200,0,0), (50, self.screenHeight-50), 50)
        pygame.draw.circle(self.screen, (200,0,0), (self.screenWidth-50, self.screenHeight-50), 50)

        pygame.font.init()
        myfont = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
        self.textsurface = myfont.render("Calibrage en cours...", True, (255,255,255))
        pygame.font.quit()

        pygame.display.update()

        continuer=True

        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()

            moving_sprites.draw(self.screen)
            moving_sprites.update(0.25)
            clock.tick(60)
            self.show()


    def show(self):

        pygame.draw.circle(self.screen, (200, 0, 0), (50, 50), 50)
        pygame.draw.circle(self.screen, (200, 0, 0), (self.screenWidth - 50, 50), 50)
        pygame.draw.circle(self.screen, (200, 0, 0), (50, self.screenHeight - 50), 50)
        pygame.draw.circle(self.screen, (200, 0, 0), (self.screenWidth - 50, self.screenHeight - 50), 50)
        self.screen.blit(self.textsurface, (self.screenWidth/2 - 250, self.screenHeight / 2 - 100))
        pygame.display.update()
