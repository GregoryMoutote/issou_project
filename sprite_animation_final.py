import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y,screen):
		super().__init__()
		self.screen=screen
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('picture/chargement_1.png'))
		self.sprites.append(pygame.image.load('picture/chargement_2.png'))
		self.sprites.append(pygame.image.load('picture/chargement_3.png'))
		self.sprites.append(pygame.image.load('picture/chargement_4.png'))
		self.sprites.append(pygame.image.load('picture/chargement_5.png'))
		self.sprites.append(pygame.image.load('picture/chargement_6.png'))
		self.sprites.append(pygame.image.load('picture/chargement_7.png'))
		self.sprites.append(pygame.image.load('picture/chargement_8.png'))
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