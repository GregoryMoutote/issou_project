import pygame

class Level:

    def __init__(self, width, height, name, mark, picture, description, difficulty, duration):
        self.name = name
        self.mark = mark
        self.picture = picture
        self.description = description
        self.difficulty = difficulty
        self.duration = duration
        self.logo_dimension = height
        self.text_size=int(height*0.25)
        self.background = pygame.image.load("Pictures/Interfaces/button2.png")
        self.background = pygame.transform.scale(self.background, (width, height))

    def show(self, screen, x, y):
        screen.blit(self.background, (x, y))

        image = pygame.image.load("stages/" + self.picture + "/" + self.picture + ".png")
        image = pygame.transform.scale(image, (self.logo_dimension - 15, self.logo_dimension - 10))
        screen.blit(image, (x + 10, y + 5))

        pygame.font.init()

        fontGlitch = pygame.font.Font("Fonts/Glitch.otf",self.text_size)

        if (len(self.name) > 18):
            textsurface = fontGlitch.render(self.name[0:18] + "..", True, (255, 255, 255))
        else:
            textsurface = fontGlitch.render(self.name, True, (255, 255, 255))
        screen.blit(textsurface, (x + self.logo_dimension, y + 10))
        pygame.font.quit()