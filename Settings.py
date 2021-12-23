class Settings:

    def __init__(self):
        self.animation=True
        self.volume=5

    @classmethod
    def setAnimation(self,anim):
        self.animation=anim

    @classmethod
    def getAnimation(self):
        return self.animation

    @classmethod
    def setVolume(self,vol):
        self.volume=vol

    @classmethod
    def getVolume(self):
        return self.volume

