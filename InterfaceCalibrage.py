from Interface import *
from MainMenuInterface import *
import ctypes
import pygame, sys
from sprite_animation_final import *

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)

class InterfaceCalibrage(Interface):

    def __init__(self,detection):

        self.screenData = ctypes.windll.user32
        pygame.init()
        self.screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN,pygame.NOFRAME)
        super().__init__(self.screenData, self.screen)

        clock = pygame.time.Clock()
        pygame.display.set_caption("Sprite Animation")
        moving_sprites = pygame.sprite.Group()
        player = Player(self.screenWidth/2+100,self.screenHeight/2-50,self.screen)
        moving_sprites.add(player)

        self.screen.fill((0,0,0))
        pygame.draw.circle(self.screen, (200,0,0), (50,50), 50)
        pygame.draw.circle(self.screen, (200,0,0), (self.screenWidth-50, 50), 50)
        pygame.draw.circle(self.screen, (200,0,0), (50, self.screenHeight-50), 50)
        pygame.draw.circle(self.screen, (200,0,0), (self.screenWidth-50, self.screenHeight-50), 50)
        pygame.font.init()
        myfont = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
        self.textsurface = myfont.render("Calibrage en cours", True, (255,255,255))
        self.screen.blit(self.textsurface, (self.screenWidth/2, self.screenHeight/2-25))
        pygame.font.quit()

        pygame.display.update()

        continuer=True

        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                        print("mainmenuInterface")
                    if event.key == pygame.K_a:
                        player.attack()

            self.screen.fill((0, 0, 0))
            moving_sprites.draw(self.screen)
            moving_sprites.update(0.25)
            clock.tick(60)
            self.show()

        MainMenuInterface(detection,self.screenData,self.screen)


    def show(self):

        pygame.draw.circle(self.screen, (200, 0, 0), (50, 50), 50)
        pygame.draw.circle(self.screen, (200, 0, 0), (self.screenWidth - 50, 50), 50)
        pygame.draw.circle(self.screen, (200, 0, 0), (50, self.screenHeight - 50), 50)
        pygame.draw.circle(self.screen, (200, 0, 0), (self.screenWidth - 50, self.screenHeight - 50), 50)
        self.screen.blit(self.textsurface, (self.screenWidth / 2 - 400, self.screenHeight / 2 - 25))
        pygame.display.update()