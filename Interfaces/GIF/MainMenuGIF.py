import pygame, sys

class MenuGIF(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y,screen):
		super().__init__()
		self.screen=screen
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-01.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-02.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-03.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-04.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-05.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-06.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-07.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-08.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-09.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-10.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-11.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-12.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-13.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-14.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-15.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-16.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-17.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-18.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-19.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-20.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-21.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-22.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-23.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-24.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-25.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-26.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-27.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-28.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-29.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-30.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-31.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-32.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-33.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-34.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-35.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-36.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-37.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-38.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-39.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-40.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-41.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-42.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-43.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-44.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-45.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-46.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-47.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-48.gif'))
		self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-49.gif'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def update(self,speed):
		self.current_sprite += speed
		if int(self.current_sprite) >= len(self.sprites):
			self.current_sprite = 0
			self.attack_animation = False
		self.image = self.sprites[int(self.current_sprite)]