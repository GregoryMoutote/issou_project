import pygame.draw

from Interface.Interface import *
from Bottun.PictureBottun import *
from Level import *
from random import *

class LevelSelectionInterface(interface):

    def __init__(self,detection,screenData,screen):
        self.detection=detection
        self.detection.initHandCapture()

        super().__init__(screenData, screen)

        self.background = pygame.image.load("./picture/interface/fond.png")
        self.fondLogo=pygame.image.load("./picture/interface/fondLogo.png")

        self.levels=[level("Day of the Lords",3,"day of the Lords.png","description de Day of the Lords","MEDIUM","3:20")]
        self.levels.append(level("One More Time",4,"one More Time.png","description One More Time","MEDIUM","2:56"))
        self.levels.append(level("Something",5,"something.png","descritpion Something","HARD","3:03"))
        self.levels.append(level("Welcome Home",2,"welcome Home.png","description Welcome Home","EASY","2:59"))
        self.levels.append(level("In Bloom",4,"in Bloom.png","description In Bloom","MEDIUM","3:42"))
        self.levels.append(level("On the Run",4,"on the Run.png","description On the Run","EASY","4:01"))
        self.levels.append(level("Welcome to the Machine",3,"welcome to the Machine.jpg","description Welcome to the Machine","EASY","2:51"))
        self.levels.append(level("In the Flesh?",4,"in the Flesh.jpg","description In the Flesh?","MEDIUM","3:00"))
        self.levels.append(level("Thriller",1,"thriller.jpg","description Thriller","HARD","5:51"))

        self.bannerBottomPicture = pygame.image.load("./picture/interface/bannerBottom.png")
        self.bannerBottomPicture = pygame.transform.scale(self.bannerBottomPicture,(self.screenWidth, self.screenHeight*0.15))

        self.randomBottun=pictureBottun(self.screenWidth*0.8,self.screenHeight*0.86,self.screenHeight*0.13,self.screenHeight*0.13,self.screen ,"dice.png","",50,50,"Arial.ttf",(255,255,255))
        self.upBottun=pictureBottun(self.screenWidth*0.9,self.screenHeight*0.86,self.screenHeight*0.13,self.screenHeight*0.13,self.screen ,"arrowUp.png","",50,50,"Arial.ttf",(255,255,255))
        self.downBottun=pictureBottun(self.screenWidth*0.7,self.screenHeight*0.86,self.screenHeight*0.13,self.screenHeight*0.13,self.screen ,"arrowDown.png","",50,50,"Arial.ttf",(255,255,255))
        self.quitBottun=pictureBottun(0,self.screenHeight*0.9,self.screenWidth*0.25,self.screenHeight*0.08,self.screen,"bottun1.png","retour",50,50,"Glitch.otf",(255,255,255))

        self.show()
        self.resetCoo()

        continuer=True

        while continuer:

            detection.hand_detection()
            self.testAffichage()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()

            if len(self.detection.rightHand) > 0:
                self.rightX = self.detection.rightHand[0]
                self.rightY = self.detection.rightHand[1]

            if len(self.detection.leftHand) > 0:
                self.leftX = self.detection.leftHand[0]
                self.leftY = self.detection.leftHand[1]

            if self.rightX>self.quitBottun.x and self.rightX<(self.quitBottun.x+self.quitBottun.width) and self.rightY>self.quitBottun.y and self.rightY<(self.quitBottun.y+self.quitBottun.height):
               continuer=False

            if self.rightX>self.downBottun.x and self.rightX<(self.downBottun.x+self.downBottun.width) and self.rightY>self.downBottun.y and self.rightY<(self.downBottun.y+self.downBottun.height):
                self.levels.append(self.levels[0])
                del self.levels[0]
                self.show()
                self.resetCoo()

            if self.rightX>self.upBottun.x and self.rightX<(self.upBottun.x+self.upBottun.width) and self.rightY>self.upBottun.y and self.rightY<(self.upBottun.y+self.upBottun.height):
                self.levels.insert(0,self.levels[len(self.levels)-1])
                del self.levels[len(self.levels)-1]
                self.show()
                self.resetCoo()

            if self.rightX>self.randomBottun.x and self.rightX<(self.randomBottun.x+self.randomBottun.width) and self.rightY>self.randomBottun.y and self.rightY<(self.randomBottun.y+self.randomBottun.height):
                for i in range(0,int(random()*len(self.levels))):
                    self.levels.append(self.levels[0])
                    del self.levels[0]
                self.resetCoo()
                self.show()

            self.testAffichage()
            pygame.display.update()

    def showDescription(self,name,picture,difficulty,description,duration,nbStar):

        self.bannerTopPicture = pygame.image.load("./picture/interface/bannerTop.png")
        self.bannerTopPicture = pygame.transform.scale(self.bannerTopPicture,(self.screenWidth, self.screenHeight / 4.5))
        self.screen.blit(self.bannerTopPicture, (0, 0))

        self.musicPicture = pygame.image.load("./picture/music/"+picture)
        self.musicPicture = pygame.transform.scale(self.musicPicture,(self.screenHeight / 5 - 20, self.screenHeight / 5 - 20))
        self.screen.blit(self.musicPicture, (10, 10))

        self.starUnchecked = pygame.image.load("./picture/interface/starUnchecked.png")
        self.starUnchecked = pygame.transform.scale(self.starUnchecked,(60, 60))

        self.starChecked = pygame.image.load("./picture/interface/starChecked.png")
        self.starChecked = pygame.transform.scale(self.starChecked,(60, 60))

        for i in range(0,5):
            if(i<nbStar-0.5):
                self.screen.blit(self.starChecked, (self.screenWidth*0.75+70*i, 10))
            else:
                self.screen.blit(self.starUnchecked,(self.screenWidth*0.75+70*i, 10))

        pygame.font.init()
        fontGlitch=pygame.font.Font("./font/Glitch.otf",70)
        fontArial=pygame.font.Font("./font/Arial.ttf",30)
        fontBigArial = pygame.font.Font("./font/Arial.ttf", 40)

        self.title = fontGlitch.render(name, True, (255, 255, 255))
        self.screen.blit(self.title, (self.screenHeight / 5, 10))

        self.difficulty = fontBigArial.render(difficulty, True, (255, 0, 0))
        self.screen.blit(self.difficulty, (self.screenWidth*0.64, 25))

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


    def show(self):
        self.screen.blit(self.background, (0, 0))

        self.musicPicture = pygame.image.load("./picture/interface/play.png")
        self.musicPicture = pygame.transform.scale(self.musicPicture,(200, 200))
        self.screen.blit(self.musicPicture, (self.screenWidth/5, self.screenHeight/2-100))

        for i in range(0,len(self.levels)):
            if(i==2):
                self.levels[i].show(self.screen, self.screenWidth * 0.60, self.screenHeight * 0.167 * i, self.screenWidth * 0.40, self.screenHeight * 0.167)
            else:
                self.levels[i].show(self.screen,self.screenWidth*0.65,self.screenHeight*0.167*i,self.screenWidth*0.35,self.screenHeight*0.167)

        self.showDescription(self.levels[2].name,self.levels[2].picture,self.levels[2].difficulty,self.levels[2].descritpion,self.levels[2].duration,self.levels[2].marck)
        self.screen.blit(self.bannerBottomPicture, (0, self.screenHeight * 0.85))

        self.upBottun.showBottun()
        self.downBottun.showBottun()
        self.quitBottun.showBottun()
        self.randomBottun.showBottun()
        pygame.display.update()

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0


    def testAffichage(self):

        if len(self.detection.leftHand)>0:
            #print("right", self.detection.leftHand[0], "  ", self.detection.leftHand[1])
            pygame.draw.circle(self.screen, (255, 0, 0), (self.detection.leftHand[0]-5, self.detection.leftHand[1]-5), 10)

        if len(self.detection.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.detection.rightHand[0]-5,  self.detection.rightHand[1]-5), 10)