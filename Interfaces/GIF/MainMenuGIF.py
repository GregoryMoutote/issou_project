import pygame, sys

class MenuGIF(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y,screen):
		super().__init__()
		self.screen=screen
		self.attack_animation = False
		self.sprites = []
		for image_id in range(1, 50):
			if image_id < 10:
				self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-0' + \
													  str(image_id) + '.gif'))
			else:
				self.sprites.append(pygame.image.load('Pictures/Interfaces/gif/ISSOUMainMenu/frame-' + \
													  str(image_id) + '.gif'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]

	def update(self,speed):
		self.current_sprite += speed
		if int(self.current_sprite) >= len(self.sprites):
			self.current_sprite = 0
			self.attack_animation = False
		self.image = self.sprites[int(self.current_sprite)]