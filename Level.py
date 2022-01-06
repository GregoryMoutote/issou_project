import pygame

class level:

    def __init__(self,name,marck,picture,descritpion,difficulty,duration):
        self.name=name
        self.marck=marck
        self.picture=picture
        self.descritpion=descritpion
        self.difficulty=difficulty
        self.duration=duration

    def show(self,screen,x,y,width,height):
        if self.difficulty=="EASY":
            level = pygame.image.load("./picture/interface/easyLevelBackground.png")
            level = pygame.transform.scale(level,(width,height))
            screen.blit(level,(x,y))

        if self.difficulty=="MEDIUM":
            level = pygame.image.load("./picture/interface/mediumLevelBackground.png")
            level = pygame.transform.scale(level, (width, height))
            screen.blit(level, (x, y))

        if self.difficulty=="HARD":
            level = pygame.image.load("./picture/interface/hardLevelBackground.png")
            level = pygame.transform.scale(level, (width, height))
            screen.blit(level, (x, y))

        image = pygame.image.load("./picture/music/"+self.picture)
        image = pygame.transform.scale(image, (height-10, height-10))
        screen.blit(image, (x+5, y+5))

        pygame.font.init()

        fontGlitch = pygame.font.Font("./font/Glitch.otf", 30)

        textsurface = fontGlitch.render(self.name, True, (255,255,255))
        screen.blit(textsurface,(x+height, y+10))
        pygame.font.quit()