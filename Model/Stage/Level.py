import pygame

class Level:

    def __init__(self, name, mark, picture, description, difficulty, duration):
        self.name = name
        self.mark = mark
        self.picture = picture
        self.description = description
        self.difficulty = difficulty
        self.duration = duration

    def show(self, screen, x, y, width, height):
        if self.difficulty == 0:
            level = pygame.image.load("./Pictures/Interfaces/easyLevelBackground.png")
            level = pygame.transform.scale(level,(width,height))
            screen.blit(level, (x, y))

        if self.difficulty == 1:
            level = pygame.image.load("./Pictures/Interfaces/mediumLevelBackground.png")
            level = pygame.transform.scale(level, (width, height))
            screen.blit(level, (x, y))

        if self.difficulty == 2:
            level = pygame.image.load("./Pictures/Interfaces/hardLevelBackground.png")
            level = pygame.transform.scale(level, (width, height))
            screen.blit(level, (x, y))

        image = pygame.image.load("Stages/" + self.picture + "/" + self.picture + ".png")
        image = pygame.transform.scale(image, (height-10, height-10))
        screen.blit(image, (x+5, y+5))

        pygame.font.init()

        font_glitch = pygame.font.Font("./Fonts/Glitch.otf", 30)

        if (len(self.name) > 18):
            text_surface = font_glitch.render(self.name[0:18] + "..", True, (255, 255, 255))
        else:
            text_surface = font_glitch.render(self.name, True, (255, 255, 255))
        screen.blit(text_surface, (x + height, y + 10))
        pygame.font.quit()