from Interface import *
from MainMenuInterface import *
import ctypes
import pygame.draw

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)

class InterfaceCalibrage(Interface):

    def __init__(self,detection):
        self.screenData = ctypes.windll.user32
        pygame.init()
        self.screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN,pygame.NOFRAME)

        super().__init__(self.screenData,self.screen)
        self.screen.fill((0,0,0))
        pygame.draw.circle(self.screen, (150,0,0), (50,50), 50)
        pygame.draw.circle(self.screen, (150,0,0), (self.screenWidth-50, 50), 50)
        pygame.draw.circle(self.screen, (150,0,0), (50, self.screenHeight-50), 50)
        pygame.draw.circle(self.screen, (150,0,0), (self.screenWidth-50, self.screenHeight-50), 50)
        pygame.font.init()
        myfont = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
        textsurface = myfont.render("Calibrage en cour veuillez patienter", True, (255,255,255))
        self.screen.blit(textsurface, (self.screenWidth/2-400, self.screenHeight/2-25))
        pygame.font.quit()
        pygame.display.update()

        continuer=True

        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                        print("mainmenuInterface")

        MainMenuInterface(detection,self.screenData,self.screen)