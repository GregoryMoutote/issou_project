class Settings:

    def __init__(self):
        self.animation=True
        self.volume=5

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

    def getVolume(self):
        return self.volume