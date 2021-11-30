import pygame

class Botton:

    def __init__(self,x,y,width,height,screen,color,text,textSize,textLeftSpace,font,textColor):

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.screen=screen
        self.color=color
        self.text=text
        self.textSize=textSize
        self.textLeftSpace=textLeftSpace
        self.font="font/"+font
        self.textColor=textColor
        self.botton=pygame.Rect(x,y,width,height)
        self.showTarget()

    def showTarget(self):
        pygame.font.init()
        pygame.draw.rect(self.screen, self.color, self.botton)
        myfont = pygame.font.Font(self.font, self.textSize)
        textsurface = myfont.render(self.text, True, self.textColor)
        self.screen.blit(textsurface, (self.x+self.textLeftSpace, self.y+(self.height-self.textSize)/2))
        pygame.display.update()
        pygame.font.quit()