import pygame,threading,os,time

from Model.Stage.Coordinates import *

class Animation(pygame.sprite.Sprite):
	def __init__(self, screen,coordonate,sprites):
		super().__init__()
		#thread = AnimationThread(screen, coordonate,name)  # crée le thread
		#thread.start()
		self.screen = screen
		self.sprites = []
		self.coordonne = coordonate
		self.sprites=sprites
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.coordonne.x, self.coordonne.y]


	def show(self):
		if self.current_sprite < len(self.sprites):
			image = self.sprites[int(self.current_sprite)]
			self.current_sprite += 1
			time.sleep(0.03)
			self.screen.blit(image, (self.rect.x, self.rect.y))
			return False
		return True