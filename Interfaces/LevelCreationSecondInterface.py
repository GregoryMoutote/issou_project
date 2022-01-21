import pygame.draw

from Buttons import CocheButton
from Interfaces.Interface import *
from Buttons.TimelineButton import *
from Buttons.PictureButton import *
from Buttons.CocheButton import *
from Buttons.MenuLevelCreationButton import *
from Targets.Target import *
from Model.Constants import *
import time
import os

class LevelCreationSecondInterface(Interface):

    def __init__(self,screenData,screen,detection,settings):
        self.settings=settings
        self.detection=detection

        super().__init__(screenData, screen)

        self.isSelectedTarget=False
        self.selectedPicture=None
        self.selectedPictureName=None
        self.lastClick=time.time()

        self.background=pygame.image.load("./Pictures/Interfaces/levelBuilderBackground.png")
        self.background=pygame.transform.scale(self.background, (self.screenWidth*0.80+1, self.screenHeight*0.80+1))

        self.rightMenu=pygame.image.load("./Pictures/Interfaces/menuBackground.png")
        self.rightMenu=pygame.transform.scale(self.rightMenu, (self.screenWidth, self.screenHeight*0.20))

        self.bottomMenu=pygame.image.load("./Pictures/Interfaces/menuBackground.png")
        self.bottomMenu=pygame.transform.scale(self.bottomMenu, (self.screenWidth*0.20,self.screenHeight ))

        self.playButton=CocheButton(self.screenWidth*0.05, self.screenHeight*0.82, self.screenHeight*0.1, self.screenHeight*0.1, self.screen,"levelCreationPlay.png","levelCreationPause.png",True)
        self.fullscreenButton=CocheButton(self.screenWidth*0.26, self.screenHeight*0.82, self.screenHeight*0.1, self.screenHeight*0.1, self.screen,"maximiser.png","minimiser.png",True)
        self.importDeleteButton=CocheButton(self.screenWidth*0.8,self.screenHeight*0.8,self.screenWidth*0.2,self.screenHeight*0.1,self.screen,"deleteButton.png","importButton.png",False)

        self.bottuns = [PictureButton(self.screenWidth * 0.12, self.screenHeight * 0.82, self.screenHeight * 0.1, self.screenHeight * 0.1, self.screen, "minusTen.png", "", 0, 0, "", (255, 255, 255))]
        self.bottuns.append(PictureButton(self.screenWidth * 0.19, self.screenHeight * 0.82, self.screenHeight * 0.1, self.screenHeight * 0.1, self.screen, "plusTen.png", "", 0, 0, "", (255, 255, 255)))

        self.timeline=TimelineButton(self.screenWidth*0.05,self.screenHeight*0.95,self.screenWidth*0.9,self.screenHeight*0.02,self.screen,"timelineGray.png","timelineRed.png")

        self.placeTarget=[]

        self.BasicTargetsList=[]
        i=1;
        for file in os.listdir("Pictures/Targets"):
            if file!="Transparent":
                self.BasicTargetsList.append(MenuLevelCreationButton(self.screenWidth * 0.8, self.screenHeight * 0.1 * i, self.screenWidth * 0.1, Constants.TARGET_RADIUS * 1.6, self.screen, file, file[6:-4], 35, 10, "arial.ttf", (255, 255, 255)))
                i+=1

        self.ImportTargetsList=[]

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
                    if event.key == pygame.K_SPACE:
                        self.timeline.changeStat(self.timeline.percent+1)
                    if event.key == pygame.K_ESCAPE:
                        continuer=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rightX, self.rightY = pygame.mouse.get_pos()
                    self.detection.mediaPipe.isFistClosed=1

            self.showHand()

            if self.detection.mediaPipe.isFistClosed==1:
                #bouton -10 sec
                if self.rightX > self.bottuns[0].x and self.rightX < (self.bottuns[0].x + self.bottuns[0].width) and self.rightY > self.bottuns[0].y and self.rightY < (self.bottuns[0].y + self.bottuns[0].height):
                    self.resetCoo()
                    self.show()

                # bouton +10 sec
                elif self.rightX > self.bottuns[1].x and self.rightX < (self.bottuns[1].x + self.bottuns[1].width) and self.rightY > self.bottuns[1].y and self.rightY < (self.bottuns[1].y + self.bottuns[1].height):
                    self.resetCoo()
                    self.show()

                #bouton play
                elif self.rightX > self.playButton.x and self.rightX < (self.playButton.x + self.playButton.width) and self.rightY > self.playButton.y and self.rightY < (self.playButton.y + self.playButton.height):
                    self.playButton.changeStat()
                    self.resetCoo()
                    self.show()

                #bouton pleine écran
                elif self.rightX > self.fullscreenButton.x and self.rightX < (self.fullscreenButton.x + self.fullscreenButton.width) and self.rightY > self.fullscreenButton.y and self.rightY < (self.fullscreenButton.y + self.fullscreenButton.height):
                    self.fullscreenButton.changeStat()
                    self.resetCoo()
                    self.show()

                #gestion du bouton d'import et de suppréssion
                elif self.rightX > self.importDeleteButton.x and self.rightX < (self.importDeleteButton.x + self.importDeleteButton.width) and self.rightY > self.importDeleteButton.y and self.rightY < (self.importDeleteButton.y + self.importDeleteButton.height):
                    if self.isSelectedTarget:
                        self.importDeleteButton.actif=True
                        self.delete()
                    else:
                        self.importDeleteButton.actif = False
                    self.resetCoo()
                    self.show()

                #placer les cibles
                elif self.rightX > Constants.TARGET_RADIUS and self.rightX < self.screenWidth*0.8-Constants.TARGET_RADIUS and self.rightY >  Constants.TARGET_RADIUS and self.rightY < self.screenHeight*0.8-Constants.TARGET_RADIUS:
                    if self.isSelectedTarget:
                        if(time.time()-self.lastClick>1):
                            self.lastClick=time.time()
                            print(self.selectedPictureName[:-4])
                            self.placeTarget.append(Target([0,self.rightX,self.rightY,10,10,25,self.selectedPictureName[:-4]],self.screen,self.selectedPictureName[:-4]))
                            self.isSelectedTarget = False
                            self.importDeleteButton.actif = False
                            self.resetCoo()
                            self.show()

                #choix d'un nouveau type de cible
                for target in self.BasicTargetsList:
                    if self.rightX > target.x and self.rightX < (target.x + target.width) and self.rightY > target.y and self.rightY < (target.y + target.height):
                        self.selectedPicture = target.picture
                        self.selectedPictureName=target.pictureNane
                        self.isSelectedTarget = True

                        if self.isSelectedTarget:
                            self.importDeleteButton.actif = True
                        else:
                            self.importDeleteButton.actif = False
                        self.show()

                #déplacement de cible
                for target in self.placeTarget:
                    if self.rightX > target.coordinates.x and self.rightX < (target.coordinates.x +Constants.TARGET_RADIUS) and self.rightY > target.coordinates.y and self.rightY < (target.coordinates.y +Constants.TARGET_RADIUS   ):
                        if(time.time()-self.lastClick>1):
                            self.lastClick=time.time()
                            self.isSelectedTarget = True
                            picture = pygame.image.load("Pictures/Targets/" + str(target.pictureName)+".png")
                            self.selectedPicture = pygame.transform.scale(picture, (Constants.TARGET_RADIUS*0.8, Constants.TARGET_RADIUS*0.8))
                            self.selectedPictureName = target.pictureName
                            self.placeTarget.remove(target)

                            if self.isSelectedTarget:
                                self.importDeleteButton.actif = True
                            else:
                                self.importDeleteButton.actif = False
                            self.show()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.bottomMenu,(self.screenWidth*0.8,0))
        self.screen.blit(self.rightMenu,(0,self.screenHeight*0.8))
        self.playButton.showButton()
        self.fullscreenButton.showButton()
        self.importDeleteButton.showButton()

        for button in self.bottuns:
            button.showButton()
        for target in self.BasicTargetsList:
            target.showButton()
        for place in self.placeTarget:
            if place!=None:
                place.showTarget()

        if self.isSelectedTarget:
            self.screen.blit(self.selectedPicture,(self.rightX-Constants.TARGET_RADIUS*0.8,self.rightY-Constants.TARGET_RADIUS*0.8))

        self.timeline.showButton()
        pygame.font.init()
        myfont = pygame.font.Font("./Fonts/arial.ttf", 50)
        textsurface = myfont.render("Choix des cibles", True, (255, 255, 255))
        pygame.font.quit()
        self.screen.blit(textsurface,(self.screenWidth*0.82,self.screenHeight*0.02))


    def showHand(self):
        self.show()
        if len(self.detection.mediaPipe.leftHand)>0:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.leftX-5, self.leftY-5), 10)

        if len(self.detection.mediaPipe.rightHand)>0:
           pygame.draw.circle(self.screen, (255, 255, 255), (self.rightX-5, self.rightY-5), 10)
        pygame.display.update()

    def resetCoo(self):
        self.rightX=0
        self.rightY=0
        self.leftX=0
        self.leftY=0

    def delete(self):
        self.isSelectedTarget = False
        self.selectedPicture = None
        self.selectedPictureName = None