import ctypes
from Bottun.ColorBottun import *

pygame.init()
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height= user32.GetSystemMetrics(1)
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN,pygame.NOFRAME)

botton = [Botton(width / 6 * 3 + 5, height / 2 - 187, width / 2.4, 75, screen, (0, 112, 192), "JOUER", 40, 290,"Glitch.otf", (255, 255, 255))]

continuer=True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                   continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            self.rightX,self.rightY=pygame.mouse.get_pos()