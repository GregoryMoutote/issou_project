import pygame.draw

from Interfaces.PlayInterface import *
from Model.Stage.Level import *
from random import *
from Model.Stage.Stage import *
import os

class LevelSelectionInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.detection=detection
        self.settings=settings
        self.stages=[]
        self.index=2;

        super().__init__(screenData, screen)
        self.pre_load_all_stages()

        self.background = pygame.image.load("Pictures/Interfaces/fond.png")

        self.bannerTopPicture = pygame.image.load("Pictures/Interfaces/bannerTop.png")
        self.bannerTopPicture = pygame.transform.scale(self.bannerTopPicture,(self.screen_width, self.screen_height / 4.5))

        self.bannerBottomPicture = pygame.image.load("Pictures/Interfaces/bannerBottom.png")
        self.bannerBottomPicture = pygame.transform.scale(self.bannerBottomPicture,(self.screen_width, self.screen_height *0.2))

        self.starUnchecked = pygame.image.load("Pictures/Interfaces/starUnchecked.png")
        self.starUnchecked = pygame.transform.scale(self.starUnchecked,(60, 60))

        self.starChecked = pygame.image.load("Pictures/Interfaces/starChecked.png")
        self.starChecked = pygame.transform.scale(self.starChecked,(60, 60))

        self.levels=[]
        for stage in self.stages:
            self.levels.append(Level(self.screen_width*0.35+self.screen_height*0.1,self.screen_height*0.17,stage.name,3,stage.name,stage.stage_music.description,stage.difficulty,stage.stage_music.duration))

        self.randomButton=PictureButton(self.screen_width * 0.8, self.screen_height * 0.86, self.screen_height * 0.13, self.screen_height * 0.13, self.screen, "dice.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.upButton=PictureButton(self.screen_width * 0.9, self.screen_height * 0.86, self.screen_height * 0.13, self.screen_height * 0.13, self.screen, "arrowUp.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.downButtun=PictureButton(self.screen_width * 0.7, self.screen_height * 0.86, self.screen_height * 0.13, self.screen_height * 0.13, self.screen, "arrowDown.png", "", 50, 50, "Arial.ttf", (255, 255, 255))
        self.quitButton=PictureButton(0, self.screen_width * 0.9, self.screen_height * 0.25, self.screen_height * 0.08, self.screen, "button1.png", "retour", 50, 50, "Glitch.otf", (255, 255, 255))
        self.playButton=PictureButton(self.screen_width / 5, self.screen_height / 2 - 100, 200, 200, self.screen, "play.png", "", 0, 0, "", (0, 0, 0))

        self.show()
        self.resetCoo()
        self.loop()


    def loop(self):
        continuer=True

        while continuer:
            if len(self.detection.media_pipe.right_hand) > 0:
                self.rightX = self.detection.media_pipe.right_hand[0]
                self.rightY = self.detection.media_pipe.right_hand[1]

            if len(self.detection.media_pipe.left_hand) > 0:
                self.leftX = self.detection.media_pipe.left_hand[0]
                self.leftY = self.detection.media_pipe.left_hand[1]

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.media_pipe.is_fist_closed = 1

            self.showHand()

            if self.detection.media_pipe.is_fist_closed == 1:
                if self.rightX>self.quitButton.x and self.rightX<(self.quitButton.x + self.quitButton.width) and self.rightY>self.quitButton.y and self.rightY<(self.quitButton.y + self.quitButton.height):
                   continuer=False

                elif self.rightX>self.playButton.x and self.rightX<(self.playButton.x + self.playButton.width) and self.rightY>self.playButton.y and self.rightY<(self.playButton.y + self.playButton.height):
                    PlayInterface(self.screen_data, self.screen, self.detection, self.settings, self.stages[self.index])
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

        self.screen.blit(self.bannerTopPicture, (0, 0))
        self.screen.blit(self.bannerBottomPicture, (0, self.screen_height*0.8))

        self.musicPicture = pygame.image.load("stages/"+picture+"/"+picture+".png")
        self.musicPicture = pygame.transform.scale(self.musicPicture,(self.screen_height / 5 - 20, self.screen_height / 5 - 20))
        self.screen.blit(self.musicPicture, (10, 10))

        for i in range(0,5):
            if(i<nbStar):
                self.screen.blit(self.starChecked, (self.screen_width*0.75+70*i, 10))
            else:
                self.screen.blit(self.starUnchecked,(self.screen_width*0.75+70*i, 10))

        if(len(name)>15):
            name=name[0:15]+"..."

        min=str(int(duration/60))
        sec=str(int(duration%60))

        pygame.font.init()
        fontGlitch=pygame.font.Font("Fonts/Glitch.otf",70)
        fontArial=pygame.font.Font("Fonts/Arial.ttf",30)
        fontBigArial = pygame.font.Font("Fonts/Arial.ttf", 40)

        title = fontGlitch.render(name, True, (255, 255, 255))

        if(difficulty==0):
            difficultyText = fontBigArial.render("EASY", True, (0, 255, 0))
        elif(difficulty==1):
            difficultyText = fontBigArial.render("MEDIUM", True, (255, 128, 0))
        else:
            difficultyText = fontBigArial.render("HARD", True, (255, 0, 0))

        for i in range(0, len(description), 80):
            text = fontArial.render(description[i:i + 80], True, (255, 255, 255))
            if (i == 0):
                self.screen.blit(text, (self.screen_height / 5, 70, 1000, 100))
            elif (i == 80):
                self.screen.blit(text, (self.screen_height / 5, 100, 1000, 100))
            else:
                self.screen.blit(text, (self.screen_height / 5, 130, 1000, 100))

        durationText = fontBigArial.render("Durée: "+min+":"+sec, True, (255, 255, 255))
        pygame.font.quit()

        self.screen.blit(title, (self.screen_height / 5, 10))
        self.screen.blit(difficultyText, (self.screen_width*0.64, 25))
        self.screen.blit(durationText, (self.screen_width / 5 * 4.2, self.screen_height / 10))


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.playButton.show_button()

        if(len(self.levels)>4):
            for i in range(0,5):
                if(i==2):
                    self.levels[i].show(self.screen, self.screen_width * 0.60, self.screen_height * 0.17* i+self.screen_height*0.075)
                else:
                    self.levels[i].show(self.screen,self.screen_width*0.65,self.screen_height*0.17*i+self.screen_height*0.075)
        else:
            for i in range(0, len(self.levels)):
                if (i == 2):
                    self.levels[i].show(self.screen, self.screen_width * 0.60, self.screen_height * 0.164 * i)
                else:
                    self.levels[i].show(self.screen, self.screen_width * 0.65, self.screen_height * 0.164 * i)

        if(len(self.levels)>2):
            self.showDescription(self.levels[2].name,self.levels[2].picture,self.levels[2].difficulty,self.levels[2].description,self.levels[2].duration,self.levels[2].mark)

        self.upButton.show_button()
        self.downButtun.show_button()
        self.quitButton.show_button()
        self.randomButton.show_button()


    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0


    def showHand(self):
        self.show()
        if len(self.detection.media_pipe.left_hand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.media_pipe.right_hand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)
        pygame.display.update()

    def pre_load_all_stages(self):
        self.file=os.listdir("stages")
        for file in self.file:
            self.stages.append(Stage("stages/"+file+"/"+file+".issou",self.screen))