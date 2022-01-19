import threading
import pygame

class RefreshThread(threading.Thread):
    def __init__(self, ecran, mainMenu):
        self.continuer = True
        self.screen = ecran

    def run(self):
        while self.continuer:
            self.screen.blit(self.screen.background, (0, 0))
            for self.mainMenu.c in self.mainMenu.bottun:
                self.mainMenu.c.showButton()
            self.screen.blit(self.mainMenu.fondLogo, (self.mainMenu.screenWidth / 10, self.mainMenu.screenHeight / 2 - 249))
            self.screen.moving_sprites.draw(self.screen)
            self.screen.moving_sprites.update(1)

            self.mainMenu.show()
            if len(self.mainMenu.detection.mediaPipe.leftHand) > 0:
                # print("right", self.detection.mediaPipe.leftHand[0], "  ", self.detection.mediaPipe.leftHand[1])
                pygame.draw.circle(self.screen, (255, 0, 0), (self.mainMenu.leftX - 5, self.mainMenu.leftY - 5), 10)

            if len(self.mainMenu.detection.mediaPipe.rightHand) > 0:
                pygame.draw.circle(self.screen, (255, 255, 255), (self.mainMenu.rightX - 5, self.mainMenu.rightY - 5), 10)
            pygame.display.update()
        pass


    def stop(self):
        self.continuer = False

