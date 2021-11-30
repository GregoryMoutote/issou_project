from Interface import *


class InterfaceCalibrage(Interface):

    def __init__(self,screenData,screen,detection):
        super().__init__(screenData,screen)
        self.screen.fill((0,0,0))
        self.detection=detection
        pygame.draw.circle(screen, (150,0,0), (50,50), 50)
        pygame.draw.circle(screen, (150,0,0), (self.screenWidth-50, 50), 50)
        pygame.draw.circle(screen, (150,0,0), (50, self.screenHeight-50), 50)
        pygame.draw.circle(screen, (150,0,0), (self.screenWidth-50, self.screenHeight-50), 50)
        pygame.display.update()

        continuer=True

        while continuer:
            self.testAffichage()
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False

    def testAffichage(self):
        hand=self.detection.mediaPipeClass.hand
        x=0
        y=0
        if(len(hand)):
            x=hand[0][0]
            y=hand[0][1]

        self.screen.fill((0,0,0))
        pygame.draw.circle(self.screen, (0, 255,0), (x, y), 100)
        pygame.display.update()