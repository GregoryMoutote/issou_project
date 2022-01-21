import pygame


class Settings:

    def __init__(self):
        self.chargeChange()

    def setAnimation(self,anim):
        self.animation=anim

    def changeAnimation(self):
        if self.animation:
            self.animation=False
        else:
            self.animation=True

    def getAnimation(self):
        return self.animation

    def setVolume(self,vol):
        self.volume=vol
        pygame.mixer.music.set_volume(self.volume*0.1)

    def getVolume(self):
        return self.volume

    def saveChange(self):
        fichier = open("data.issou", "w")
        fichier.write("Data file ISSOU\n")
        fichier.write(str(self.volume)+"\n")
        fichier.write(str(self.animation)  + "\n")
        fichier.close()

    def chargeChange(self):
        with open("data.issou", "r") as filin:
            line = filin.readline()
            if line=="Data file ISSOU\n":
                self.volume=int(filin.readline())
                if filin.readline()=="True\n":
                    self.animation =True
                else:
                    self.animation = False
            else:
                print("erreur chargement du fichier de settings")
                self.volume=5
                self.animation=True
        pygame.mixer.music.set_volume(self.volume*0.1)
