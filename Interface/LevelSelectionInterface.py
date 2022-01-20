import pygame.draw

from Interface.PlayInterface import *
from Level import *
from random import *
from Stage import *
import os

class LevelSelectionInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.detection=detection
        self.settings=settings
        self.stages=[]
        self.index=2;

        super().__init__(screenData, screen)
        self.pre_load_all_stages()

        self.background = pygame.image.load("./picture/interface/levelSelectionBackground.png")

        self.levels=[]
        for stage in self.stages:
            self.levels.append(level(stage.name,3,stage.name,stage.stage_music.description,stage.difficulty,stage.stage_music.duration))

        self.randomButton=pictureButton(self.screenWidth * 0.8, self.screenHeight * 0.86, self.screenHeight * 0.13, self.screenHeight * 0.13, self.screen, "dice.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.upButton=pictureButton(self.screenWidth * 0.9, self.screenHeight * 0.86, self.screenHeight * 0.13, self.screenHeight * 0.13, self.screen, "arrowUp.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.downButtun=pictureButton(self.screenWidth * 0.7, self.screenHeight * 0.86, self.screenHeight * 0.13, self.screenHeight * 0.13, self.screen, "arrowDown.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.quitButton=pictureButton(0, self.screenHeight * 0.9, self.screenWidth * 0.25, self.screenHeight * 0.08, self.screen, "button1.png", "retour", 50, 50, "Glitch.otf", (255, 255, 255))
        self.playButton=pictureButton(self.screenWidth / 5,self.screenHeight / 2 - 100,200,200,self.screen,"play.png","",0,0,"",(0,0,0))

        self.show()
        self.resetCoo()
        self.loop()


    def loop(self):
        continuer=True

        while continuer:


            if len(self.detection.mediaPipe.rightHand) > 0:
                self.rightX = self.detection.mediaPipe.rightHand[0]
                self.rightY = self.detection.mediaPipe.rightHand[1]

            if len(self.detection.mediaPipe.leftHand) > 0:
                self.leftX = self.detection.mediaPipe.leftHand[0]
                self.leftY = self.detection.mediaPipe.leftHand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.mediaPipe.isFistClosed = 1

            self.showHand()

            if self.detection.mediaPipe.isFistClosed == 1:
                if self.rightX>self.quitButton.x and self.rightX<(self.quitButton.x + self.quitButton.width) and self.rightY>self.quitButton.y and self.rightY<(self.quitButton.y + self.quitButton.height):
                   continuer=False

                elif self.rightX>self.playButton.x and self.rightX<(self.playButton.x + self.playButton.width) and self.rightY>self.playButton.y and self.rightY<(self.playButton.y + self.playButton.height):
                    PlayInterface(self.screenData, self.screen, self.detection, self.settings, self.stages[self.index])
                    self.show()
                    self.resetCoo()

                elif self.rightX>self.downButtun.x and self.rightX<(self.downButtun.x + self.downButtun.width) and self.rightY>self.downButtun.y and self.rightY<(self.downButtun.y + self.downButtun.height):
                    self.levels.append(self.levels[0])
                    del self.levels[0]
                    self.show()
                    self.resetCoo()
                    if(self.index==len(self.levels)-1):
                        self.index=0
                    else:
                        self.index+=1

                elif self.rightX>self.upButton.x and self.rightX<(self.upButton.x + self.upButton.width) and self.rightY>self.upButton.y and self.rightY<(self.upButton.y + self.upButton.height):
                    self.levels.insert(0,self.levels[len(self.levels)-1])
                    del self.levels[len(self.levels)-1]
                    self.show()
                    self.resetCoo()
                    if(self.index==0):
                        self.index=len(self.levels)-1
                    else:
                        self.index-=1

                elif self.rightX>self.randomButton.x and self.rightX<(self.randomButton.x + self.randomButton.width) and self.rightY>self.randomButton.y and self.rightY<(self.randomButton.y + self.randomButton.height):
                    for i in range(0,int(random()*len(self.levels))):
                        self.levels.append(self.levels[0])
                        del self.levels[0]
                        if (self.index == len(self.levels) - 1):
                            self.index = 0
                        else:
                            self.index += 1
                    self.resetCoo()
                    self.show()


    def showDescription(self,name,picture,difficulty,description,duration,nbStar):

        self.bannerTopPicture = pygame.image.load("./picture/interface/bannerTop.png")
        self.bannerTopPicture = pygame.transform.scale(self.bannerTopPicture,(self.screenWidth, self.screenHeight / 4.5))
        self.screen.blit(self.bannerTopPicture, (0, 0))

        self.musicPicture = pygame.image.load("stages/"+picture+"/"+picture+".png")
        self.musicPicture = pygame.transform.scale(self.musicPicture,(self.screenHeight / 5 - 20, self.screenHeight / 5 - 20))
        self.screen.blit(self.musicPicture, (10, 10))

        self.starUnchecked = pygame.image.load("./picture/interface/starUnchecked.png")
        self.starUnchecked = pygame.transform.scale(self.starUnchecked,(60, 60))

        self.starChecked = pygame.image.load("./picture/interface/starChecked.png")
        self.starChecked = pygame.transform.scale(self.starChecked,(60, 60))

        for i in range(0,5):
            if(i<nbStar):
                self.screen.blit(self.starChecked, (self.screenWidth*0.75+70*i, 10))
            else:
                self.screen.blit(self.starUnchecked,(self.screenWidth*0.75+70*i, 10))

        pygame.font.init()
        fontGlitch=pygame.font.Font("./font/Glitch.otf",70)
        fontArial=pygame.font.Font("./font/Arial.ttf",30)
        fontBigArial = pygame.font.Font("./font/Arial.ttf", 40)

        if(len(name)>15):
            name=name[0:15]+"..."

        self.title = fontGlitch.render(name, True, (255, 255, 255))
        self.screen.blit(self.title, (self.screenHeight / 5, 10))

        if(difficulty==0):
            self.difficulty = fontBigArial.render("EASY", True, (0, 255, 0))
        elif(difficulty==1):
            self.difficulty = fontBigArial.render("MEDIUM", True, (255, 128, 0))
        else:
            self.difficulty = fontBigArial.render("HARD", True, (255, 0, 0))
        self.screen.blit(self.difficulty, (self.screenWidth*0.64, 25))

        for i in range(0, len(description), 80):
            text = fontArial.render(description[i:i + 80], True, (255, 255, 255))
            if (i == 0):
                self.screen.blit(text, (self.screenHeight / 5, 70, 1000, 100))
            elif (i == 80):
                self.screen.blit(text, (self.screenHeight / 5, 100, 1000, 100))
            else:
                self.screen.blit(text, (self.screenHeight / 5, 130, 1000, 100))

        min=str(int(duration/60))
        sec=str(int(duration%60))

        durationText = fontBigArial.render("Durée: "+min+":"+sec, True, (255, 255, 255))
        self.screen.blit(durationText, (self.screenWidth / 5 * 4.2, self.screenHeight / 10))
        pygame.font.quit()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.playButton.showButton()

        if(len(self.levels)>5):
            for i in range(0,6):
                if(i==2):
                    self.levels[i].show(self.screen, self.screenWidth * 0.60, self.screenHeight * 0.164 * i, self.screenWidth * 0.40, self.screenHeight * 0.167)
                else:
                    self.levels[i].show(self.screen,self.screenWidth*0.65,self.screenHeight*0.164*i,self.screenWidth*0.35,self.screenHeight*0.167)
        else:
            for i in range(0, len(self.levels)):
                if (i == 2):
                    self.levels[i].show(self.screen, self.screenWidth * 0.60, self.screenHeight * 0.164 * i,self.screenWidth * 0.40, self.screenHeight * 0.167)
                else:
                    self.levels[i].show(self.screen, self.screenWidth * 0.65, self.screenHeight * 0.164 * i,self.screenWidth * 0.35, self.screenHeight * 0.167)

        if(len(self.levels)>2):
            self.showDescription(self.levels[2].name,self.levels[2].picture,self.levels[2].difficulty,self.levels[2].descritpion,self.levels[2].duration,self.levels[2].marck)

        self.upButton.showButton()
        self.downButtun.showButton()
        self.quitButton.showButton()
        self.randomButton.showButton()


    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0


    def showHand(self):
        self.show()
        if len(self.detection.mediaPipe.leftHand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.mediaPipe.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)
        pygame.display.update()

    def pre_load_all_stages(self):
        self.file=os.listdir("stages")
        for file in self.file:
            self.stages.append(Stage("stages/"+file+"/"+file+".issou",self.screen))
