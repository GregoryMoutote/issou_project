import pygame.draw

from Interface.Interface import *
from bottun.NavigationBottoun import *


class LevelSelectionInterface(Interface):

    def __init__(self,detection,screendata,screen):
        self.detection=detection
        self.detection.initHandCapture()
        self.screenData=screendata
        self.screen=screen

        super().__init__(self.screenData, self.screen)

        self.background = pygame.image.load("./picture/interface/fond.png")
        self.fondLogo=pygame.image.load("./picture/interface/fondLogo.png")

        self.screen.blit(self.background, (0, 0))

        self.showDescription("titre plus long","images.png","DIFFICILE","Ceci est une petite description de la musique que vous avez sélectionnée. Ceci est une petite description de la musique que vous avez sélectionnée. Ceci est une petite description de la musique que vous avez sélectionnée.","6:66",3)

        pygame.draw.rect(self.screen,(50,50,50),(0,self.screenHeight*0.9,self.screenWidth,self.screenHeight*0.1))

        self.quit=navigationBottun(0,self.screenHeight*0.91,self.screenWidth/5,self.screenHeight*0.08,self.screen ,(100,100,100),"retour",50,50,"Glitch.otf",(255,255,255))

        self.random = pygame.image.load("./picture/interface/dice.png")
        self.up=pygame.image.load("./picture/interface/arrowUp.png")
        self.down = pygame.image.load("./picture/interface/arrowDown.png")

        pygame.display.update()

        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0

        continuer=True

        while continuer:

            detection.hand_detection()
            self.testAffichage()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            if self.rightX>self.quit.x and self.rightX<(self.quit.x+self.quit.width) and self.rightY>self.quit.y and self.rightY<(self.quit.y+self.quit.height):
               continuer=False

            self.testAffichage()

            pygame.display.update()

    def showDescription(self,name,picture,difficulty,description,duration,nbStar):

        pygame.draw.rect(self.screen, (30, 30, 30), (0, 0, self.screenWidth, self.screenHeight / 5))

        self.musicPicture = pygame.image.load("./picture/interface/"+picture)
        self.musicPicture = pygame.transform.scale(self.musicPicture,(self.screenHeight / 5 - 20, self.screenHeight / 5 - 20))
        self.screen.blit(self.musicPicture, (10, 10))

        self.starUnchecked = pygame.image.load("./picture/interface/starUnchecked.png")
        self.starUnchecked = pygame.transform.scale(self.starUnchecked,(60, 60))

        self.starChecked = pygame.image.load("./picture/interface/starChecked.png")
        self.starChecked = pygame.transform.scale(self.starChecked,(60, 60))

        for i in range(0,5):
            if(i<nbStar-0.5):
                self.screen.blit(self.starChecked, (self.screenWidth/5+len(name)*45+len(difficulty)*15+70*i, 10))
            else:
                self.screen.blit(self.starUnchecked,(self.screenWidth/5+len(name)*45+len(difficulty)*15+70*i, 10))

        pygame.font.init()
        fontGlitch=pygame.font.Font("./font/Glitch.otf",70)
        fontArial=pygame.font.Font("./font/Arial.ttf",30)
        fontBigArial = pygame.font.Font("./font/Arial.ttf", 40)

        self.title = fontGlitch.render(name, True, (255, 255, 255))
        self.screen.blit(self.title, (self.screenHeight / 5, 10))
        "DIFFICILE"
        self.difficulty = fontBigArial.render(difficulty, True, (255, 0, 0))
        self.screen.blit(self.difficulty, (self.screenHeight / 5+len(name)*45, 25))

        for i in range(0, len(description), 80):
            text = fontArial.render(description[i:i + 80], True, (255, 255, 255))
            if (i == 0):
                self.screen.blit(text, (self.screenHeight / 5, 70, 1000, 100))
            elif (i == 80):
                self.screen.blit(text, (self.screenHeight / 5, 100, 1000, 100))
            else:
                self.screen.blit(text, (self.screenHeight / 5, 130, 1000, 100))

        durationText = fontBigArial.render("Durée: "+duration, True, (255, 255, 255))
        self.screen.blit(durationText, (self.screenWidth / 5 * 4.2, self.screenHeight / 10))
        pygame.font.quit()




    def testAffichage(self):

        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.detection.leftHand[0]-5, self.detection.leftHand[1]-5), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.rightHand[0]-5,  self.detection.rightHand[1]-5), 10)